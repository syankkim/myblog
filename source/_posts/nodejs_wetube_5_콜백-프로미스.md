---
title: JS callback & promise
tags: ['nodejs']
categories:
  - ☁️
thumbnail: ''
permalink: ''
status: ''
date: 2021-09-25 22:08:20
---

mongoose 를 예시로, callback과 promise 함수를 알아본다.
<!-- excerpt -->
<!-- toc -->

---

# callback 함수
> 무언가 발생한 다음 호출되는 function.

javascript에서 해당 함수 수행을 마칠때까지 기다림이 필요함을 말한다.
database같이 javascript파일 내에 없는 데이터이기 때문에 처리 시간을 예측할 수 없다는 뜻이다.

즉, 특정 코드를 가장 마지막에 실행한다.
장점은 에러들을 내부에서 바로 불러올 수 있다는 것.

* callback

```js
export const home = (req, res) => {
    console.log(“Start”);
    Video.find({}, (error, videos) => {
	   console.log(“Finally finished”);
        return res.render("home", {pageTitle: "Home", videos: []});
    });
    console.log(“Finished first”);
}
```

위 코드에서 `find()`는 mongoose가 제공하는 Query이다. 이것은 callback 함수이고, database 검색이 끝난 후에 rendering이 시작된다.
application을 실행해보면, callback함수 내부의 `Finished` 메시지가 가장 마지막으로 찍히는것이 확인된다.

* npm run start

```s
———————————————————————————
Start
I finished first
Finished
GET / 304 146.403 ms - -
———————————————————————————
```

# promise 함수

> async/await
callback 함수의 최신 버전이라고 할 수 있다. (es8)

`await`는 javascript가 작업을 `기다려준다는 의미이다.`
async와 await는 callback과 달리 `직관적`이라는 장점이 있다.
반면에 callback은 callback 함수 내부에서 결과값을 수행하기 때문에, callback 함수 내부의 callback 함수, callback 함수 내부의 callback 함수 .. 이렇게 코드가 깊어져, 가독성이 떨어지게 된다.

* promise

```js
export const home = async(req, res) => {
    const videos = await Video.find({});
    return res.render("home", {pageTitle: "Home", videos: []});
}
```