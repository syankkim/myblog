---
title: 스레드 pthread 구현
tags: ['thread']
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-05-27 23:50:54
---

POSIX thread와 그 사용법 익혀보기.
`#Pthread` `#pthread_join` `#pthread_detach`
<!-- excerpt -->
<!-- toc -->

---

# 스레드

## pthread
- `POSIX 스레드` 또는 `Pthread` 라고 부른다.
- 저수준 API로 100 여개의 함수 제공
- 복잡하지만 유닉스 시스템 핵심 스레딩 라이브러리
- 다른 스레딩 솔루션도 결국 Pthread 를 기반으로 구현되어 있으므로 익혀둘 가치가 있다.
- 기본 라이브러리 `(glibc) 와 분리`된 `libpthread` 라이브러리에 pthread 구현되어 있으므로
컴파일시 명시적으로 `pthread 옵션`이 필요하다.
- pthread API는 `Semaphore를 포함하지 않는다`.

## Pthread 라이브러리
- <pthread.h> 헤더 파일에서 정의한다.
- 모든함수는 `pthread_` 로 시작한다.

## 스레드 생성

* 스레드 생성
  - thread_inst(): 9까지 출력
  - main 함수: thread_inst 스레드 생성후, 4까지 출력

```shell
#include<pthread.h>
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>

void * thread_inst(void *arg){
    pthread_t tid;
    tid = pthread_self();

    int i=0;
    while(i<10){
        printf("[%lx] new thread: %d\n", tid, i);
        i++;
        sleep(1);
    }
}

int main(){
    pthread_t thread;
    pthread_create(&thread, NULL, thread_inst, NULL);
    pthread_t tid= pthread_self();

    int i=0;
    while(i<5){
        printf("[%lx] main thread: %d\n", tid, i);
        i++;
        sleep(1);
    }
}

```

* 스레드 실행결과
  - 아래처럼 9까지 출력되어야 할 new thread 는 main 함수가 끝나니 함께 끝나버렸다.
  - 다음 예제의 pthread_join 추가가 필요하다.
```shell
ubuntu@ip-172-31-33-123:~$ gcc pthread.c -pthread -o pthread
ubuntu@ip-172-31-33-123:~$ ./pthread
[7f93eb31c740] main thread: 0
[7f93eaaee700] new thread: 0
[7f93eb31c740] main thread: 1
[7f93eaaee700] new thread: 1
[7f93eb31c740] main thread: 2
[7f93eaaee700] new thread: 2
[7f93eb31c740] main thread: 3
[7f93eaaee700] new thread: 3
[7f93eb31c740] main thread: 4
[7f93eaaee700] new thread: 4
```

## 스레드 관리

* 리소스
 1. pthread_join
  - 메인 스레드에서 해당 스레드가 종료되면, 상태값을 보고 메인스레드에서 `추가처리`를 할 수 있다.
 2. pthread_detach(thread1)
  - 관련 리소스를 `즉시 해제`한다.
  
* 실행
 1. pthread_join
  - 스레드 1이 종료될때까지 다음코드를 수행하지 않고 `기다린다`.
 2. pthread_detach
  - 스레드 1이 종료될때까지 `기다리지 않는다`.

## Pthread 뮤텍스 - 상호배제 기법

~~~~  ~~`
