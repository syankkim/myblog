---
title: Servlet 정의와 생명주기, Servlet 컨테이너
tags: ['java','servlet']
categories: [☁️ Java]
thumbnail: ''
permalink: ''
img : <img width="370" alt="servlet-logo" src="https://user-images.githubusercontent.com/28856435/116650882-fab45480-a9bc-11eb-812f-c29c03474b64.png">
date: 2021-04-30 10:26:43
status: 'ing'
---

Servlet 개념 잡기 !
💬 _작성중_
<!-- excerpt -->
<!-- toc -->

---

요즘 당연하게 생각하고 사용해왔던 개념, 기능들을 찾아보며 정리중이다.
Java, RESTful API 개발을 하고 있지만, 내부적으로 어떻게 돌아가는지 개념적인 부분을 다시 한번 짚고자 한다.

### Servlet 이란?
> 서버사이드에서 클라이언트 요청을 처리하고 그 결과를 응답해주는 규칙.

#### Servlet 특징
- 동적 웹페이지를 작성하기 위해 나왔다.
- 서버쪽에서 실행되면서 클라이언트의 요청에 따라 동적으로 일을 처리하는 `자바 클래스` 이다.
- Servlet


### Servlet 컨테이너
> Servlet 클래스로 작성된 프로그램을 실행하고, 관리해준다.

#### Servlet 컨테이너 역할
- 웹서버와의 통신을 지원해준다. 서블릿 컨테이너는 소켓을 만들고  listen, accept 등의 기능을 api 로 제공하여 개발자가 비지니스 로직에만 집중할 수 있도록 해준다.
- 서블릿의 생명주기를 관리한다. 실행부터 종료까지. 

### Servlet 작동흐름
> 1. 클라이언트가 HTTP Request 를 Servlet Container 로 전송.
2. Servlet Container 는 HttpServletRequest, HttpServletResponse 두 객체 생성
3. 

### Servlet 생명주기
