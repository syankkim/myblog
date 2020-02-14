---
title: Git 블로그 생성 with hexo
date: 2020-01-18 01:19:04
tags: hexo
categories: []
thumbnail: ""
permalink: ""
---

Hexo 를 이용해 Git Blog 를 생성합니다.
연동 전 기본 setting 부터 git repo 연동과 배포까지.
<!-- excerpt -->

작년에 `jekill` 로 git 블로그 생성을 시도하다 실패였고,
네이버 블로그, 티스토리로도 블로그를 시작하려 해봤지만 의지박약으로 실패 ..

내가 공부했던 로그나 일한것들을 올릴 수 있는 나만의 페이지를 갖고싶기도 하였고,
내 github activity 에도 실적을 남길 수 있다는 일석이조의 장점이 동기부여를 심어주지 않을까 하여
`node.js` 가 좀 생소한 언어이지만 공부하는 김에,
블로그 생성과 커스텀에 대한 설명이 좀더 많은 `hexo`를 택하기로 마음 먹었습니다.

시작이 반이라 하였으니,
일단 hexo 로 블로그를 구축하며 겪은 과정들을 포스팅을 하기로 !

***
<!-- toc -->
<!-- 1. github 에  본인 ID.gitgub.io 명으로 repository 를 생성합니다.
2. git 설치 [Git](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98)
3. node.js 설치 [Node.js](https://nodejs.org/ko/download/)
4. node.js 를 이용한 hexo 설치
5. hexo 새 프로젝트 만들기, 시작.
6. 프로젝트 폴더 위치에서 hexo 서버 실행
7. 브라우저에서 서버접속하여 확인 -->

<br/>
<br/>

#### @ID/gibhub.io 로 repository 를 생성
![20190120_01](https://user-images.githubusercontent.com/28856435/72684483-1b3c0080-3b24-11ea-8a3e-cc52ede28df1.jpg)
<br/>

#### git과 node.js 설치 후 확인

git 설치 [Git](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98)
node.js 설치 [Node.js](https://nodejs.org/ko/download/)

``` bash
$ node -v
$ npm -v
```

#### hexo 설치 후 확인

``` bash
$ npm i hexo -cli -g
$ hexo -v
```

#### hexo 새 프로젝트 만들기, 시작

``` bash
C:\Users\Suyeon Kim>node -v
v12.14.1
C:\Users\Suyeon Kim>npm -v
6.13.4
C:\Users\Suyeon Kim>npm i hexo-cli -g
...
+ hexo-cli@3.1.0
added 82 packages from 356 contributors in 7.839s
C:\Users\Suyeon Kim>hexo -v
hexo-cli: 3.1.0
...
C:\Users\Suyeon Kim>hexo init blog
... 
Thank you for installing EJS: built with the Jake JavaScript build tool (https://jakejs.com/)
 found 0 vulnerabilities
INFO  Start blogging with Hexo!
```

<br/>
<br/>

#### 프로젝트 폴더 위치에서 hexo 서버 실행
``` bash
C:\Users\Suyeon Kim>cd blog
 
C:\Users\Suyeon Kim\blog>hexo server
INFO  Start processing
INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
```

<br/>
<br/>

#### 브라우저에서 http://localhost:4000 접속하여 확인

![20200120_03](https://user-images.githubusercontent.com/28856435/72684672-ff395e80-3b25-11ea-9d04-2a25e1759c3c.jpg)

***

#### 다음 포스팅
**git repository - hexo server 연동**
1. hexo 배포
2. hexo 테마설정
3. theme & git repository 연동 (_config.yml)