---
title: 'Python 가상환경 구성, 장고 프로젝트'
tags: [python, virtualenv]
categories: []
thumbnail: ''
permalink: ''
status: 'ing'
date: 2020-02-29 10:56:21
---

_작성중_
Python 가상환경을 virtualenv, anaconda 를 사용하여 설치해봅니다.
가상환경에 장고 프로젝트를 생성합니다.
<!-- excerpt -->
<!-- toc -->

---

## 가상환경 설치

__pyenv & Python__
Python 설치시, 인터프리터와 라이브러리도 함께 설치한다.
Python은 기본적으로 하나의 의존성에 대해 한 가지 버전만 설치가 가능하다.
Window 환경이 아니라면 인터프리터 환경을 변경해주는 version manager를 설치해줘야 한다. Node.js 의 nvm도 version manager라고 할 수 있다.
Python 의 version manager 는 `pyenv` 이다.

__Python 다운로드__
기본적으로 Python 설치가 필요하다.
공식사이트에서 Window 용, v3.6.0 을 설치했다.
---

### virtualenv 를 이용한 가상환경 설치
원하는 경로에서 실행하거나 명령어 뒤에 경로를 포함하여 실행해준다. 
필자의 경우 `pythonPrj`라는 작업 디렉토리에서 `test-prj`명으로 설치를 진행했다.
`python -m pip install virtualenv "가상환경경로"`

```bash
$ pwd
$ /c/Users/SUYEON/pythonPrj
$ python -m pip install virtualenv
```

__가상환경 생성__
원하는 가상환경명으로 생성해준다.
`virtualenv "가상환경명"`

```bash
$ virtualenv test-prj
```

__가상환경 실행__
`source {가상환경/Scripts/activate}` 를 실행하면 가상환경이 구동된다.

```bash
$ source test-prj/Scripts/activate
(test-prj)
```
__가상환경 종료__
```bash
$ deactivate
```
---

<br/>

### anaconda 를 이용한 가상환경 설치
개인적으로 anaconda 의 명령어가 더 간단하다고 느꼈다.
방법은 virtualenv 와 비슷하다. `Anaconda3` 가장 최신 버전으로 다운받았다.
가볍게 사용할 분들은 anaconda의 축소판인 `miniconda` 도 추천한다.

__가상환경 생성__
원하는 가상환경명으로 생성해준다.
`conda create -n "가상환경명"`

```bash
$ conda create -n logon python=3.8
```
__가상환경 list 보기__
생성된 가상환경 리스트를 보여준다.
`conda env list`

```bash
$ conda env list
# conda environments:
#
base                  *  C:\ProgramData\Anaconda3
logon                    C:\ProgramData\Anaconda3\envs\logon
```

__가상환경 실행__
`conda {가상환경명}` 를 실행하면 가상환경이 구동된다.

```bash
$ conda activate logon
(logon)
```
__가상환경 종료__
```bash
(logon)$ conda deactivate
```

## 장고 설치

장고 설치 명령어를 실행해준다.
`pip install django`

```bash
$ pip install django
Installing collected packages: asgiref, sqlparse, pytz, django
Successfully installed asgiref-3.2.7 django-3.0.5 pytz-2019.3 sqlparse-0.3.1
```