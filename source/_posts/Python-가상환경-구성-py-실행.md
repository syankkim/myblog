---
title: 'Python 인터프리터 설치, 가상환경 구성, .py 실행'
tags: []
categories: []
thumbnail: ''
permalink: ''
date: 2020-02-29 10:56:21
---


<!-- excerpt -->
<!-- toc -->

---

### pyenv & Python
Python 설치시, 인터프리터와 라이브러리도 함께 설치한다.
Python은 기본적으로 하나의 의존성에 대해 한 가지 버전만 설치가 가능하다.
인터프리터 환경을 변경해주는 version manager를 설치해준다.
Node.js 의 nvm도 version manager라고 할 수 있다.
Python 의 version manager 는 `pyenv` 이다.

#### Python 다운로드
가장먼저 Python 설치가 필요하다.
공식사이트에서 Window 용, v3.6.0 을 설치했다.

#### pyenv 설치




### 가상환경 -virtualenv
#### virtualenv 가상환경 설치
원하는 경로에서 실행하거나 명령어 뒤에 경로를 포함하여 실행해준다. 
필자의 경우 `pythonPrj`라는 작업 디렉토리에서 `test-prj`명으로 설치를 진행했다.

`python -m pip install virtualenv "가상환경경로"`

```bash
$ pwd
$ /c/Users/SUYEON/pythonPrj
$ python -m pip install virtualenv
```

#### 가상환경 생성
원하는 가상환경명으로 생성해준다.
`virtualenv "가상환경명"`

```bash
$ virtualenv test-prj
```

#### 가상환경 실행
`source {가상환경/Scripts/activate}` 를 실행하면 가상환경이 구동된다.

```bash
$ source test-prj/Scripts/activate
(test-prj)
```
#### 가상환경 종료
```bash
$ deactivate
```

