---
title: 프로세스 IPC 기법
tags: ['ipc']
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-05-26 23:13:08
---

IPC 기법을 직접 실습해본다.
<!-- excerpt -->
<!-- toc -->

---

# IPC 기법

## 파이프
- 부모 프로세스와 자식 프로세스가 같은 `kernel 공간`을 공유한다. 즉, 같은 물리주소를 바라보고 있다.
- `단방향` 통신이다. 부모프로세스 -> 자식프로세스

### 파이프 예제
- 부모프로세스가 `write` 한 msg를 `pipe`를 통해 자식프로세스가 `read` 한다.

* pipe.c

```cpp
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>

#define MSGSIZE 255

char* msg="Hello Child Process";

int main(){

        char buf[255];
        int fd[2], pid, nbytes;

        // 파이프 생성: pipe(fd)= -1이면 pipe가 생성되지 않은것.
        if(pipe(fd)<0)
                exit(1); // 종료

        // 부모-자식 프로세스 생성
        pid= fork();
        printf("after fork pid : %d\n", pid);

        if(pid>0){ // 부모 프로세스

                printf("[1] Parent: %d, Child: %d\n", getpid(), pid);
                // 부모 프로세스가 fd[1] 에 쓴다.
                write(fd[1], msg, MSGSIZE);
                exit(0);
        }else{
                //자식 프로세스에는 pid값이 0
                 printf("[2] Parent: %d, Child: %d\n", getpid(), pid);

                 nbytes = read(fd[0], buf, MSGSIZE);
                 printf("nbytes: %d , msg: %s\n", nbytes, buf);
                 exit(0);

        }
        return 0;
}
```

### 파이프 실행 결과
- pid=0 일 때 자식 프로세스이며, 아래와 같이 부모 프로세스가 저장한 `msg` 를 읽어오는 것을 확인할 수 있다.

```shell
$ ./_ipc
[1] Parent: 21768, Child: 21769
$ [2] Parent: 21769, Child: 0
nbytes: 255 , msg: Hello Child Process
```
---

## 메시지 큐
- `kernel 공간`의 메모리를 사용한다.
- `양방향` 통신이 가능하다.
- 먼저 들어간 메시지부터 읽는다.

### 메시지 큐 예시
-  `msgrcv`(int msgid, void *msgp, size_t msgsz, long msgtype, int msgflag)
  - msgtype: 0일때 첫번째 데이터부터 읽고 그 이상이라면 그 type에 일치하는 데이터부터 읽는다.
  - msgflag: 0: 블록모드, IPC_NOWAIT: 비블록모드

- 보내는 프로세스 msgSnd.c, 받는 프로세스 msgRcv.c 를 따로 만들어 수행한다.

* msgSnd.c

```cpp
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/msg.h>

typedef struct msgbuf {
        long type;
        char text[50];
} MsgBuf;

int main(void){
        int msgid, len;
        MsgBuf msg;
        key_t key = 1234;
        // IPC_CREAT: 새로운 키는 식별자 생성(접근권한)
        msgid= msgget(key, IPC_CREAT|0644); // => rw‑r‑‑r‑‑

        if(msgid == -1){
                perror("msgget");
                exit(1);
        }
        msg.type = 1;
        // 아래 메시지 전송
        strcpy(msg.text, "Message Queue is Executed\n");
        if(msgsnd(msgid, (void *)&msg, 50, IPC_NOWAIT) == -1){ 
                perror("msgsnd");
                exit(1);
        }
        return 0;
}


```

* msgRcv.c

```cpp
#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<string.h>
#include<sys/msg.h>

typedef struct msgbuf {
        long type;
        char text[50];
} MsgBuf;

int main(void){
        int msgid, len;
        MsgBuf msg;
        key_t key = 1234;
        // IPC_CREAT: 새로운 키는 식별자 생성(접근권한)
        msgid= msgget(key, IPC_CREAT|0644); // => rw‑r‑‑r‑‑
        if(msgid == -1){
                perror("msgget");
                exit(1);
        }
        len= msgrcv(msgid, &msg, 50, 0, 0);
        printf("Got a Message ! => %s [%d] \n", msg.text, len);
        return 0;
}

```

### 메시지큐 실행 결과
- msgSnd - 보내고 , msgRcv - 받는다.

```shell
ubuntu@ip-172-31-42-223:~$ gcc msgRcv.c -o msgRcv
ubuntu@ip-172-31-42-223:~$ gcc msgSnd.c -o msgSnd
ubuntu@ip-172-31-42-223:~$ ./msgSnd
ubuntu@ip-172-31-42-223:~$ ./msgRcv
Got a Message ! => Message Queue is Executed
 [50]
```
<br>


> __ftok() - 키 생성을 위한 함수__
>- path 경로명의 inode 값과 숫자값(id)을 기반으로 생성된다.
>- 경로 삭제 후 재생성시 inode값이 달라지므로 기존과 다른 값을 리턴한다.
>```cpp
#include<sys/ipc.h>
key_t ftok(const char *path, int id);

// 예시
key = ftok("keyfile", 1); // 메시지큐를 통해서 부모-자식 프로세스 간 공유
id = msgget(key, IPC_CREAT|0640);
```