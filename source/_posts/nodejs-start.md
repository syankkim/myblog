---
title: Node JS 기본, 시작해보기
tags: ['nodejs']
categories: [☁️ NodeJS]
thumbnail: ''
permalink: ''
status: ''
date: 2021-07-04 17:51:11
---

parcel bundler를 이용하여 웹에 index.html을 띄워본다.
버전관리, package.json 등의 의미
`#nvm` `#npm` `#parcel`
<!-- excerpt -->
<!-- toc -->

# 💡 NodeJS 시작하기

## 시작하기

* 다음 설치환경이 선행되어 있음
    - nvm 버전관리 모듈 설치
    - npm 12.14.1 버전 사용


* 프로젝트 폴더에서 npm 초기화

```ssh
> npm init y
```

* 아래 npm 모듈을 설치해본다.

```ssh
> npm install parcel-bundler -D
> npm install lodash
```

>📌  Parcel?
>- `꾸러미` 라는 뜻을 가졌다. 짐을 싸듯이 객체를 싸는 클래스이다.
>- 쉽고 빠른 웹/앱 bundler.
    (bundler: 여라 파일들을 하나의 파일로 묶어주어 네트워크의 응답속도를 빠르게 도와주고 파일 간의 병목현상을 줄여, 유지보수의 효율성 증가)
>- Parcel 은 파일 변화를 자동으로 감지하여 다시 빌드하고, 빠른 모듈 교체를 지원하는 내장 개발용 서버를 보유하고 있어, 신속한 개발을 가능하게 한다.


>📌  lodash?
>- 유틸리티 라이브러리로 array, collection, date, number, object등이 있으며, 데이터를 쉽게 다룰 수 있도록 도와준다.
>- 특히 자바스크립트 배열 내부의 객체들을 핸들링할 때 유용하다.
>- 자주 사용하는 기능 : `filter`, `map`, `uniqBy` etc...

## package.json ?

* package.json : 패키지 모듈 직접 관리
* package-lock.json : 인스톨한 패키지들을 내부에서 자동으로 관리

## 옵션 -D, --save-dev

* 옵션 -D, --save-dev : `devDependencies` 에 설치됨
    - 개발할 때만 필요. 웹브라우저에서는 직접적으로 동작하지 않는다.


## 브라우저에서 index.html 띄우기

* dev: index.html 을 기준으로 `개발용`으로만 활용
* build: index.html 을 기준으로 `웹브라우저`에서 동작시키는 용도

```json
 "scripts": {
    "dev": "parcel index.html",
    "build": "parcel build index.html"
  },
```

* 터미널에서 명령어 사용, localhost:1234 접속

```ssh
> npm run dev
```

## lodash 모듈 사용

* 아래 코드를 입력하고

```js
import _ from 'lodash';

console.log('hellow');
// lodash 모듈을 사용
console.log(_.camelCase('hello suyeon'));
```
*  `npm run dev` 실행후 브라우저에서 접속하면 console에서 아래와 같이 적용된다.
![node1](https://user-images.githubusercontent.com/28856435/124388083-14a34800-dd1c-11eb-8d2a-2e04b337845e.PNG)

</br>

---

# 💡 유의적 버전 (Semantic Versioning) ;버전규칙

* ^Major.Minor.Patch
    - ^ : Major 버전 안에서 가장 최신 버전으로 업데이트 가능
        - 해당 기호를 지우면 `npm update` 사용하여 업데이트 불가하다
    - Major : 기존 버전과 호환되지 않는 새로운 버전
    - Minor : 기존 버전과 호환되는 새로운 기능이 추가된 버전
    - Patch : 기존 버전과 호환되는 버그 및 오타 등이 수정된 버전

* 버전 정보 확인

```ssh
npm info lodash
```

## 버전을 낮춰서 설치하기

```ssh
npm install lodash@4.17.20
```
---

# 💡 프로젝트 버전 관리 NPM


## 패키지 재설치 (package.json)

* node_mudule 폴더를 지우더라도 `npm -i` 를 통해서 다시 설치 가능 (.cache, dist도 마찬가지)

## .gitignore 생성하여 버전관리 제외

* 버전관리가 불필요한 파일들을 .gitignore 에 추가하여 제외할 수 있다.

```ssh
.cache/
dist
node_modules/
```

* `git status` 명령어로 확인, `.gitignore` 에 추가한 파일은 올라가지 않는다.

![nod2](https://user-images.githubusercontent.com/28856435/124389250-4834a100-dd21-11eb-8a41-c59cb9e7c3d2.PNG)

