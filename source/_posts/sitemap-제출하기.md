---
title: Google search console, sitemap
tags: Git
categories: []
thumbnail: ''
permalink: ''
date: 2020-02-17 22:54:49
---

hexo 플러그인을 이용해 Google search console 에 github 블로그 소유권을 인증하고 xml 을 등록해봅니다.
<!-- excerpt -->
<!-- toc -->

### Google search console 등록

[Google search console](https://search.google.com/search-console/welcome?hl=ko) 에 접속하여 일반적인 github.blog.io 를 사용하고 있다면 다음 창에 주소를 써 넣어준다.

![image](https://user-images.githubusercontent.com/28856435/74661554-863c2e00-51db-11ea-97a6-eb2365f5d594.png)


아래과 같이 타 도메인이 아닌 깃헙 블로그는 쉽게 인증이 가능하다.

![image](https://user-images.githubusercontent.com/28856435/74668917-893e1b00-51e9-11ea-8b6a-8f83dbcb6bdb.png)
<br/>

### sitemap.xml 등록하기

필자는 `hexo` 를 사용중이기에 hexo 플러그인을 사용해 sitemap 을 생성해주도록 설정했다.

아래 명령을 실행해 플러그인을 설치한다.
```bash
$ npm install hexo-generator-seo-friendly-sitemap --save
```
root 위치의 _config.yml 에 아래와 같이 sitemap 이 생성될 경로와 이름을 추가해준다.

```yml
sitemap:
    path: sitemap.xml
```

![image](https://user-images.githubusercontent.com/28856435/74670458-8d1f6c80-51ec-11ea-8e7b-c851a0f7694a.png)

