---
title: NodeJS란? 프로젝트 시작.
tags: [nodejs, babel]
categories: [☁️ NodeJS]
status: ''
thumbnail: ''
permalink: ''
date: 2021-09-09 14:42:47
---

빈 파일부터 시작하는 NodeJS 프로젝트 첫 단추 끼우기.
babel로 최신 JavaScript를 사용하자.
`#express` `#nodemon` `#babel`
<!-- excerpt -->

<!-- toc -->

---

# JavaScript is FREE
> 📌 NodeJS?? 브라우저 밖에서 돌아가는 자바스크립트
> `History`
>- 자바스크립트는 브라우저에서만 사용되었다.
>    - 브라우저를 가진 모든 컴퓨터는 자바스크립트가 설치되어 있다.
>    - 창시자인 Ryan이 자바스크립트를 브라우저에 분리하여 NodeJS를 만든것이다.
>- 즉, JS를 다른 프로그래밍 언어처럼 사용할 수 있게 되었다.
>    - 예를 들면, console.log() 를 브라우저에서만 확인할 수 있었지만, nodeJS 를 설치했다면 터미널에서도 console.log() 가능!!

# NPM
> NodeJS Package Manager

- nodeJS와 같이 설치된다.
- 누군가 이미 만들어 놓은 패키지를 가져다 쓰고, 개발을 쉽게 할 수 있다.
    - 그 중 하나가 express이다. 오래된만큼 안정적인 패키지이다.
    - `npm i express`

# NodeJS 프로젝트 생성

기본적이 프로젝트를 진행하기 위해서 아래와 같은 순서로 환경을 구축한다.
1. 프로젝트 디렉토리 생성
2. git repository와 연동
3. express 설치
4. babel 설치, 관련 패키지 설치

## 프로젝트 디렉토리 생성
- 프로젝트를 시작할 빈 디렉토리에서 `npm init` 이 명령어 한 줄이면 쉽게 생성 가능하다.
- 아래와 같은 프로세스대로 질문이 뜨고 질문에 답하면 package.json 파일이 생성된다.

```bash
(base) ➜  wetube git:(master) npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (wetube) 
version: (1.0.0) 
description: The best way to watch videos.
entry point: (index.js) 
test command: 
git repository: (https://github.com/ksso730/wetube-prj.git) 
keywords: 
author: Suyn
license: (ISC) 
About to write to /Users/mac/Documents/wetube/package.json:

{
  "name": "wetube",
  "version": "1.0.0",
  "description": "The best way to watch videos.",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/ksso730/wetube-prj.git"
  },
  "author": "Suyn",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/ksso730/wetube-prj/issues"
  },
  "homepage": "https://github.com/ksso730/wetube-prj#readme"
}

Is this OK? (yes) yes
```

## package.json
```json
{
  "name": "wetube",
  "version": "1.0.0",
  "description": "The best way to watch videos.",
  "main": "index.js",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/ksso730/wetube-prj.git"
  },
   "scripts":{
    "win": "node index.js"
  },
  "author": "Suyn",
  "license": "ISC",
  "bugs": {
    "url": "https://github.com/ksso730/wetube-prj/issues"
  },
  "homepage": "https://github.com/ksso730/wetube-prj#readme"
}
```
- `main` 은 다른 사람들이 우리가 만들고 배포한 패키지를 설치하면 main을 사용할 수 있다.
    - 프로젝트에서 필요 없다면 지워준다.
- `script` 에 사용할 명령어를 정의하고 아래와 같이 사용할 수 있다.

```bash
(base) ➜  wetube git:(master) ✗ npm run win

> wetube@1.0.0 win /Users/mac/Documents/wetube
> node index.js

hello node
```

## Express 설치

```bash
(base) ➜  wetube git:(master) ✗ npm i express
npm notice created a lockfile as package-lock.json. You should commit this file.
+ express@4.17.1
added 50 packages from 37 contributors and audited 50 packages in 2.245s
```
- __package-lock__
    - 패키지를 안전하게 관리해주며, 수정여부를 해시값으로 체크해준다. 
- __node_modules__
    - npm으로 설치한 모든 패키지가 저장된다.
- __package.json__ 에 dependencies가 추가 된다.
    - 이렇게 dependencies에 추가된 패키지들은 node_modules폴더가 삭제되더라도 `npm install` 만 실행해주면 다시 생성된다.

```json
"dependencies": {
    "express": "^4.17.1"
  }
```

## Babel 설치, 관련 패키지 설치

> 📌 Babel is JavaScript compiler

- 아직 nodeJS가 이해하지 못하는 코드가 있다. babel은 우리가 작성한 최신 자바스크립트를 컴파일 해준다. 최신 문법으로 작성하기 위해 `개발자용`으로 설치한다.

```bash
npm install --save-dev @babel/core
```
<br>

* package.json

```json
  "devDependencies": {
    "@babel/core": "^7.15.5"
  }
```

>__dependencies__ : 프로젝트를 실행하기 위해 필요한 것.
__devDependencies__ : 개발자를 위해 필요한 것.


### Babel연동 (babel.config.json 생성)

- preset-env 를 사용한다.
- preset: babel을 위한 거대한 __플러그인__
    - "preset-env" is a smart preset that allows you to use the latest JavaScript without needing to~"

* babel.config.json에 아래와 같이 추가해준다.

```json
{
    "presets":["@babel/preset-env"]
}
```

* babel을 사용하기 위해 다음 패키지 설치
`npm i @babel/preset-env --save-dev`
`npm i @babel/node --save-dev`

```json
 "devDependencies": {
    "@babel/core": "^7.15.5",
    "@babel/node": "^7.15.4",
    "@babel/preset-env": "^7.15.4"
  }
  ```

### Babel의 nodemon

> 📌 파일 수정을 감시해주는 패키지로, 파일이 수정되면 nodemon이 자동으로 재실행해준다.
(관련 패키지는 @babel/node")

* `npm run dev` 수행을 위한 명령

```
 "scripts": {
    "dev": "nodemon --exec babel-node index.js"
  }
```

* 아래처럼 메시지를 바꿔서 저장할때마다 새로 수행된다.

```bash
> nodemon --exec babel-node index.js

[nodemon] 2.0.12
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node index.js`
hi!
[nodemon] clean exit - waiting for changes before restart
[nodemon] restarting due to changes...
[nodemon] starting `babel-node index.js`
how are you?
[nodemon] clean exit - waiting for changes before restart
[nodemon] restarting due to changes...
[nodemon] starting `babel-node index.js`
I'm good!
[nodemon] clean exit - waiting for changes before restart

```

