---
title: 🚀 Django API 서버 생성
tags: []
categories: ['☁️ Django']
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-07-23 00:04:05
---

python venv에 Django API 서버 프로젝트 생성하여 띄워본다.
최종목표는 내 블로그까지 만들어내기 👍🏼
`#python` `#django` `#virtualenv`
<!-- excerpt -->
<!-- toc -->

---

## 가상환경

* 설치

```bash
(base) ➜ Django-prj pip3 install virtualenv
```

* 가상환경 생성

```bash
(base) ➜ Django-prj virtualenv venv
```

* 가상환경 실행

```bash
(base) ➜  Django-prj source venv/bin/activate
(venv) (base) ➜  Django-prj 
```

## Django 설치

```bash
(venv) (base) ➜ pip3 install django
```

* Django 버전 확인

```bash
(venv) (base) ➜  bin python -m django --version
3.2.5
```

## 프로젝트 폴더 ✔️

```bash
(venv) (base) ➜  Django-prj cd venv/bin
(venv) (base) ➜  bin ls
__pycache__      activate.fish    activate_this.py pip              pip3.8           python3.8        wheel-3.8
activate         activate.ps1     django-admin     pip-3.8          python           sqlformat        wheel3
activate.csh     activate.xsh     django-admin.py  pip3             python3          wheel            wheel3.8
```

## Django 기본 프로젝트 생성

```bash
(venv) (base) ➜  bin django-admin startproject jansvc
(venv) (base) ➜  jansvc ll
total 32
-rw-r--r--  1 mac  staff     0B  7 22 23:15 __init__.py
drwxr-xr-x  4 mac  staff   128B  7 22 23:46 __pycache__
-rw-r--r--  1 mac  staff   389B  7 22 23:15 asgi.py
-rw-r--r--  1 mac  staff   3.2K  7 22 23:15 settings.py
-rw-r--r--  1 mac  staff   748B  7 22 23:15 urls.py
-rw-r--r--  1 mac  staff   389B  7 22 23:15 wsgi.py
(venv) (base) ➜  bin cd jansvc
```

> **manage.py**: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티.
**__init__.py**: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일.
**settings.py**: 현재 Django 프로젝트의 환경 및 구성을 저장합니다. Django settings에서 환경 설정 확인.
**urls.py**: 현재 Django project 의 URL 선언을 저장합니다. Django 로 작성된 사이트의 "목차".
**asgi.py**: An entry-point for ASGI-compatible web servers to serve your project.
**wsgi.py**: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다. nginx나 apache로 웹 서버를 사용하게 될 때 그 웹서버와 통신하는 곳.

## 프로젝트 내 App 생성

> Django 프로젝트는 다수의 App이 존재한다.

```bash
(venv) (base) ➜  jansvc python3 manage.py startapp blog
(venv) (base) ➜  jansvc ls
blog      jansvc    manage.py
(venv) (base) ➜  jansvc ll blog
total 40
-rw-r--r--  1 mac  staff     0B  7 22 23:46 __init__.py

-rw-r--r--  1 mac  staff    63B  7 22 23:46 admin.py
-rw-r--r--  1 mac  staff   140B  7 22 23:46 apps.py
drwxr-xr-x  3 mac  staff    96B  7 22 23:46 migrations
-rw-r--r--  1 mac  staff    57B  7 22 23:46 models.py
-rw-r--r--  1 mac  staff    60B  7 22 23:46 tests.py
-rw-r--r--  1 mac  staff    63B  7 22 23:46 views.py
```

## 서버 생성

```bash
(venv) (base) ➜  jansvc python3 manage.py migrate

(venv) (base) ➜  jansvc python3 manage.py createsuperuser
사용자 이름 (leave blank to use 'mac'): sy
이메일 주소: suyans730@naver.com
Password:
Password (again):
Superuser created successfully.

(venv) (base) ➜  jansvc python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
July 22, 2021 - 23:58:58
Django version 3.2.5, using settings 'jansvc.settings'
Starting development server at http://127.0.0.1:8000/
```
<br>

* 서버가 정상적으로 뜬다.jpg 🤩

<img width="1976" alt="장고서버생성" src="https://user-images.githubusercontent.com/28856435/126664170-e4f7b116-2e4b-42ba-a11b-89a02ab36965.png">

<br>