---
title: NodeJS - middleware (feat.morgan)
tags: [nodejs, express]
categories: [☁️ NodeJS]
status: ''
thumbnail: ''
permalink: ''
date: 2021-09-10 16:42:47
---

express의 다양한 application을 사용한 서버와 통신, middleware
`#express` `#request` `#middleware` `#next()` `#morgan`
<!-- excerpt -->

<!-- toc -->

---

# middleware ?

> 작업을 다음 함수에게 넘기는 함수.
const handleEvnt = (req, res, next) => { next(); };

- 모든 controller는 middleware가 될 수 있고, 모든 middleware는 middleware가 될 수 있다.
- 연결이 중단되면 middleware가 아니다.
- `next()` 함수를 사용하면 다음 get method 가 작동된다.
- 어떤 조건에 따라 `send() 혹은 next()` 를 호출 할 수 있다.
- `app.use()` 를 사용한다.

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

## 모든 route에 적용

> middleware 를 가장 상위에 두면 어떤 url을 접속해도 선행된다.

* request method 와 url을 찍는 logger 라는 middleware 를 생성

```js
// logger middleware
const logger = (req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
};

// middleware
app.use(logger)
// Home
app.get("/", handleEvnt);
```

<br>

* 실행결과

<img width="712" alt="스크린샷 2021-09-12 오후 7 17 09" src="https://user-images.githubusercontent.com/28856435/132984228-4a8fb556-e06c-45a9-adce-9f4ef3fa394e.png">

<br>
<br>

* root가 아닌 다른 페이지를 호출해도, middleware가 수행됨을 확인

<img width="698" alt="스크린샷 2021-09-12 오후 7 08 31" src="https://user-images.githubusercontent.com/28856435/132984190-b76d253f-ecf2-4d7a-9278-02bb40a3a67e.png">


## 특정 url을 확인하는 middleware

> 어떤 조건에 따라 send() 혹은 next() 를 호출 할 수 있다.

* url이 `/protected` 라면, 허용하지 않는다는 메시지를 `send` 한다.

```js
import express from "express";
const app = express();

// logger middleware
const logger = (req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
};

// private middleware
const privateMiddlewr = (req, res, next) => {
    const url = req.url;
    if(url==="/protected"){
        return res.send("<h1>Not Allowed</h1>")
    }
    console.log("allowed, you may continue.");
    next();
};

const handleEvnt = (req, res) => {
    console.log("handleEvnt here");
    return res.send("<h1>Home</h1>");
};

const handleProtected = (req, res) => {
    return res.send("This site is private.")
};

// app.use 에 넣은 middleware는 get 요청 이전에 수행된다.
app.use(logger)
app.use(privateMiddlewr);
app.get("/", handleEvnt);
app.get("/protected", handleProtected);

```

<br>

<img width="702" alt="스크린샷 2021-09-12 오후 7 18 27" src="https://user-images.githubusercontent.com/28856435/132984243-2d717221-025c-4f98-a043-65cb2029fb85.png">

<br>

# morgan

> node.js용 request logger middleware 이다.
설치하고 사용해보자. `npm i morgan`

* 이전 코드에 logger로 만들었던 middleware 대신에 `margan` 을 사용한 logger를 추가해준다.

```js
import margan from "morgan";

const logger = morgan("dev");
app.use(logger);
```
<br>

* morgan 은 GET, path, status code 모든 정보를 가지고 있다.

```bash
✅ Server listening on port http://localhost:4001
allowed, you may continue.
handleEvnt here
GET / 200 4.390 ms - 13
allowed, you may continue.
GET /favicon.ico 404 2.161 ms - 150
GET /protected 304 0.395 ms - -
```