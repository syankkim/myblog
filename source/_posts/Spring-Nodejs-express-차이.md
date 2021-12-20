---
title: Spring vs Nodejs
tags: ['nodejs','spring']
categories: ['☁️ NodeJS']
thumbnail: ''
permalink: ''
status: ''
date: 2021-12-20 14:50:14
---


Sping과 Node.js 각 프레임워크의 차이점은 무엇일까.
`#express` `#spring` `#nodejs`
<!-- excerpt -->
<!-- toc -->

---


# 프레임워크 종류
Spring과 Express를 직접적으로 비교하기 이전에 각 프레임워크 유형이 어떤 곳에 해당하는지 알아보니 좀 더 명확하게 비교해볼 수 있었다.

## 완전관리형 프레임워크
- Spring, Next.js, Django

> 이 유형에 속하는 프레임워크들은 제공하는 규칙이 확실히 정해져 있다.

* 다양한 기능 제공
  - `DI`(Dependency Injection): 각 클래스들의 의존성을 관리한다.
  - 내부적으로 `Container`가 Object들을 관리한다.
  - 디렉터리의 구조, 클래스의 이름 규칙을 제시한다. (Controller, Service ...)
  - Spring, Django에서는 `View/Templete 렌더링` 제공 (ex. Spring의 Thymeleaf)

* 다양한 라이브러리 지원 - `스프링화` 해버리는 마법💫
  - 외부 라이브러리나 모듈들을 모두 가져와 스프링 생태계에 넣어버린다.
    - Messeging Queue(Kafka, RabbitMQ), RDBMS(MySql, PostgreSql), NoSql(MongoDB, ElasticSearch) 등..
  - Spring Boot 사용시 라이브러리 버전관리가 쉽다.

  - `Next.js` 또한 동일하게 DI를 지원하는 프레임워크로, ORM(Typeorm, Sequerlize)을 내부적으로 지원하여 DB사용이 편하다.
    - 그 외 GraphQL, gRPC 기술 지원
  

## 미니멀리즘 프레임워크
- Express.js, Gin

> 미니멀리즘 프래임워크는 웹 요청만 처리하며, 약간의 기능만 지원한다. 덕분에 `빠른 속도의 API`를 사용할 수 있다.

* 자유로운 라이브러리와 아키텍쳐
  - 보안, DB, Messaging, Logging, Caching 등 사용자에게 맞는 형태로 `커스터마이징`이 가능하다.

* 단점이 존재한다.
  - 협업시에 각기 다른 스타일이 적용될 수 있기 때문에 코딩 컨벤션을 정하는것이 중요하다.
  - 라이브러리들 간 버전관리가 어렵다.
  - 어떤 라이브러리를 업데이트 하게되면, 그 라이브러리와 의존관계에 있는 라이브러리 때문에 코드가 동작하지 않을 수 있다.
    - `라이브러리들 간의 의존관계`를 잘 알아봐야한다.

---

# 동작 방식의 차이 SpringMVC & Node.js

## Spring MVC: Multi-Thread
Spring MVC 는 `Multi-Thread` 방식으로, 다중 요청을 동시에 처리한다. 각 요청-응답을 개별 Thread가 책임진다.
예를 들어 카페에서 `손님(client)`이 주문을 하고 주문(request)을 받은 `카운터(server)`가 그 손님이 주문한 음료가 나올때까지 다른 손님의 주문을 받지 않고 기다리는 것이다(response). 이는 그 카페 입장에서 자원의 낭비를 발생시킨다.

이러한 I/O 작업이 빈번하게 일어난다면, Thread들은 각 요청에 대한 응답을 받을때까지 블로킹된다.
또한 Thread 갯수가 증가할 때마다 context switching이 빈번하게 일어나면 성능 저하도 야기될 수 있다.


## Node.js: Single-Thread
> Node.js 는 스크립트 언어가 아닌, 프로그램 환경이다. 즉, `Chrome V8* 이라는 JavaScript 엔진으로 빌드된 JavaScript 런타임이다.`



Node.js는 `Single-Thread` 방식으로, 하나의 Thread가 모든 요청을 처리한다.
이는 `Async, Non-blocking I/O` 작업을 수용하며 `Event Loop`를 통한 높은 처리성능(이벤트 기반**) 때문에 가능하다.

즉, Node.js는 다음과 같은 환경에서 사용한다면 좋은 성능을 기대할 수 있다.

- 빈번한 I/O 작업 수행.
- 단순한 CPU 작업 진행.

<small>*V8 엔진: 구글이 V8엔진을 사용하여 크롬을 출시했으며, 다른 엔진과 달리 매우 빠르다.</small>
<small>**이벤트 기반(Event-driven): 이벤트가 발생할 때 미리 지정해둔 작업을 수행하는 방식.</small>

이전의 카페 예시에서 Node.js를 사용한다면, `카운터(server)`에서 미리 여러 `손님(client)`의 주문을(request) 받아놓고, 음료를 제조한다면 한 사람의 음료가 나올때까지 주문을 기다리는 방법보다 순조롭게 순환될 것이다.

![flat-design-people-sitting-at-cafe_52683-24023](https://user-images.githubusercontent.com/28856435/146717011-b777dd8a-ce30-4062-8caa-c0974fe51bb9.jpg)



---

# Reference
- [Node.js가 Spring MVC보다 성능상 유리할까?](https://appleg1226.tistory.com/33)
- [Node.js vs Spring Boot](https://siyoon210.tistory.com/164)
- [Node.js 개념 이해하기](https://hanamon.kr/nodejs-%EA%B0%9C%EB%85%90-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0/)