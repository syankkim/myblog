---
title: JPA 플러시, 준영속 상태
tags: JPA
img: <img width="25" alt="inflearn2" src="https://user-images.githubusercontent.com/28856435/74893276-55244f00-53cf-11ea-8a6d-90ac0c4eb72a.png">
categories: []
thumbnail: ''
permalink: ''
date: 2020-02-16 16:50:54
---

플러시와 준영속 상태에 대해 알아봅니다.
<!-- excerpt -->
<!-- toc -->

### 플러시?

> 영속성 컨텍스트의 변경내용을 데이터베이스에 적용.
<br/>

#### 플러시 작용 순서

1) 변경감지
2) 수정된 엔티티쓰기지연 sql  저장소에 등록
3) flush() : 쓰기지연 sql 저장소에 있는 쿼리들이 DB에 반영이 됨.

#### 플러시는 동기화를 위한 수동호출

>트랜잭션 커밋시 자동호출됨.
JPQL 실행시 자동호출됨.
트랜잭션이라는 작업 단위가 중요하다, 커밋 직전에만 동기화하면 된다.


```java
Member member = new Member(200L, "member200");

// 1차 캐시에 저장됨.
em.persist(member);

// 쓰기지연 SQL 저장소 -> DB
em.flush();

```

### 준영속 상태

#### 특정 엔티티만 준영속 상태로
JPA 에서 조회(em.find) 했을때 1차 캐시에 없을 때 DB에서 가져와 넣음.
>em.detach()

```java
 Member findMember1 = em.find(Member.class, 150L);
findMember1.setName("AAAA");

// JPA 가 관리하지 않음. (select 문은 실행하지만 update 문은 실행하지 않음.)
em.detach(findMember1);

```
#### 영속성 컨텍스트의 모든값을 초기화
>em.clear()

#### 영속성 컨텍스트를 종료
>em.close()