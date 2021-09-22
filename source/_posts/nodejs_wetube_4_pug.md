---
title: NodeJS with Pug 🐶
tags: ['nodejs', 'pug']
categories: [☁️ NodeJS]
thumbnail: ''
permalink: ''
status: ''
date: 2021-09-20 21:54:11
---

PUG 템플릿 엔진을 이용해, html을 작성하고,
express 활용한 데이터 수정까지.
`#pug` `#urlencoded`
<!-- excerpt -->
<!-- toc -->

---


# PUG 란?

__Templete Engine: PUG__
- 기본적으로 현재 작업 디렉토리(cwd) 에서 `/views` 디렉토리를 찾는다.

__현재 작업 디렉토리(cwd)?__
- 노드를 시작하는 디렉토리. 현재의 경우에는 `/wetube`
- `process.cwd()` : 현재 작업 디렉토리를 찾고, express가 pug의 views 디렉토리를 찾도록 해준다.
* 아래와 같이 src 하위의 views 디렉토리를 찾도록 세팅.

```js
app.set("view engine", "pug");
app.set("views", process.cwd() + "/src/views");
```


## Partials

HTML의 head나 header 또는 footer는 분리된 .pug파일로 함수화 할 수 있다.
partials 디렉토리 하위에 공통적으로 사용할 element를 정의하고, `include`하여 사용한다.

* footer.pug를 공통적으로 사용할 포맷으로 만들고.

```pug
footer &copy; #{new Date().getFullYear()} PugTemplete.
```

* layout.pug 에 아래와 같이 include 하여 사용한다. footer.pug에 정의된 내용이 그대로 적용되는걸 볼 수 있다.

```pug
doctype html
html(lang="ko")
    head
        title PugTemplete
    body
        header
            h1 Welcome !
    include partials/footer.pug
```



## form 사용 GET/POST: title 수정하기

* edit.pug
    - `GET`: form의 default method
    - `POST`: database를 바꾸거나 file을 바꿀때, 로그인할 때 사용한다.

```pug
extends base.pug

block content
    h4 Change Title of video
    form(action="save-chages")
        input(name="title", placeholder="Video Title", value=video.title)
        input(value="Save", type="submit")
```

위와 같은 코드에서 Save를 클릭하면, url은 `/videos/1/save-chages?title=First+Video` 이렇다. 즉 GET으로 데이터를 가져온다.

POST 방식을 사용하기 위해서, router에 post method를 추가한다.

* videoRouter.js : get 하위에 추가된 post

```js
videoRouter.get("/:id(\\d+)/edit", getEdit);
videoRouter.post("/:id(\\d+)/edit", postEdit);
```

* 위 코드의 get/post 는 `route`로 대체할 수 있다.

```pug
videoRouter.route("/:id(\\d+)/editz").get(getEdit).post(postEdit);
```

<br>

* videoController.js
    - postEdit: Save 수행시, 해당 비디오페이지로 이동 `redirect`
    - 동적 객체인 `videos` 를 정의해 두었다.

```js
export const getEdit = (req, res) => {
    const {id} = req.params;
    const video = videos[id-1];
    return res.render("edit", {pageTitle: `Editing: ${video.title}`, video});
};
export const postEdit = (req, res) => {
    const {id} = req.params;
    console.log(req.body);
    return res.redirect(`/videos/${id}`);
};

let videos = [
    {
        title: "First Video",
        rating: 5,
        comment: 2,
        createdAt: "2 minutes ago",
        views: 14,
        id: 1,
    },
    {
        title: "Second Video",
        rating: 5,
        comment: 21,
        createdAt: "21 minutes ago",
        views: 10,
        id: 2,
    },
    {
        title: "Third Video",
        rating: 52,
        comment: 44,
        createdAt: "52 minutes ago",
        views: 11,
        id: 3,
    },
];
```

postEdit 함수에서 찍은 console log의 결과는 `undefined` 이다. form의 데이터를 받지 못하고 있는것.

### express.urlencoded()

그래서, HTML form의 value들을 이해하여 javascript object 형식으로 데이터를 받기위해 express의 `urlencoded` 를 사용한다.

* server.js: router들의 상위에 middleware로서 등록.

```js
app.use(express.urlencoded({extended: true}));
app.use("/", globalRouter);
app.use("/users", userRouter);
app.use("/videos", videoRouter);
```
<br>

* title을 수정하면 아래와 같이 console.log에 남는다. 우리가 input의 name을 title이라고 지었기 때문에. 모든 input에는 name을 넣어주는것이 좋다.

<img width="999" alt="스크린샷 2021-09-22 오후 9 48 34" src="https://user-images.githubusercontent.com/28856435/134346430-c34e421e-de90-4761-8ea8-b55667b873d9.png">

<br>

* console

```bash
{ title: 'Edit this video' }
```

<br>

즉 title객체를 이용하여, postEdit 함수에서 title을 원래의 값과 바꿔줄 수 있다는 말이다.

* videoController.js

```js
export const postEdit = (req, res) => {
    const {id} = req.params;
    const {title} = req.body;
    videos[id-1].title = title;
    return res.redirect(`/videos/${id}`);
};
```

<br>

---

<br>

그 결과, 아래처럼 Secode Video -> Edit this video 로 데이터가 수정되어 반영된것을 확인할 수 있다.

<br>

<img width="1001" alt="스크린샷 2021-09-22 오후 9 50 10" src="https://user-images.githubusercontent.com/28856435/134346790-c088f49f-297a-49cb-bc7d-56a9b59ee164.png">

<br>

<img width="979" alt="스크린샷 2021-09-22 오후 9 50 38" src="https://user-images.githubusercontent.com/28856435/134346979-942a399d-7f3e-4608-8615-ffadba2456e0.png">
