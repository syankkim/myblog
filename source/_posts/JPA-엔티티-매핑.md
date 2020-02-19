---
title: JPA 엔티티 매핑
tags: []
categories: []
thumbnail: ''
permalink: ''
date: 2020-02-16 17:12:54
---

객체와 테이블, 필드와 컬럼, 기본키, 연관관계 매핑에 대해 알아봅니다.
*인프런 강의를 보고 공부하며 작성한 포스트입니다.*
<!-- excerpt -->

<!-- toc -->

### 객체과 테이블 매핑

#### @Table
>엔티티와 매핑할 테이블 지정

```java
@Entity
@Table(name = "MEM_TAB")
public class Member {
    ...}
```
아래와 같이 터미널에 MEM_TAB 에서 조회한것을 볼 수 있다.

```bash
Hibernate: 
    select
        member0_.id as id1_0_0_,
        member0_.name as name2_0_0_ 
    from
        MEM_TAB member0_ 
    where
        member0_.id=?
```
<br/>

#### 데이터베이스 스키마 자동 생성

> DDL 을 애플리케이션 실행 시점에 자동생성
테이블 중심 -> 객체 중심
데이터베이스 방언을 활요해서 적절한 DDL 생성
생성된 DDL 은 개발 장비에서만 사용.

아래의 JPA 옵션을 적용하여 실행할 경우.

__옵션__

```xml
<property name="hibernate.hbm2ddl.auto" value="create" />
```
|옵션|기능|
|----|---|
|create|기존 테이블에서 삭제후 생성 (CREATE+DROP)|
|create-drop|create 와 같으나 종료시점에 테이블 DROP|
|update|변경분만 반영(운영 DB에서는 사용금지)|
|validate|엔티티와 테이블이 정상 매핑되었는지 확인|
|none|사용하지 않음|

###### create

__Member.java__
```java
@Entity
@Table
public class Member {
    @Id
    private Long id;

    @Column(name ="username", length=10)
    private String name;
    private int age;

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public Member(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```

__터미널__
```bash

# 테이블 삭제
Hibernate: 
    
    drop table MEM_TAB if exists

# 테이블 생성 (객체중심)
Hibernate: 
    
    create table Member (
       id bigint not null,
        age integer not null,
        name varchar(255),
        primary key (id)
    )   

# 테이블 조회
Hibernate: 
    select
        member0_.id as id1_0_0_,
        member0_.age as age2_0_0_,
        member0_.name as name3_0_0_ 
    from
        Member member0_ 
    where
        member0_.id=?

```

###### update

__터미널__
```bash
Hibernate: 
    
    alter table Member 
       add column username varchar(10)
Hibernate: 
    select
        member0_.id as id1_0_0_,
        member0_.age as age2_0_0_,
        member0_.username as username3_0_0_ 
    from
        Member member0_ 
    where
        member0_.id=?
```


##### 스키마 자동생성 주의점

> 운영 장비에서는 절대 사용금지
개발 초기단계는 create, update
테스트 서버는 update, validate
스테이징과 운영서버는 validate, none



