---
title: 프로세스ID
tags: []
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-05-24 22:24:11
---

시스템콜 함수로 직접 시스템 프로그래밍 해보기.
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

## 시스템콜 함수 사용해보기

### getpid() getppid() 시스템콜
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

### fork() exec() 시스템콜
- fork() : 새로운 프로세스 공간을 별도로 만들고, fork() 를 호출한 프로세스(부모) 공간을 모두 `복사`한다.
 - 헤더: `<unistd.h>`
 - 함수: `pid_t fork(void);`
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

- exec() : 호출한 현재 프로세스 공간의 `TEXT, DATA, BSS` 영역을 새로운 프로세스의 이미지로 `덮어씌운다`. 별도의 공간을 만들지 않는다.

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

### wait() 시스템콜
- fork() 함수 호출시 자식 프로세스가 종료할 때까지 `부모 프로세스가 기다린다.`
- wait() 자식 프로세스와 부모 프로세스의 동기화, 부모 프로세스가 먼저 죽는 경우를 막기 위해 사용한다. (고아 프로세스: 자식 프로세스가 메모리를 계속 사용하고 있을 수 있다.)
- 자식 프로세스의 일이 끝나면 부모 프로세스에 시그널을 보낸다. SIGCHL

### fork(), execl(), wait() 사용한 프로그램 만들기
- execl() 만 사용하면, 부모 프로세스가 사라진다.
 - 이를 유지위해 fork() 로 새로운 공간 복사 후, execl() 사용.






