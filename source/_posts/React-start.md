---
title: React 입문해보자
tags: ['react','node']
categories: [☁️ React]
thumbnail: ''
permalink: ''
img : <img width="100" alt="react-logo" src="https://user-images.githubusercontent.com/28856435/83209013-2c5fe280-a192-11ea-947e-18055da3d97e.png">
date: 2020-05-24 22:21:00
---

React 의 기본개념과 생명주기에 대해 알아봅니다.
<!-- excerpt -->
<!-- toc -->

---

## React ?

>**VirtualDom**
: 리액트가 관리하는 가상 DOM. (브라우저의 DOM과 별도)
- 페이지 내 내용이 변경되면 VirtualDom 은 차이가 있는 부분을 확인한다.
- 자체적으로 변경된 부분만 찾아서 Reflow(재렌더링) 한다.

>**JSX** (JavaScript+XML)
: 자바스크립트를 확장한 프로그래밍 언어.

__장점?__

1) Component 를 사용하여 속도가 빠르다.
2) react-dom 이라는 가상돔에서 만든다.

__단점?__

1) 단방향, 데이터를 바꿀 때 전체(최상위)를 바꿔야 함. -개선된것 Redux
2) function 기반은 전역변수 사용이 어렵다. -개선 Hooks (속성으로 넘기기힘듦 - UserState: state를 자유자재로 쓸수있음)


## 설치

리액트를 사용하기위해 아래 순서대로 설치를 진행해준다.


**1. Node.js 설치**

**2. React 설치**

```bash
C:\Users\sist27>npm install -g create-react-app
```

**3. WebStorm 설치 (편집기)**



---


## React 프로젝트 생성/실행 with WebStorm

<br>

1. New Project 생성 후 (왼쪽 사이드바에 React App 선택)
![image](https://user-images.githubusercontent.com/28856435/81461652-340e1600-91e8-11ea-838f-fc8db1b4fd87.png)

2. App.js 에서 약간의 수정이후 터미널에서 `npm start` 를 실행한다.
![image (1)](https://user-images.githubusercontent.com/28856435/81461659-45572280-91e8-11ea-9fda-e3a41631929e.png)

3. package.json 의 dependencies 에 axios 버전을 추가해준다.

```bash

"axios": "^0.19.2"

```


## Component 기본 형식 [class 기반, function 기반]

>class 기반 : 생명주기가 있음

```javascript
    class App extends Component
    {
        constructor(){}
        // 화면에 불러오기 전 (데이터 받기전)
        componentWillMount()
        // 화면 출력을 읽는 데이터 (데이터 받음)
        render(){}
        // 화면을 출력 (onLoad() 와 비슷)
        componentDidMount()
        //javaScript onLoad() 방식은 아래와 같음.
        componentDidMount() => $(function(){})
            $(document).ready(function(){})
            window.onload=function(){}
    }
```

>function : 생명주기가 없음 -> Data를 넘겨주는 방식 -> 그런데 어려움 -> Hooks 사용

```javascript
    function App()
    {
        return{
            <html>
            </html>
        )
    }
```

## JSX 형식

1. 반드시 계층구조를 만든다.

```html
<div>Hello</div>
<div>React</div>
//- Error
```
```html
/* 계층구조로 아래와 같이 */
<div>
  	<div>Hello</div>
	<div>React</div>
</div>
```
2. HTML 태그는 반드시 소문자
```html
<Html> => //- Error
```
3. 속성은 반드시 ""
```html
<table width="100">
```
```html
<table width=100> //- Error
```