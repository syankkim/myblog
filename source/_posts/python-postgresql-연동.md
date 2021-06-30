---
title: python postgresql 연동
tags: []
categories: [☁️ DataBase]
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-06-23 13:36:02
---

python postgresql 연동
<!-- excerpt -->
<!-- toc -->

---

# psycopg2 를 이용하여 Python Database 연동

1. Database 정보 config.ini 설정

* config.ini
```bash
[DB]
host=172.23.174.55
database=mydatabase
user=mydb
password=1234
port=5432
```

2. DB Load & Connect

* main.py
```python
import psycopg2
import config
import sys

# Load DB => config.{.ini파일}(section={해당 DB 설정변수})
db=config.config(section='DB')

conn = None
try:
    conn = psycopg2.connect(**db)
    curs = conn.cursor()
    curs.execute(query['select'],(user_id, phone_num))
```


# Python Database API
- fatchone
- fatchall
- fatchmany(row개수)

# 파일 데이터 처리
읽기(r), 쓰기(w 혹은 x), 추가(a), 수정(+) 모드