---
title: Spring vs Nodejs(express)_차이
tags: []
categories: ['☁️ TIL']
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-11-25 16:50:14
---


Sping과 Express 를 사용해보니 차이점이 궁금해졌다?!
`#express` `#spring` `#nodejs`
<!-- excerpt -->
<!-- toc -->

---

Spring과 Express를 직접적으로 비교하기 이전에 각 프레임워크 유형이 어떤 곳에 해당하는지 알아보니 좀 더 명확하게 비교해볼 수 있었다.

# 프레임워크 종류

## 완전관리형 프레임워크
- Spring, Next.js, Django

> 이 유형에 속하는 프레임워크들은 제공하는 규칙이 확실히 정해져 있다.

* 다양한 기능 제공
  - `DI`(Dependency Injection): 각 클래스들의 의존성을 관리한다.
  - 내부적으로 `Container`가 Object들을 관리한다.
  - 디렉터리의 구조, 클래스의 이름 규칙을 제시한다. (Controller, Service ...)
  - Spring, Django에서는 View/Templete 렌더링 제공 (ex. Spring의 Thymeleaf)

* 다양한 라이브러리 지원 - 스프링화 해버리는 마법💫
  - 외부 라이브러리나 모듈들을 모두 가져와 스프링 생태계에 넣어버린다.
    - Messeging Queue(Kafka, RabbitMQ), RDBMS(MySql, PostgreSql), NoSql(MongoDB, ElasticSearch) 등..
  - Spring Boot 사용시 라이브러리 버전관리가 쉽다.

  - Next.js 또한 동일하게 DI를 지원하는 프레임워크로, ORM(Typeorm, Sequerlize)을 내부적으로 지원하여 DB사용이 편하다.
    - 그 외 GraphQL, gRPC 기술 지원
  

## 미니멀리즘 프레임워크
- Express.js, Gin

> 미니멀리즘 프래임워크는 웹 요청만 처리하며, 약간의 기능만 지원한다. 덕분에 빠른 속도의 API를 사용할 수 있다.

* 자유로운 라이브러리와 아키텍쳐
  - 보안, DB, Messaging, Logging, Caching 등 사용자에게 맞는 형태로 커스터마이징이 가능하다.

* 단점이 존재한다.
  - 협업시에 각기 다른 스타일이 적용될 수 있기 때문에 코딩 컨벤션을 정하는것이 중요하다.
  - 라이브러리들 간 버전관리가 어렵다.
  - 어떤 라이브러리를 업데이트 하게되면, 그 라이브러리와 의존관계에 있는 라이브러리 때문에 코드가 동작하지 않을 수 있다.
    - 라이브러리들 간의 의존관계를 잘 알아봐야한다.

# 동작 방식의 차이 Express & Spring




---

# Reference
- https://appleg1226.tistory.com/33