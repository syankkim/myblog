---
title: 🚀 Django API 서버 생성
tags: []
categories: ['☁️ Django']
thumbnail: ''
permalink: ''
status: ''
date: 2021-07-23 00:04:05
---

python venv에 Django API 서버 프로젝트 생성하여 띄워본다.
`#python` `#django` `#virtualenv`
<!-- excerpt -->
<!-- toc -->

---

## 가상환경
_mac 기준으로 작성되었습니다._

* 설치

```bash
➜ Django-prj pip3 install virtualenv
```

* 가상환경 생성

```bash
➜ Django-prj virtualenv venv
```

* 가상환경 실행

[mac 일 경우]
```bash
➜  Django-prj source venv/bin/activate
(venv) ➜  Django-prj 
```
[window 일 경우]
```bash
➜  Django-prj source venv/Scripts/activate
(venv) ➜  Django-prj 
```

## Django 설치

```bash
(venv) ➜ Django-prj  pip3 install django
```

* Django 버전 확인

```bash
(venv) ➜  bin python -m django --version
3.2.5
```

## 프로젝트 폴더 ✔️

```bash
(venv) ➜  Django-prj cd venv/bin
(venv) ➜  bin ls
__pycache__      activate.fish    activate_this.py pip              pip3.8           python3.8        wheel-3.8
activate         activate.ps1     django-admin     pip-3.8          python           sqlformat        wheel3
activate.csh     activate.xsh     django-admin.py  pip3             python3          wheel            wheel3.8
```

## Django 기본 프로젝트 생성

```bash
(venv) ➜  bin django-admin startproject jansvc
(venv) ➜  jansvc ll
total 32
-rw-r--r--  1 mac  staff     0B  7 22 23:15 __init__.py
drwxr-xr-x  4 mac  staff   128B  7 22 23:46 __pycache__
-rw-r--r--  1 mac  staff   389B  7 22 23:15 asgi.py
-rw-r--r--  1 mac  staff   3.2K  7 22 23:15 settings.py
-rw-r--r--  1 mac  staff   748B  7 22 23:15 urls.py
-rw-r--r--  1 mac  staff   389B  7 22 23:15 wsgi.py
(venv) ➜  bin cd jansvc
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
(venv) ➜  jansvc python3 manage.py startapp blog
(venv) ➜  jansvc ls
blog      jansvc    manage.py
(venv) ➜  jansvc ll blog
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
(venv) ➜  jansvc python3 manage.py migrate

(venv) ➜  jansvc python3 manage.py createsuperuser
사용자 이름 (leave blank to use 'mac'): sy
이메일 주소: suyans730@naver.com
Password:
Password (again):
Superuser created successfully.

(venv) ➜  jansvc python3 manage.py runserver
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

# admin 페이지에 model 추가하기

* model.py

```python
from django.db import models

class User(models.Model):
    name= models.TextField()

    def __str__(self):
        return self.name
```

* admin.py

```python
from django.contrib import admin
from .models import User

admin.site.register(User)
```

* `makemigrations` 명령으로 적용
sqlite3에 Blog 클래스를 알려주는 아래 명령어를 사용한다.
`makemigrations`: Blog class의 속성들을 DB야 알아들으렴
`migrate`: 알아들었으면 적용하렴

```bash
> pip3 manage.py makemigrations
```

# 마무리
여기까지 Django서버를 가상환경에 올리고 직접 글작성도 올려보았는데,
프론트를 react로 하여서 블로그를 만드려면 새로운 구조를 모색해 봐야겠다.