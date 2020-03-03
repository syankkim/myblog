---
title: JPA 상속관계 매핑
tags: [jpa]
categories: [JPA]
img: <img width="25" alt="inflearn2" src="https://user-images.githubusercontent.com/28856435/74893276-55244f00-53cf-11ea-8a6d-90ac0c4eb72a.png">
thumbnail: ''
permalink: ''
date: 2020-03-04 00:32:57
---

상속관계 매핑을 통해 모델링 전략을 알아봅니다.
조인전략, 단일 테이블전략, 구현 클래스마다의 서브테이블로,의 전략.
<!-- excerpt -->
<!-- toc -->

---

### 상속관계 매핑

#### 논리모델을 실제 물리모델로

![modeling](https://user-images.githubusercontent.com/28856435/75794895-ce9b4480-5db4-11ea-97a9-7151cbffc627.jpg)

1) 조인전략: 각각 테이블로 변환
 상속관계로 가져옴 item 이 부모(라고 가정) > 자식들(alberm, movie, book)
 각 자식들은 부모의 id 를 상속받는다.

2) 단일 테이블전략 : 통합 테이블로 변환
 item 테이블에 모두 들어있음.

3) 구현 클래스마다 : 서브타입 테이블로 변환
 부모없이, (alberm, movie, book) 각 클래스마다 테이블전략

<br/>

#### 어노테이션

##### @Inheritance(strategy=InheritanceType. ~~)
조인전략: `JOINED`
단일 테이블전략: `SINGEL_TABLE`
각 클래스마다 테이블: `TABLE_PER_CLASS`

##### @DiscriminatorColumn(name="DTYPE")

##### @DiscriminatorValue(~~~)
---

#### 조인전략
__장점__
> 테이블 정규화
외래키 참조 무결성 제약조건 활용가능
저장공간 효율화

__단점__
> 조인을 많이 사용, 성능 저하
조회 쿼리복잡
데이터 저장시 INSERT 2번 호출


__ITEM__
```java
@Entity
@Inheritance(strategy = InheritanceType.JOINED)
public class Item {
    @Id @GeneratedValue
    private Long id;

    private  String name;
    private int price;

}
```
__MOVIE__
```java
@Entity
public class Movie extends Item {

    private String director;
    private String actor;
}
```
__ALBUM__
```java
@Entity
public class Album extends Item{
    private String artist;
}
```
__BOOK__
```java
@Entity
public class Book extends Item {
    private String author;
    private  String isbn;
}
```

실행해 주면,
아래와 같이 테이블 생성이 된다.

<img width="456" alt="h2_item" src="https://user-images.githubusercontent.com/28856435/75796170-985ec480-5db6-11ea-9421-cd47c5af54b6.PNG">

<br/>

movie 객체 하나를 생성해서 넣어준다.
```java
Movie movie = new Movie();
movie.setDirector("suyeon");
movie.setActor("nam");
movie.setName("바람과함께");
movie.setPrice(10000);

em.persist(movie);
```
---

#### 단일 테이블 전략
__장점__
> 조인이 필요없음, 조회성능 빠름
조회쿼리가 단순.

__단점__
> 자식 엔티티가 매핑한 컬럼은 모두 NULL
하나의 테이블에 모두 저장되므로 오히려 느려질 수도 있는 상황 발생우려.