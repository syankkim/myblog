---
title: 'Git pull 오류: Nothing to fetch'
tags: ['git']
categories: [☁️ Git]
thumbnail: ''
permalink: ''
date: 2020-03-17 12:09:22
---

💬 _작성중_
이클립스에서 Git pull 오류: Nothing to fetch 해결 방법입니다.
<!-- excerpt -->
<!-- toc -->

---

### Git pull 오류

이클립스에서 git pull 을 실행하고 아래와 같으 오류를 직면했다.

![image](https://user-images.githubusercontent.com/28856435/76814014-f969ac00-683c-11ea-865c-62c14c550d22.png)

#### 원인?
>remote 에 fetch 가 잡히지 않아서이다.

그럼 또 의문이 생긴다. 왜 remote 에 fetch 를 잡아줘야 할까 ?
Git 에 대해 정확한 개념이 잡혀 있지 않은 듯해서 모호한 개념들에 대해 찾아봤다.

### origin remote 정확히 짚고 가기

필자의 블로그 repository 주소는 `https://github.com/ksso730/myblog.git` 이다.
로컬에 이 서버를 clone 하게되면 Git 은 자동으로 `origin` 이라는 이름을 붙인다.
`origin` 으로부터 해당 repository 데이터를 모두 받고, `master` 브랜치를 가리키는 포인터를 만든다. 이 포인터를 `origin/master` 라 부른다.
Git 은 로컬의 `master` 브랜치가 `origin/master` 를 가리키게 한다.

정리해보자면 ,

`https://github.com/ksso730/myblog.git`

(My Computer - origin/master) -> 






