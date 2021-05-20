---
title: 시스템콜과 API
tags: []
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-05-20 23:59:59
---

시스템 프로그래밍
<!-- excerpt -->
<!-- toc -->

---

# 시스템콜
- 주요 시스템콜 read(), write(), open()

## 시스템콜은 어떻게 구현?

```c
mov eax, 1 // 시스템콜 번호
mov ebx, 0
int 0x80 // 소프트웨어 인터럽트 명령
```

# API
- 응용 프로그램과 분리된 하위 호환 인터페이스
 - eg. 시스템콜 래퍼, 입출력 라이브러리 등
 - process_fork(){fork()}
