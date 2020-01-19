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

## List
### 1. 연동 전 기본 setting
1. github 에  본인 ID.gitgub.io 명으로 repository 를 생성합니다.
2. git 설치 [Git](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EC%84%A4%EC%B9%98)
3. node.js 설치 [Node.js](https://nodejs.org/ko/download/)
4. node.js 를 이용한 hexo 설치
5. hexo 새 프로젝트 만들기, 시작.
6. 프로젝트 폴더 위치에서 hexo 서버 실행
7. 브라우저에서 서버접속하여 확인

<br/>
<br/>

#### 1. @ID/gibhub.io 로 repository 를 생성
![20190120_01](https://user-images.githubusercontent.com/28856435/72684483-1b3c0080-3b24-11ea-8a3e-cc52ede28df1.jpg)

#### 2,3. git과 node.js 설치 후 확인

``` bash
$ node -v
$ npm -v
```


#### 4. hexo 설치 후 확인

``` bash
$ npm i hexo -cli -g
$ hexo -v
```

#### 5. hexo 새 프로젝트 만들기, 시작

``` bash
$ hexo init {프로젝트명}
```
<div class="colorscripter-code" style="color:#FFFFFF;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#282525;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:120%"><div style="line-height:120%">1</div><div style="line-height:120%">2</div><div style="line-height:120%">3</div><div style="line-height:120%">4</div><div style="line-height:120%">5</div><div style="line-height:120%">6</div><div style="line-height:120%">7</div><div style="line-height:120%">8</div><div style="line-height:120%">9</div><div style="line-height:120%">10</div><div style="line-height:120%">11</div><div style="line-height:120%">12</div><div style="line-height:120%">13</div><div style="line-height:120%">14</div><div style="line-height:120%">15</div><div style="line-height:120%">16</div><div style="line-height:120%">17</div><div style="line-height:120%">18</div><div style="line-height:120%">19</div><div style="line-height:120%">20</div><div style="line-height:120%">21</div><div style="line-height:120%">22</div><div style="line-height:120%">23</div><div style="line-height:120%">24</div><div style="line-height:120%">25</div><div style="line-height:120%">26</div><div style="line-height:120%">27</div><div style="line-height:120%">28</div><div style="line-height:120%">29</div><div style="line-height:120%">30</div><div style="line-height:120%">31</div><div style="line-height:120%">32</div><div style="line-height:120%">33</div><div style="line-height:120%">34</div><div style="line-height:120%">35</div><div style="line-height:120%">36</div><div style="line-height:120%">37</div><div style="line-height:120%">38</div><div style="line-height:120%">39</div><div style="line-height:120%">40</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FFFFFF;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:120%"><div style="padding:0 6px; white-space:pre; line-height:120%">C:\Users\Suyeon&nbsp;Kim<span style="color:#0086B3"></span><span style="color:#ED7803">&gt;</span>node&nbsp;<span style="color:#0086B3"></span><span style="color:#ED7803">-</span>v</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">v12.<span style="color:#0F9FB9">14.</span><span style="color:#0F9FB9">1</span></div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">C:\Users\Suyeon&nbsp;Kim<span style="color:#0086B3"></span><span style="color:#ED7803">&gt;</span>npm&nbsp;<span style="color:#0086B3"></span><span style="color:#ED7803">-</span>v</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%"><span style="color:#0F9FB9">6.</span><span style="color:#0F9FB9">13.</span><span style="color:#0F9FB9">4</span></div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">C:\Users\Suyeon&nbsp;Kim<span style="color:#0086B3"></span><span style="color:#ED7803">&gt;</span>npm&nbsp;i&nbsp;hexo<span style="color:#0086B3"></span><span style="color:#ED7803">-</span>cli&nbsp;<span style="color:#0086B3"></span><span style="color:#ED7803">-</span>g</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">...</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%"><span style="color:#0086B3"></span><span style="color:#ED7803">+</span>&nbsp;hexo<span style="color:#0086B3"></span><span style="color:#ED7803">-</span>cli@<span style="color:#0F9FB9">3.</span><span style="color:#0F9FB9">1.</span><span style="color:#0F9FB9">0</span></div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">added&nbsp;<span style="color:#0F9FB9">82</span>&nbsp;packages&nbsp;from&nbsp;<span style="color:#0F9FB9">356</span>&nbsp;contributors&nbsp;in&nbsp;<span style="color:#0F9FB9">7.</span>839s</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">C:\Users\Suyeon&nbsp;Kim<span style="color:#0086B3"></span><span style="color:#ED7803">&gt;</span>hexo&nbsp;<span style="color:#0086B3"></span><span style="color:#ED7803">-</span>v</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">hexo<span style="color:#0086B3"></span><span style="color:#ED7803">-</span>cli:&nbsp;<span style="color:#0F9FB9">3.</span><span style="color:#0F9FB9">1.</span><span style="color:#0F9FB9">0</span></div><div style="padding:0 6px; white-space:pre; line-height:120%">...</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">C:\Users\Suyeon&nbsp;Kim<span style="color:#0086B3"></span><span style="color:#ED7803">&gt;</span>hexo&nbsp;init&nbsp;blog</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">...&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">Thank&nbsp;you&nbsp;<span style="color:#ED7803">for</span>&nbsp;installing&nbsp;EJS:&nbsp;built&nbsp;with&nbsp;the&nbsp;Jake&nbsp;JavaScript&nbsp;build&nbsp;tool&nbsp;(https:<span style="color:#0086B3"></span><span style="color:#ED7803">/</span><span style="color:#0086B3"></span><span style="color:#ED7803">/</span>jakejs.com<span style="color:#0086B3"></span><span style="color:#ED7803">/</span>)</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;found&nbsp;<span style="color:#0F9FB9">0</span>&nbsp;vulnerabilities</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">INFO&nbsp;&nbsp;Start&nbsp;blogging&nbsp;with&nbsp;Hexo<span style="color:#0086B3"></span><span style="color:#ED7803">!</span></div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<br/>
<br/>

#### 6. 프로젝트 폴더 위치에서 hexo 서버 실행
``` bash
$ hexo server
```


<div class="colorscripter-code" style="color:#FFFFFF;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#282525;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px;border-right:2px solid #4f4f4f"><div style="margin:0;padding:0;word-break:normal;text-align:right;color:#aaa;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:120%"><div style="line-height:120%">1</div><div style="line-height:120%">2</div><div style="line-height:120%">3</div><div style="line-height:120%">4</div><div style="line-height:120%">5</div><div style="line-height:120%">6</div><div style="line-height:120%">7</div><div style="line-height:120%">8</div><div style="line-height:120%">9</div></div></td><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#FFFFFF;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:120%"><div style="padding:0 6px; white-space:pre; line-height:120%">C:\Users\Suyeon&nbsp;Kim<span style="color:#0086B3"></span><span style="color:#ED7803">&gt;</span>cd&nbsp;blog</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">C:\Users\Suyeon&nbsp;Kim\blog<span style="color:#0086B3"></span><span style="color:#ED7803">&gt;</span>hexo&nbsp;server</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">INFO&nbsp;&nbsp;Start&nbsp;processing</div><div style="padding:0 6px; white-space:pre; line-height:120%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:120%">INFO&nbsp;&nbsp;Hexo&nbsp;is&nbsp;running&nbsp;at&nbsp;http:<span style="color:#0086B3"></span><span style="color:#ED7803">/</span><span style="color:#0086B3"></span><span style="color:#ED7803">/</span>localhost:<span style="color:#0F9FB9">4000</span>&nbsp;.&nbsp;Press&nbsp;Ctrl<span style="color:#0086B3"></span><span style="color:#ED7803">+</span>C&nbsp;to&nbsp;stop.</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<br/>
<br/>

##### 7. 브라우저에서 http://localhost:4000 접속하여 확인

![20200120_03](https://user-images.githubusercontent.com/28856435/72684672-ff395e80-3b25-11ea-9d04-2a25e1759c3c.jpg)

***

### 다음 포스팅
### 2. git repository - hexo server 연동
1. hexo 배포
2. hexo 테마설정
3. theme & git repository 연동 (_config.yml)