---
title: JPA 공통 매핑정보 사용
tags: [jpa]
categories: [☁️ JPA]
img: <img width="25" alt="inflearn2" src="https://user-images.githubusercontent.com/28856435/74893276-55244f00-53cf-11ea-8a6d-90ac0c4eb72a.png">
thumbnail: ''
permalink: ''
date: 2020-03-04 23:07:50
---

@MappedSuperclass 공통 속성을 모아두는 클래스.
공통 객체에서 상속받아 공통 속성들을 사용한다.
<!-- excerpt -->
<!-- toc -->

---

### @MappedSuperclass
`BaseEntity` 클래스.
자주쓰이는 공통으로 사용되는 매핑정보들을 모아, 상속받아 사용.
실무에서 많이 사용되는 방식이다.
추상 클래스로 만들어둔다. `abstract`
물론 조회는 안된다.

```java
@MappedSuperclass
public abstract class BaseEntity {
    private String modDate;
    private String regDate;
    private String createdBy;
}
```

예를 들어 Member 가 BasdEnty 를 상속받는다면,

```java
@Entity
public class Member extends BaseEntity {
    @Id
    @GeneratedValue
    @Column(name = "MEMBER_ID")
    private Long id;

    @Column(name = "USERNAME")
    private Long username;

```

```java
try{
    Member member = new Member();
    member.setCreatedBy("Sue");
    member.setModDate("20200212");
    member.setRegDate("20200110");

    em.persist(member);
    ...
}
```

아래와 같이 상속받은 슈퍼 클래스의 값이 잘 입력된것을 확인 !

![image](https://user-images.githubusercontent.com/28856435/75888907-6cebe080-5e6f-11ea-9e33-17dc4321d674.png)
