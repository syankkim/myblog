---
title: NodeJS - router
tags: [nodejs, express]
categories: [☁️ NodeJS]
status: ''
thumbnail: ''
permalink: ''
date: 2021-09-15 22:23:47
---

express의  routers
`#express` `#reouter`
<!-- excerpt -->

<!-- toc -->

---

# Routers ?

> url을 그룹화 하여 명시할 수 있다.

video 라는 Router를 찾으면 /video/watch 

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