---
title: JPA 영속성 컨텍스트
date: 2020-02-15 12:19:04
tags: [JPA]
img: <img width="25" alt="inflearn2" src="https://user-images.githubusercontent.com/28856435/74893276-55244f00-53cf-11ea-8a6d-90ac0c4eb72a.png">
categories: [☁️ JPA]
thumbnail: ''
permalink: ''
---

JPA 를 이해하는데 가장 중요한 용어.
엔티티 매니저와 영속성 컨텍스트를 알아봅니다.
<!-- excerpt -->

<!-- toc -->

---

### Entity Manager (엔티티 매니저)

>Entity Manager : Persistence Context = 1 : 1
<br/>

### Persistence Context (영속성 컨텍스트)

>엔티티를 영구 저장하는 환경.
엔티티 매니저를 통해서 영속성 컨텍스트에 접근한다. 영속성 컨텍스트는 직접적으로 눈에 보이지 않는다.
EntityManager.persist(entity);
<br/>

#### 영속, 비영속, 준영속, 삭제

__비영속 상태__

```java
// 객체를 생성한 상태(비영속)
Member member = new Member();
member.setId("member");
member.setUsername("회원1");
```

__영속 상태__
```java
// 객체를 생성한 상태(비영속)
Member member = new Member();
member.setId("member");
member.setUsername("회원1");

// EntityManager -> Persistence Context 영속
em.persist

// 커밋하는 순간 데이터베이스에 수행됨.
tx.commit();
```

__준영속, 삭제 상태__

```java
em.persist
// 준영속
em.detach(member);
tx.commit();
```

```java
em.persist
// 준영속
em.detach(member);
tx.commit();
```
>`em.persist(member)` 를 넣으면 무슨일이 일어날까?
여기서 영속성 컨텍스트의 이점을 알 수 있다.
<br/>


#### 영속성 컨텍스트의 이점

```java
Member member1 = new Member(150L, "A");
Member member2 = new Member(160L, "B");

em.persist(member1);
em.persist(member2);

tx.commit();
```
`em.persist(member)` -> 1차 캐시에들어간다.

`tx.commit()` -> UPDATE 변경이 반영됨.
<br/>

__1차캐시 테이블__

|@id|Entity|
|---|-----|
|"member1"|member1|
|"member2"|member2|

사실, 1차 캐시는 데이터베이스의 하나의 트랜젝션 안에서만 의미가 있다.

```java
Member findMember1 = em.find(Member.class, 1L);
// 1L 1차캐시에 영속성을 넣어둠.
Member findMember2 = em.find(Member.class, 1L);
```

아래와 같이 이미 1차 캐시에 존재하기 때문에 select 를 한번만 실행.
```bash
Hibernate: 
    select
        member0_.id as id1_0_0_,
        member0_.name as name2_0_0_ 
    from
        Member member0_ 
    where
        member0_.id=?
```
<br/>

### 엔티티 수정 -변경감지 (Dirty Checking)

아래와 같이 Member 테이블이 있다고 하자.

|ID|NAME|
|---|----|
|150|A|
|160|B|

```java
Member findMember1 = em.find(Member.class, 150L);
findMember1.setName("ZZZZZ");

// em.persist() ~~?? 안해도 된다.
tx.commit();
```
>가져온 obj 에 setName 만 해주니 UPDATE 가 되었다. 어떻게 가능한걸까 ?
변경 transaction 이 commit 되는 시점에서 JPA 가 1차 캐시 내부의 @id, Entity, 스냅샷을 모두 비교한다. 
Dirty Checking 의 과정은 아래와 같다.

<br/>

#### Drirty Checking Flow

1) flush() -> 영속성 컨텍스트(entityManager)
:: findMember1.setName("ZZZZZ");

2) 엔티티와 스냅샷 비교

|@id|Entity|스냅샷|
|---|-----|-----|
|"member1"|member1|member1스냅샷
|"member2"|member2|member2스냅샷

3) update SQL 생성 -> `쓰기지연 SQL 저장소`

4) flush -> SQL update 적용

5) commit() -> DB
<br/>

### 엔티티 삭제

```java
Member memberA = em.find(Member.class, "memberA");
em.remove(memberA);
```
