---
title: NodeJS with Pug 🐶
tags: ['nodejs', 'pug']
categories: [☁️ NodeJS]
thumbnail: ''
permalink: ''
status: ''
date: 2021-09-20 21:54:11
---

`#pug`
<!-- excerpt -->
<!-- toc -->

---


# PUG 란?

__뷰 엔진으로 pug 사용__
- 기본적으로 현재 작업 디렉토리(cwd) 에서 `/views` 디렉토리를 찾는다.

__현재 작업 디렉토리(cwd)?__
- 노드를 시작하는 디렉토리. 현재의 경우에는 `/wetube`
- `process.cwd()` : 현재 작업 디렉토리를 찾고, express가 pug의 views 디렉토리를 찾도록 해준다.
* 아래와 같이 src 하위의 views 디렉토리를 찾도록 세팅.

```js
app.set("view engine", "pug");
app.set("views", process.cwd() + "/src/views");
```


### partials