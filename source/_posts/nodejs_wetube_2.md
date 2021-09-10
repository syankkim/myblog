---
title: Express의 application을 사용
tags: [nodejs, express]
categories: [☁️ NodeJS]
status: 'ing'
thumbnail: ''
permalink: ''
date: 2021-09-10 16:42:47
---

express의 다양한 application을 사용하여 서버와 기본적인 통신을 구현해본다.
`#express` `#request` `#middleware`
<!-- excerpt -->

<!-- toc -->

---

```js
import express from "express";

// *express application생성
const app = express();


// middleware??

// request와 response 중간에 있다.
// request - middleware - response

// 모든 handler는 controller 이며 middleware 이다.
// -> next 변수: 
// const handleEvnt = (req, res, next) => { next(); };
const middlewr = (req, res, next) => {
    console.log("middle here");
    next();
};

// *요청기능
const handleEvnt = (req, res) => {
    // 무언가를 동작
    console.log("and event");
    // request 를 종료해준다.
    // return res.end();

    // text, html 혹은 json으로도 메시지 전달할 수 있다.
    return res.send("<h1>ByeBye</h1>");
};

const handleLogin = (req, res) => {
    return res.send("Login Please");
};

app.get("/", middlewr, handleEvnt);
app.get("/login", handleLogin);

// *외부서버 연결
const PORT = 4001
const handleListening = () =>
    console.log(`✅ Server listening on port http://localhost:${PORT}`);
app.listen(PORT, handleListening);
// callback 함수? 서버가 시작할때 작동하는 함수
// port정보를 줘야함.

// HTTP? 가장 안정적이고 오래된 방식. 서버와 통신하는.
// 브라우저가 대신해서 http request 만들어줌
```

## middleware 생성

> 작업을 다음 함수에게 넘기는 함수.

- 모든 controller는 middleware가 될 수 있고, 모든 middleware는 middleware가 될 수 있다.
- next() 함수를 사용해야, 다음 handler함수가 수행된다.
- middleware는 요청하는 request를 할 수 없다.

* get() 요청 시, middleware 실행

```js
const middlewr = (req, res, next) => {
    console.log("middle here");
    next();
};

const handleEvnt = (req, res) => {
    console.log("handleEvnt here");
    return res.send("<h1>ByeBye</h1>");
};

app.get("/", middlewr, handleEvnt);
```

* 실행결과

```bash
✅ Server listening on port http://localhost:4001
middle here
handleEvnt here
```

