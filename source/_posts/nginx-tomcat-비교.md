---
title: 'Nginx & Tomcat 비교'
tags: ['apache', 'nginx', 'C10K', 'MPM', 'PreFork', 'Worker']
categories: [☁️ Web]
img: <img width="300" src="https://user-images.githubusercontent.com/28856435/83641005-e074c980-a5e7-11ea-92d3-c89fd6ba9662.png">
permalink: ''
date: 2020-06-03 22:12:06
---

<!-- ![0_UneV-I-bBldmqkgK](https://user-images.githubusercontent.com/28856435/83641005-e074c980-a5e7-11ea-92d3-c89fd6ba9662.png)
Nginx & Apache 를 비교하며 각 장단점을 알아봅니다. -->
`apache` `nginx` `C10K` `MPM` `PreFork` `Worker`
<!-- excerpt -->
<!-- toc -->

## Nginx 란,
>apache 의 C10K 문제점 해결을 위해 만들어진 `Event-Driven` 구조의 웹서버SW 라고 합니다.  OSI7 Layer 중 application Level 아래의 Level 에서 Nginx 같은 웹서버가 HTTP 통신을 담당합니다.

**`C10K` 일만개의 클라이언트 문제**
한 시스템에 동시 접속자수가 1만명이 넘어갈 때 효율적방안

---

## Nginx & Apache
`Nginx` 는 `Tomcat` 과 비교되어 그 장점을 설명할 수 있습니다.

### Apache 
`MPM 방식`으로 HTTP 요청을 처리합니다.
>MPM : Multi-Process Module 은 크게 두 가지 방식이 있습니다.
`PreFork 방식` `Worker 방식`

* __PreFork MPM (다중 프로세스)__
o Client 요청에 대해 apache 자식 프로세스를 생성하여 처리합니다.
o 요청이 많을 경우 Process 를 생성하여 처리합니다. 이 방식은 Apache 설치시 default 로 설정되어 있습니다.
o 하나의 자식프로세스당 `하나의 스레드` 를 갖습니다. (최대 1024개)
o 스레드간 메모리 공유를 하지 않습니다. 이 방식은 독립적이기에 안정적인 반면, 메모리 소모가 크다는 단점이 있습니다.

* __Worker MPM (멀티 프로세스-스레드)__
o Prefork 보다 메모리 사용량이 적고 동시접속자가 많은 사이트에 적합합니다. 각 프로세스의 스레드를 생성해 처리하는 구조입니다.
o 스레드 간의 메모리 공유가 가능합니다.
o 프로세스 당 최대 64개의 스레드처리가 가능하며, 각 스레드는 하나의 연결만을 부여받습니다.

### Apache 의 한계
>**클라이언트 접속마다 Process 혹은 Thread 를 생성하는 구조입니다.** 1만 클라이언트로부터 동시접속 요청이 들어온다면 CPU 와 메모리 사용이 증가하고 추가적인 Process/Tread 생성비용이 드는 등 대용량 요청에서 한계를 보입니다.
또한, Apache 서버의 프로세스가 `blocking` 될 때 요청을 처리하지 못하고 처리가 완료될 때까지 대기상태에 있습니다. 이는 `Keep Alive(접속대기)` 로 해결이 가능하지만, 효율이 떨어집니다.

---


### 다시 Nginx 를 살펴봅시다.

>Nginx 는 위에서 언급했듯이 Event-Driven 방식으로 동작합니다. 즉, 프로그램 흐름이 이벤트에 의해 결정이 됩니다.
한 개 또는 고정된 프로세스만 생성하고, 그 내부에서 비동기로 효율적인 방식으로 task 를 처리합니다. Apache 와 달리 동시접속자 수가 많아져도 추가적인 생성비용이 들지 않습니다.

o 비동기 이벤트 기반으로 요청하여 적은양의 스레드가 사용되기 때문에 CPU소모가 적습니다.
o Apache 와 달리 CPU 와 관계없이 I/O 들을 전부 Event Listener로 미루기 때문에 흐름이 끊이지 않습니다.
o `context switching` 비용이 적습니다.

**`[Context Switching]`**
`Context: 스레드가 작업을 진행하는동안 작업정보 (레지스터, 커널스택, 사용자스택 등)를 보관`
`O/S 는 A작업을 진행할 때 A스레드의 Context를 읽어오며, B스레드로 전환 할 때 A스레드의 Context를 저장하고 B스레드의 Context를 읽어오는 일련의 반복작업을 합니다.`
`즉, 스레드 갯수가 많아질 수록 context switching 작업은 더 빈번하게 일어나고 이 때문에 성능이 저하될 수 있습니다.`


### Apache & Nginx 장점
O Apache 는 Nginx 에 비해 모듈이 다양합니다.
O Apache 의 안정성, 확장성, 호환성을 장점으로 들자면, Nginx 는 성능이 우세하다는 장점이 있습니다.

## 어느것이 더 나은가

>Apache 나 Nginx 모두 각 웹서버마다의 장단점을 가지고 있으므로 사용에 있어서 정답은 없습니다. 상황과 비용에 따라, 혹은 안정성이나 효율성에 따라 적합한 웹서버를 사용한면 되지 않을까 합니다.