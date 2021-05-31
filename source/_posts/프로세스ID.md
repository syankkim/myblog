---
title: 시스템콜을 이용한 프로세스 관리
tags: ['system_call']
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
status: ''
date: 2021-05-24 22:24:11
---

시스템콜 함수를 직접 사용하면서 프로세스의 생성과 종료, 우선순위 관리까지 경험해본다.
`#fork` `#exec` `#wait` `#COW` `#exit` `#nice`
<!-- excerpt -->
<!-- toc -->

---

# 프로세스 생성
- 생성과정
 (1) TEXT, DATA, BSS, HEAP, STACK 의 공간을 생성한다.
 (2) 프로세스 이미지를 해당 공간에 업로드하고 실행한다.

## 프로세스 소유자 관리
```shell
$ ps -ef
$ sudo vi /etc/passwd
$ sudo vi /etc/shadow
```

# 시스템콜 함수사용

## getpid() getppid() 시스템콜
- getpid(), getppid() 함수를 사용하여 test_ps.c 프로그램 예시.

```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(){
        printf("pid=%d\n", getpid());
        printf("ppid=%d\n", getppid());
}
```
* 아래와 같이 `pid`, `ppid` 가 정상적으로 출력되는것을 확인할 수 있다.

```shell
ubuntu@ip-172-31-42-223:~/test$ gcc test_ps.c -o test_ps
ubuntu@ip-172-31-42-223:~/test$ ls
dir  loop.c  soft  soft_link  softlink  test_ps  test_ps.c
ubuntu@ip-172-31-42-223:~/test$ ./test_ps
pid=14611
ppid=14529
```

## fork() exec() - 프로세스 생성

### fork()
> 새로운 프로세스 공간을 별도로 만들고, fork() 를 호출한 프로세스(부모) 공간을 모두 `복사`한다.
- 함수 사용
```c
<unistd.h>
pid_t fork(void);
```

- 자식프로세스는 `pid=0`, 부모프로세스는 `실제 pid`
- pid= fork() 실행되면 부모 프로세스와 동일한 자식 프로세스를 `별도 메모리공간`에 생성한다.
 - 두 프로세스의 변수, PC(Program Counter)값은 동일하다.

* _fork.c
```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(){
  pid_t pid;
  printf("Before fork() call\n");
 // -- 여기까지 프로세스는 1개

  pid = fork();
  if(pid==0)
    printf("Child Process");
}
```

### exec()
>호출한 현재 프로세스 공간의 `TEXT, DATA, BSS` 영역을 새로운 프로세스의 이미지로 `덮어씌운다`. 별도의 공간을 만들지 않는다.

 - 헤더
 - 함수 6가지
  
  - execlp : path 명 포함. 

* _execl.c
```c
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(){
  printf("execute ls\n");
  execl("/bin/ls","ls","-l",NULL);
  // argv[0]=ls, argv[1]=-l
  // -- 기존의 'ls al' 의 기능이 덮어씌워진다.
  perror(execl is failed\n);
  // - 에러코드 출력
  exit(1);
}

```

## wait() - 기다림
>- fork() 함수 호출시 자식 프로세스가 종료할 때까지 `부모 프로세스가 기다린다.`
>- wait() 자식 프로세스와 부모 프로세스의 동기화, 부모 프로세스가 먼저 죽는 경우를 막기 위해 사용한다. (고아 프로세스: 자식 프로세스가 메모리를 계속 사용하고 있을 수 있다.)
>- 자식 프로세스의 일이 끝나면 부모 프로세스에 `SIGCHLD` 시그널을 보낸다. 

![KakaoTalk_20210526_002054322](https://user-images.githubusercontent.com/28856435/119525382-6a99dd00-bdb9-11eb-9517-fd7ebb48d420.jpg)

<br>

### wait() 시스템콜 사용
  - 리턴값은 종료된 `자식 프로세스의 pid` 이다.

```cpp
#include <sys/wait.h>
pid_t wait (int *status)
// 사용: status 를 통해 자식 프로세스 정보 확인
int WIFEXITED(status); // 0 이 아닐때 정상종료
```

* test_wait.c 실습

```cpp
#include<sys/types.h>
#include<stdio.h>
#include<sys/wait.h>
#include<unistd.h>
#include<string.h>
#include<stdlib.h>
#include<errno.h>

int main(){
  int pid;
  int child_pid;
  int status;
  int ret;

  pid= fork();

  switch(pid){
    case -1:
      perror("fork is failed\n");
      break;
    csae 0: // pid : 자식
      execl("/bin/ls", "ls", "-al", NULL);
      perror("execl is failed\n");
      break;
    default: // pid : 부모
      // 부모프로세스는 자식 프로세스가 끝나길 기다림
      // status에 자식프로세스의 상태를 담아줌
      child_pid= wait(&status);
      printf("Parent PID(%d), Child PID (%d)\n", getpid(), child_pid)

      // 0 이 아니면 정상종료.
      ret = WIFEXITED(status);
      
      if(ret != 0){
        // 정상종료
        printf("Child process is normally terminated\n")
      }else{
        // 비정상 종료
        printf("Child process is abnormally terminated\n")
      }
      exit(0);
  }
}
```


## fork(), execl(), wait() 사용한 프로그램 만들기
- execl() 만 사용하면, 부모 프로세스가 사라진다.
 - 이를 유지위해 fork() 로 새로운 공간 복사 후, execl() 사용.


* fork_execl_wait.c

```cpp
#include<unistd.h>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<sys/wait.h>
#include<sys/types.h>

#define MAXLINE 64

int main(int argc, char **argv){
        char buf[MAXLINE];
        int proc_status;
        pid_t pid;
        printf("DaveShell ver 1.0\n");

        while(1){
            // memset(void *ptr, int value, size_t num);
            // ptr: 채우고자하는 메모리 시작포인터
            // value: 메모리에서 채우고자하는값. 1byte마다 0x00(64)로 초기화
            // sizeof: 배열의 전체 바이트 크기
            memset(buf, 0x00, MAXLINE);

            // buf 출력해보기
            // for(int i=0; i<(sizeof(buf)/sizeof(char)); i++){
            //     printf("%c\n", buf[i]);
            // }

            // char *fgets (char *string, int n, FILE *stream)
            // -- 파일에서 최대 MAXLINE-1 만큼 읽어서  buf 에 담음
            fgets(buf, MAXLINE-1, stdin);

            if(strncmp(buf, "exit\n", 5)==0){
              // strncmp(buf와 'exit\n' 의 문자열이 size5만큼) 같은지 문자열 비교
              // exit 를 입력후 enter치면 while문 종료
                break;
            }

            buf[strlen(buf)-1]=0x00;

            // 새로운 공간을 만들고 부모프로세스로부터 복사
            pid= fork();
            if(pid==0){ // 자식 프로세스
                // 실행한 사용자의 PATH 환경변수
                if(execl(buf, buf, NULL)==-1){
                    printf("command execution is failed\n");
                    exit(0);
                }
            }
            if(pid>0){
                wait(NULL); // 자식 프로세스 waiting
            }
        }
        return 0;
}
```

* fork_execl_wait 결과
  - `/bin/ls` 를 입력하면 해당 명령 수행.

```cpp
~$ ./fork_exec_wait
DaveShell ver 1.0

/bin/ls
a.txt  a_link.txt  b.txt  b_link.txt  fork_exec_wait  fork_exec_wait.c
```

### copy-on-write(COW) - 프로세스 생성
> copy-on-write 
`수정 (쓰기;write)` 가 일어날 때 복사한다.

- 자식 프로세스 생성시, 부모 프로세스 자원(페이지)을 우선 사용한다.
 - 커널 공간을 공유한다.
- `READ` 요청
  자식 프로세스 생성시, 부모 프로세스에서 사용하고 있는 물리주소를 그대로 사용(포인터랑 비슷하다고 생각하면 된다.)
- `WRITE` 요청
 (1) write 요청
 (2) Physical Memory : 부모 프로세스로의 물리 메모리 복사
 (3) PCB : 자식 프로세스의 Page Pointer 변경


## exit() - 프로세스 종료

```cpp
#include <stdlib.h>
void exit(int status);
// 사용
// EXIT_SUCCESS 는 0, exit(EXIT_SUCCESS); // EXIT_SUCCESS 는 0
exit(EXIT_SUCCESS);
exit(EXIT_FAILURE);
```

- main 함수의 return 0; 과 exit(0)l 의 차이
 - `exit() ` : 즉시 프로세스를 종료한다. exit()함수 다음에 있는 코드는 실행하지 않는다.
 - `return 0` : 단순히 함수를 종료한다. 단, `main() 함수` 에서는 C 언어 실행파일에 포함된 `_start()` 함수를 호출한 뒤, 결과적으로는 exit() 함수가 호출된다.

 ### exit() 주요동작
 - atexit()에 등록된 함수 실행
 - 열려 있는 모든 입출력 스트림버퍼 삭제 (stdin, stdout, stdrerr 데이터)
 - 프로세스가 오픈한 파일을 모두 닫는다.
 - tmpfile() 함수를 통해 생성된 임시파일 삭제
  - `FILE *tmpfile(void)`

### atexit() 함수 예제
- atexit()에 등록된 함수 실행 순서를 확인하는 예제이다.

* test_exit.c

```cpp
#include <stdlib.h>
#include <stdlio.h>

int main(void){
    void hello(void);
    void goodbye(void);
    int ret;

    ret = atexit(hello);
    if (ret!=0) perror("Error in atexit\n");
    ret = atexit(goodbye);
    if (ret!=0) perror("Error in atexit\n");
    exit(EXIT_SUCCESS);
  }

  void hello(void){
    printf("hello\n")
  }
  void goodbye(void){
    printf("see you!\n")
  }
}
```

* 아래와 같은 실행 결과를 보면, 아래서부터 반대로 수행한다. goodbye() 함수 수행 후 hello()함수가 수행되었다.

```shell
$ see you!
$ hello
```

## 우선순위 기반 스케줄러
- Priority-Based 스케줄러 (우선순위 스케줄링)
  - 동적/정적
- 프로세스 중 `root` 가 소유한 프로세스만 우선순위를 높일 수 있다. 그 외의 프로세스는 낮출 수만 있다.
  - 즉, 일반유저는 nice 값을 증가만 가능하며 root는 nice값을 감소시켜서 우선순위를 높일 수 있다.
- 스케줄링 방식에 따라 `효과가 없을 수도` 있다.

### nice
- 기본값은 보통 `0`으로 시작한다.
- `-20 ~ 19` 까지 순위값을 조정할 수 있다.
- 값이 `작을수록` 우선순위가 높다.

```cpp
#include<unistd.h>
int nice (int inc);
```

- `nice -n 10 bash` bash 프로세스 기존값에서 10을 증가 시킨다.
- 새로운 프로세스가 추가된다.

```shell
ubuntu@ip-172-31-33-123:~$ ps -l
F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 R  1000   394 27607  0  80   0 -  7336 -      pts/0    00:00:00 ps
0 S  1000 27607 27606  0  80   0 -  5814 wait   pts/0    00:00:00 bash
ubuntu@ip-172-31-33-123:~$ nice -n 10 bash
ubuntu@ip-172-31-33-123:~$ ps -l
F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000   461 27607  0  90  10 -  5752 wait   pts/0    00:00:00 bash
0 R  1000   470   461  0  90  10 -  7336 -      pts/0    00:00:00 ps
0 S  1000 27607 27606  0  80   0 -  5814 wait   pts/0    00:00:00 bash
```

### renice
- nice 와 달리 기존의 PID 로 우선순위를 조정한다.
- `renice 15 27607` PID 27607의 우선순위를 10->15로 조정

```shell
ubuntu@ip-172-31-33-123:~$ renice 15 27607
27607 (process ID) old priority 0, new priority 15
ubuntu@ip-172-31-33-123:~$ ps -l
F S   UID   PID  PPID  C PRI  NI ADDR SZ WCHAN  TTY          TIME CMD
0 S  1000   461 27607  0  90  10 -  5752 wait   pts/0    00:00:00 bash
0 R  1000   492   461  0  90  10 -  7336 -      pts/0    00:00:00 ps
0 S  1000 27607 27606  0  95  15 -  5814 wait   pts/0    00:00:00 bash
```
### getpriority/setpriority
- 스케줄링 조작 시스템콜을 기본 제공한다. (POSIX 기반)

```cpp
#include <sys/resource.h>
int getpriority(int which, id_t who);
int setpriority(int which, id_t who, int value);
```

`which` 옵션
- 프로세스(PRIO_PROCESS)
- 프로세스 그룹(PRIO_PGRP)
- 사용자(PRIO_USER)

* root 소유로 우선순위변경 실행

```cpp
#include <sys/resource.h>
int which = PRIO_PROCESS;
id_t pid;
int ret;
pid = getpid();
ret = getpriority(which, pid); // 프로세스 우선순위를 가져온다.
ret = setpriority(which, pid, 5); //프로세스의 우선순위를 5로 설정
```







