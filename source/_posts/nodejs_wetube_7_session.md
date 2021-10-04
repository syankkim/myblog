---
title: 🍪 NodeJS session/cookie & session store
tags: ['nodejs']
categories: [☁️ NodeJS]
thumbnail: ''
permalink: ''
status: ''
date: 2021-10-04 23:08:20
---

session을 저장하여 로그인하고 sessionStore db 에서 세션을 유지해본다.
`#session` `#cookie` `#locals`
<!-- excerpt -->
<!-- toc -->

---

# Session

> express-session 모듈로부터 브라우저가 백엔드와 상호작용할 때마다 session이 브라우저에 cookie를 전달. backend가 브라우저에 주는 정보.

- 정해진 규칙이 있어서 클라이언트가 request를 보낼때마다 브라우저에서는 cookie정보를 자동으로 추가하여 요청한다.
- 같은 컴퓨터에서도 브라우저마다 다른 session 값을 보인다.
- http?
    - `statless`: 클라이언트의 상태정보를 알 수 없음
    -`connectionless`: 브라우저와 bacckend의 connection이 영원하지 않음.
- 브라우저는 session ID가 포함된 `cookie` 를 가지고 있다.

![image](https://user-images.githubusercontent.com/28856435/135840108-6e7ef3a1-5a30-4cfc-a30a-c925e75c7fa9.png)

<br>

* session 미들웨어가 서버에 text를 보내는 방법.

```
app.use(
    session({
        secret: "Hello",
        resave: true,
        saveUninitialized: true,
    })
);
```

<br>

* server.js 에서 session을 직접 찍어 확인할 수 있다. 우리가 backend에 요청을 보낼 때마다, 즉 새로고침 할 때마다 확인된다.

```js
app.use((req, res, next) => {
    req.sessionStore.all((error, sessions) => {
        console.log(sessions);
        next();
    });
});
```

![image](https://user-images.githubusercontent.com/28856435/135844113-889988f1-1283-449e-8d6e-199defbfbf73.png)


<br>

## 로그인시, 세션정보에 User data 저장

```js
req.session.loggedIn = true;
req.session.user = user
```

* session object에서 user data가 찍히는것이 확인된다.

```bash
GET /login 200 35.257 ms - 763
[Object: null prototype] {
  _xkMIOUyQfOyn1GqOlhzvoq4AdDT6ry_: {
    cookie: { originalMaxAge: null, expires: null, httpOnly: true, path: '/' }     
  },
  '5lLSTQT-erP7IHsdz2BEtyab7daD7Yhr': {
    cookie: { originalMaxAge: null, expires: null, httpOnly: true, path: '/' }     
  }
}
{
  _id: new ObjectId("6156c286d0c358cec3b67416"),
  email: 'suyans730@naver.com ',
  username: 'sy',
  password: '$2b$05$0AKL1qtzW9MZPPVbYxjiTO7wYZ3I.hxHptUlf2jFq0CS95KMj7QDa',        
  name: 'Suyeon Kim',
  __v: 0
}
```

<br>

* full code of postLogin function 

```js
export const postLogin = async(req, res) => {
    const { username, password } = req.body;
    const user = await User.findOne({ username });
    if (!user) {
       //...
    };

    req.session.loggedIn = true;
    // session에 정보 추가
    console.log(user);
    req.session.user = user;

    return res.redirect("/");
};
```

## req.locals

> response객체의 locals를 middleware로 등록해두면, .pug 템플릿 어느곳에서든 저장해두었던 데이터를 가져올 수 있다.

```js
export const localsMiddleware = (req, res, next) => {
    res.locals.loggedIn = Boolean(req.session.loggedIn);
    res.locals.loggedInUser = req.session.user;
    next();
}
```

# Session Store

> Note: Session data is not saved in the cookie itself, just the session ID. Session data is stored server-side.
session ID 외의 세션 데이터는 쿠키에 저장되지 않고, 서버에 저장된다.
서버에 저장된 session object를 사용하기 위해서는 session store을 사용해야한다.

* npm 에서는 Mongostore를 제공한다. `npm i connect-mongo`

```js
import MongoStore from "connect-mongo";
```

* session db 생성 확인

```mongo
> show dbs
admin    0.000GB
config   0.000GB
local    0.000GB
wemovie  0.000GB
wetube   0.000GB
> show collections
sessions
users
videos
```

<br>

* 로그인 후 sessions collection을 조회하면 데이터가 생성되어 있다.
🙌🏼 이제 여러분의 서버를 재시작해도 로그인 세션이 끊어지지 않을것이다.

```mongo
> db.sessions.find({})
{ "_id" : "1PLHaUy_PkAjVQXNAIBUezbJscN0Awnu", "expires" : ISODate("2021-10-18T11:27:43.731Z"), "session" : "
{\"cookie\":{\"originalMaxAge\":null,\"expires\":null,\"httpOnly\":true,\"path\":\"/\"},\"loggedIn\":true,\"user\":
{\"_id\":\"6155d2a24d9be1fa548b0c8b\",\"email\":\"suyans730@naver.com \",\"username\":\"sy\",
\"password\":\"$2b$05$E5D4iGIDc6OQov19Zs9uVuLas0jlmGOhSbyWfcHICEjTaf6fKM/A.\",\"name\":\"Suyeon Kim\",\"__v\":0}}" }
```


## Properties of Cookie

- secret: cookie에 sign 할 때 사요하는 string. 안전을 위해서 길고 복잡하고 랜덤한 string을 사용하는것이 좋음.
- domain: 브라우저는 도메인에 따라 cookie를 저장한다.
- expires: 세션 만료날짜. maxAge 를 추가해서 사용.

```js
  cookie: {
      maxAge: 20000
  },
```
<br>

- saveUninitialize

> 세션이 새로 적용되고 만들어진때 수정된적이 없을 때 saveUninitialize.
세션을 수정할 때만 DB를 저장하고 쿠키를 넘겨준다. 즉, 로그인한 사용자에게만 쿠키를 주도록 설정..

브라우저에 접속할 때마다 쿠키를 가져왔다면, 이제는 로그인할 때만 적용이 된다.

* resave, saveUninitialized 옵션을 `false`로 바꿔준다.

```js
app.use(
    session({
        secret: "Hello",
        resave: false,
        saveUninitialized: false,
        store: MongoStore.create({mongoUrl: "mongodb://127.0.0.1:27017/wetube"})
    })
);
```