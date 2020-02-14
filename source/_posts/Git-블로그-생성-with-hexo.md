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
<br/>
<br/>

### Github repository 생성부터 hexo 로컬서버로 올리기까지.
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
<br/>

***

### Git blog 에 hexo theme 적용 
#### grunt 란?
###### Github 에서 말하는 Grunt
> _"Grunt is a task-based command line build tool for JavaScript projects."_
grunt 는 JavaScript Task Runner, JavaScript 자동화 툴이다.
<br/>

###### Grunt 사용
grunt 사용은 npm 을 통해 이루어진다. Node.js 가 설치되었다는 전제에 grunt를 설치한다.
설치는 프로젝트의 root 경로에서 진행한다.

**grunt-cli**
  설치 (grunt Command Line Interface)
**--save-dev**
  이 옵션은 package.json 파일과 연동시켜주며 파일 내부 "devDependencies" 항목에 설치대상을 자동으로 추가해준다. 아래 이미지를 보면 "grunt" 가 추가된것을 확인할 수 있다.

```bash
$ npm install -g grunt-cli 
$ npm install grunt --save-dev
```
<img width="422" alt="grunt_in_package" src="https://user-images.githubusercontent.com/28856435/74511722-f6338580-4f49-11ea-9e82-498be49d8174.png">
<br/>

#### hexo 배포

```bash
$ hexo clean
$ hexo g
$ hexo d // 또는 $ hexo g -d : generate 와 deploy 를 한번에 수행.
```

#### hexo 테마설정

###### theme & git repository 연동 (_config.yml)

`myblog/_config.yml` 파일에 theme 항목이 있다. 적용하고자 하는 테마를 이곳에 넣어준다.

<img width="263" alt="theme_in_config" src="https://user-images.githubusercontent.com/28856435/74512784-5d523980-4f4c-11ea-9c76-0f8204fe3be5.png">
<br/>

다시 `hexo s` 를 실행하여 localhost 에서 확인을 해보면 테마가 적용된것을 확인할 수 있다.