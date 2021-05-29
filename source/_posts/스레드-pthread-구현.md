---
title: 스레드 pthread 구현
tags: []
categories:
  - ☁️
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-05-27 23:50:54
---

<!-- excerpt -->
<!-- toc -->

---

# 스레드

## pthread
- POSIX 스레드 또는 Pthread 라고 부른다.
- 저수준 API로 100 여개의 함수 제공
- 복잡하지만 유닉스 시스템 핵심 스레딩 라이브러리
- 다른 스레딩 솔루션도 결국 Pthread 를 기반으로 구현되어 있으므로 익혀둘 가치가 있다.
- 기본 라이브러리 (glibc) 와 분리된 libpthread 라이브러리에 pthread 구현되어 있으므로
컴파일시 명시적으로 pthread 옵션이 필요하다.
- pthread API는 Semaphore를 포함하지 않는다.

## 스레드 조인

## 스레드 디테치

* 리소스
 1. pthread_join
  - 메인 스레드에서 해당 스레드가 종료되면, 상태값을 보고 메인스레드에서 추가처리를 할 수 있다.
 2. pthread_detach(thread1)
  - 관련 리소스를 즉시 해제한다.
  
* 실행
 1. pthread_join
  - 스레드 1이 종료될때까지 다음코드를 수행하지 않고 기다린다.
 2. pthread_detach
  - 스레드 1이 종료될때까지 기다리지 않는다.

## Pthread 뮤텍스 - 상호배제 기법

~~~~  ~~`

# 메모리 & mmap

## mmap 함수 사용
```cpp
#include <sys/mman.h>
void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);
```
- addr: 매핑할 메모리 `주소`
- len: 메모리 `공간의 크기`
- prot: 보호 모드
- flags: 매핑된 데이터의 처리 방법을 지정하는 상수
- fildes: 파일 기술자
- off: 파일 오프셋

**`문제`**
- 기존에 `파일 - 프로세스` 에 접근할경우,
 - 프로세스에서는 시스템콜, 스케줄러, 인터럽트 등의 기법을 사용하기 위해 OS가 처리할일이 많아서 
 - 파일을 가지고 있는 CPU에서는 DMA 나 SystemBus 를 사용해야 한다.
  - 즉, 성능이 떨어질 수 밖 에 없다.

**`해결`**
- `파일 - 메모리 - 프로세스` : 중간에 메모리를 두어, 파일의 특정공간을 미리 메모리 영역에 매핑해둔다.
 - 자주 엑세스할 파일이 있다면, 프로세스는 메모리 영역에 접근하여 빠르게 읽어올 수 있다.
- mmap는 프로세스의 주소공간을 파일에 대응시킨다. 파일은 운영체제 전역적인 자원이므로 당연히 어렵잖게 `다른 프로세스와 공유`해서 사용할 수 있을 것이다.

 ## mmap 동작
 1. mmap 실행시, 가상 메모리 주소에 file 주소를 매핑한다. (페이지 디렉토리)
 2. 해당 메모리 접근시(요구페이징, lazy allocation)
  - `페이지폴트 인터럽트` 발생
  - OS에서 file data 를 복사해서 물리메모리 페이지에 넣어준다.
3. 메모리 read: 해당 물리 페이지 데이터를 읽음
4. 메모리 write: 해당 물리 페이지 데이터 수정후, 페이지 상태 flag 중 dirty bit를 1로 수정
5. 파일 close: 물리 페이지 데이터가 file에 업데이트됨. (dirty bit 가 1인곳)

### 파일, 메모리 가상메모리
- 장점
 - read(), write 시에 반복적인 파일접근을 방지하여 성능을 개선한다.
 - mapping 된 영역은 파일 처리를 위한 lseek() `file->data주소 찾아가는 함수`를 사용하지 않고 간단한 포인터 조작으로 탐색.

단점
 - mmap은 내부적으로 가상메모리와 연관되어 `페이지 사이즈 단위로 매핑`된다. 그런데 고정된 페이지 사이즈 단위보다 클 경우 추가공간이 필요하고, 적을 경우 공간낭비(0으로 채움)가 일어난다.

## 파일처리 성능개선 munmap
- *addr 에 mapping 된 물리 메모리 주소를 해제한다.
- lenght: mapping된 메모리크기 (mmap과 동일값)

## 맵핑된 메모리 영역을 동기화 하는 방법
- MS_ASYNC: 비동기 방식으로 결과에 관계 없이 프로그램 속행
- MS_SYNC: 동기 방식으로 결과를 확인 후 프로그램 속행
- MS_ALERT: 동기화 후 시그널을 통해 알림.
- MS_INVALIDATE: 현제 메모리 맵을 무효화함.


---
 
# inode 방식 파일시스템

* inode의 메타데이터에는 아래와 같은 정보들이 포함된다.
 - Mode: 파일종류/권한
 - Owner Info: 소유자,소울그룹
 - Size: 파일사이즈
 - Timestamps: 생성, 수정시간
 - Direct blocks (12개): 직접적으로 주소가리킴
 - Single inderect, Double inderect, Triple inderect: 간접적 주소가리킴

> 이러한 inode 메타데이터를 모두 가져오는 함수가 있다. `stat` 함수

## stat 함수

> __사용 문법__
int stat(const char *path, struct stat *buf);
*buf : 구조체 변수
- stat: 파일을 `filepath` 로 지정한다.
- fstat: 파일을 `fd 넘버`로 지정한다.
- lstat: 파일을 `filepath 로 지정`하되 지정된 파일이 `심볼릭 링크 파일`이면 링크파일 자체에 대한 정보를 얻는다.

```cpp
struct stat {
 dev_t     st_dev;  // ID of device containing file
                          // :: 가상파일 시스템 file-system interface 를 사용하여 하단부에 있는 실제    디바이스의  종류는 달리할 수 있다. `추상화` `UNIX 모든것은 파일`
 ino_t     st_ino;  // inode number
 mode_t    st_mode;  // 파일 종류 및 접근권한
 nlink_t   st_nlink;  // hardlink 의 횟수
 uid_t     st_uid;  // 파일 owner
 gid_t     st_gid;  // group ID of owner
 off_t     st_size;  // 파일크기
 blksize_t st_blksize; // blocksize for file system I/O
 blkcnt_t  st_blocks;  // number of 512B blocks allocated
 time_t    st_atime;  // time if last access
 time_t    st_mtime;  // time if last modification
 time_t    st_ctime;  // time if last status change
}
```

### stat-test.c 실습

* 실제로 hello.txt 라는 파일의 메타데이터를 출력해보는 stat-test.c

```cpp
#include<stdio.h>
#include<sys/stat.h>

int main(){
  int ret= 0;
  struct stat buf;
  ret= stat("hello.txt", &buf);
  if(ret < 0){
    printf("ERROR\n");
    return 0;
  }
  printf("deviceId:%ld, inode:%ld, hardLinkCount:%ld, filesize: %ld, blockSize:%ld, blockCount:%ld \n", buf.st_dev, buf.st_ino, buf.st_nlink, buf.st_size, buf.st_blksize, buf.st_blocks);

  return 0;
}
```

* 출력 결과

```shell
~$ ./stat-test
deviceId:51713, inode:256331, hardLinkCount:1, filesize: 7, blockSize:4096, blockCount:8
```

# Standard Stream 표준 입출력 스트림
- 모든 스트림은 일반적인 plain text로 console에 출력된다.
- 표준 입력 스트림(Standard Input Stream): stdid
- 표준 입력 스트림(Standard Ouput Stream): stdout
- 표준 입력 스트림(Standard Error Stream): stderr

### std-test.c 실습

* 아래 프로그램을 실행하면, 터미널에 입력할 때마다 stdin 에 들어가고, stdout 으로 출력되는 것을 확인할 수 있다.

```cpp
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char** argv){

        char buf[255];
  FILE* fp; // 파일 디스크립터

  if(argc == 2){  // 인자가 들어오면,
    fp= fopen(argv[1], "r"); // 읽기오픈

    if(fp == NULL){
      fputs("file open error", stderr);
      exit(0);
    }

  }else{
      fp= stdin; // 터미널에 입력된 데이터가 표준입력(stdin)에 들어간다.
  }

  while(fgets(buf, 255, fp) != NULL){
    fputs(buf, stdout); // 파일 표준출력(stdout)
  }
}
```

* 실행 결과

```shell
~$ ./std-test
hello // stdin
hello // stdout
입력  // stdin
입력  // stdout
```
