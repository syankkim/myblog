---
title: JPA-QueryDsl 간단 쿼리 작성법
tags: ['jpa','querydsl']
categories: [☁️ JPA]
img: <img width="25" alt="inflearn2" src="https://user-images.githubusercontent.com/28856435/74893276-55244f00-53cf-11ea-8a6d-90ac0c4eb72a.png">
thumbnail: ''
permalink: ''
date: 2020-05-05 02:45:47
---

JPA 의 Querydsl 여러 문법에 활용하는 예제를 통해 쿼리를 작성해봅니다.
`Q-type` `검색조건` `fetch()` `fetchCount()` `QueryResults` `페이징`
<!-- excerpt -->
<!-- toc -->

---

<br/>

## Q-type 활용
```java
@Test
public void startQuerydsl(){
        queryFactory = new JPAQueryFactory(em);
// Q-type 활용 방법1
//        QMember m1 = new QMember("m1");
// Q-type 활용 방법2
//        QMember m1 = QMember.member;

// Q-type 활용 방법3 -권장 static method QMember.member
        Member findMember = queryFactory
                .select(member)
                .from(member)
                .where(member.username.eq("mem1"))  // PrepareStatement 의 parameterBinding 방식을 사용함.
                .fetchOne();

        assertThat(findMember.getUsername()).isEqualTo("mem1");
    }
```

## 검색 조건
`fetch` : 리스트 조회, 데이터 없으면 `null` 반환
`fetchOne` : 단건 조회
&nbsp;&nbsp;&nbsp; - 결과 없으면 `null`
&nbsp;&nbsp;&nbsp; - 둘 이상이면 `com.querydsl.core.NoneUniqueResultException`
`fetchFirst` = limit(1).fetchOne()
`fetchResults` : 페이징 정보를 포함. (+)total count 쿼리
`fetchCount` : count 쿼리로 변경하여 실행

```java
@Test
    public void resultFetch(){

        // 1 여러건 조회
       List<Member> fetch = queryFactory
               .select(member)
               .fetch();

       // 2 단건조회
       Member fetchOne = queryFactory
               .selectFrom(member)
               .fetchOne();

       // 3 처음 한건 조회
       Member fetchFirst = queryFactory
               .selectFrom(member)
               .fetchFirst();

        // 4 페이징에서 사용.
        //   쿼리를 두 번 실행함.
        QueryResults<Member> results = queryFactory
                .selectFrom(member)
                .fetchResults();
        long total = results.getTotal();
        System.out.println("total => "+total);
        List<Member> content = results.getResults();

        // 5 count 만 조회
       long count = queryFactory
               .selectFrom(member)
               .fetchCount();

    }
```

__4 페이징에서 사용__ `QueryResults` 를 사용하여 실행되는 쿼리를 확인해보면
count 를 조회하는 쿼리, 실제 member데이터들을 조회하는 쿼리, 2번 실행되는 것을 볼 수 있다.
> 따라서 성능을 따진다면 count 쿼리를 따로 작성하여 실행해야 한다.

```bash
2020-05-06 22:22:57.278 DEBUG 15676 --- [    Test worker] org.hibernate.SQL                        : 
    select
        count(member0_.member_id) as col_0_0_ 
    from
        member member0_
2020-05-06 22:22:57.418 DEBUG 15676 --- [    Test worker] org.hibernate.SQL                        : 
    select
        member0_.member_id as member_i1_0_,
        member0_.age as age2_0_,
        member0_.team_id as team_id4_0_,
        member0_.username as username3_0_ 
    from
        member member0_
total => 4
```

__5 count 만 조회__
```bash
 select
        count(member0_.member_id) as col_0_0_ 
    from
        member member0_
```