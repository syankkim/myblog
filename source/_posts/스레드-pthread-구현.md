---
title: 스레드 pthread 구현
tags: []
categories:
  - ☁️
thumbnail: ''
permalink: ''
status: ''
date: 2021-05-27 23:50:54
---

<!-- excerpt -->
<!-- toc -->

---

# 스레드

## pthread

## 스레드 조인

## 스레드 디테치

* 리소스
 1. pthread_join
  - 메인 스레드에서 해당 스레드가 종료되면, 상태값을 보고 메인스레드에서 추가처리를 할 수 있다.
 2. pthread_detach(thread1)
  - 관련 리소스를 즉시 해제한다.
  
* 실행
 1. pthread_join
  - 스레드 1이 종료될때까지 다음코드를 수행하지 않고 기다린다.
 2. pthread_detach
  - 스레드 1이 종료될때까지 기다리지 않는다.

## Pthread 뮤텍스 - 상호배제 기법


