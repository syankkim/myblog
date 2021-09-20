---
title: NodeJS - Router
tags: [nodejs, express]
categories: [☁️ NodeJS]
status: ''
thumbnail: ''
permalink: ''
date: 2021-09-15 22:23:47
---

express의  Router를 사용하여 모듈화 하기.
`#express` `#reouter` `#controller`
<!-- excerpt -->

<!-- toc -->

---

# Routers ?

> url을 공통 모듈로 그룹화 하여 명시할 수 있다.


## Router 생성 & 사용

* 각 Router는 그 하위의 get 요청으로 불리는 url을 포함하는 그룹 역할을 하는것을 볼 수 있다.

```js
// Router 생성
const globalRouter = express.Router();
const userRouter = express.Router();
const videoRouter = express.Router();

// Router 사용

// url : "/"
app.use("/", globalRouter);
const handleHome = (req, res) => res.send("Home");
globalRouter.get("/", handleHome);

// url : "/users/edit"
app.use("/users", userRouter);
const handleEditUser = (req, res) => res.send("Edit User");
userRouter.get("/edit", handleEditUser);

// url : "/videos/watch"
app.use("/videos", videoRouter);
const handleWatchVideo = (req, res) => res.send("Watch Video");
videoRouter.get("/watch", handleWatchVideo);
```

## 정리된 Router 모듈

1. 위에서 생성했던 3개의 Router를 독립적인 모듈로 분리해준다.
2. `export` 를 이용해, 다른 모듈에서 `import` 가능하다.

* router 폴더 내에 각 Router 모듈 생성

<img width="253" alt="스크린샷 2021-09-16 오전 12 10 49" src="https://user-images.githubusercontent.com/28856435/133460281-299b2201-1e24-4c5d-abfe-79d81820ba04.png">

<br>

* 아래와 같이 각 router를 `export`

```js
import express from "express";
const userRouter = express.Router();
export default userRouter;
```

* server.js 에서 각 router 를 `import`

```js
import globalRouter from "./routers/globalRouter";
import videoRouter from "./routers/videoRouter";
import userRouter from "./routers/userRouter";

app.use("/", globalRouter);
app.use("/users", userRouter);
app.use("/videos", videoRouter);
```


## Controller와 Router 변수 사용

- handleHome, handleEditUser, handleWatchVideo 등의 handler 메서드는 controller 모듈로 분리한다.
- url로부터 전달받은 파라미터는 router에서 controller의 `req` 객체로 전달되어 `res` 객체에서 확인 가능하다.

<br>

* UserRouter.js

```js
import express from "express";
import {see} from "../contorllers/userController";

// http://localhost:4001/users/5
const userRouter = express.Router();
userRouter.get("/:id", see)

export default userRouter;
```

* UserController.js

```js
export see = (req, res) => {
    res.send(`Hello #${req.params.id}`);
};
```

<br>

* _localhost:4001/users/12_ 요청 결과이다.

<img width="600" alt="스크린샷 2021-09-20 오후 9 48 45" src="https://user-images.githubusercontent.com/28856435/134004924-6aba058e-ec18-47fd-bddf-68a0197a089c.png">

### request 순서
- upload 를 2번째로 내리면, request는 가장 위에서부터 요청을 처리하기 때문에 express는 `upload`가 `id`라고 인식한다.
- 하지만 가장 상단으로 올려주면 정상적으로 작동한다.

```js
videoRouter.get("/upload", upload);
videoRouter.get("/:id", see);
videoRouter.get("/:id/edit", edit);
videoRouter.get("/:id/delete", deleteVideo);
```

### 정규식으로 원하는 변수만

* 정규식을 사용하여 id 에 숫자만 허용할 수 있다.

```js
videoRouter.get("/:id(//d+)", see);
```
