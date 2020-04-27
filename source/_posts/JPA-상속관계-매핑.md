---
title: JPA 상속관계 매핑
tags: [jpa]
categories: [☁️ JPA]
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
컬럼을 구분하기 위한 기능.
단일 테이블 전략에서 사용된다. (현재는 추가하지 않아도 자동으로 setting됨)


##### @DiscriminatorValue(~~~)
---

#### 조인전략
__장점__
> 테이블 정규화
`외래키 참조 무결성 제약조건` 활용가능
저장공간 효율화

__단점__
> 조인을 많이 사용, 성능 저하
조회 쿼리복잡
데이터 저장시 INSERT 2번 호출

여기서 잠깐짚고 넘어가는.. 잊혀진 상식..!

__무결성 제약조건__
데이터베이스에 들어있는 데이터의 정확성(일관성)을 보장하기 위해 부정확한 자료가 데이터베이스 내에 저장되는 것을 방지하기 위한 제약 조건을 의미함

|무결성의 종류 |설명|
|---------------|-----|
|널 무결성 | 릴레이션의 특정속성 값이 Null이 될 수 없도록 하는 규정|
|고유 무결성 | 릴레이션의 특정 속성에 대해서 각 튜플이 갖는 값들이 서로 달라야 한다는 규정|
|참조 무결성 | 외래키 값은 Null이거나 참조 릴레이션의 기본키 값과 동일해야 한다는 규정 즉 릴레이션은 참조할 수 없는 외래키 값을 가질 수 없다는 규정|
|도메인 무결성 | 특정 속성의 값이, 그 속성이 정의된 도메인에 속한 값이어야 한다는 규정|
|키 무결성 | 하나의 테이블에는 적어도 하나의 키가 존재해야 한다는 규정|


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

아래와 같이 ITEM 을 상속받은 MOVIE 에 ID 가 동일하게 들어갔음을 확인할수 있다.
![image](https://user-images.githubusercontent.com/28856435/75882576-cac6fb00-5e64-11ea-8060-57c9cb79bfe4.png)

<br/>

---

#### 단일 테이블 전략

설계시 간단한 조건일 경우 많이 사용.
단일 테이블 전략은 한 테이블에 모두 밀어넣는 방법!

__장점__
> 조인이 필요없음, 조회성능 빠름
조회쿼리가 단순.

__단점__
> 자식 엔티티가 매핑한 컬럼은 모두 NULL
하나의 테이블에 모두 저장되므로 오히려 느려질 수도 있는 상황 발생우려.

아까 조인전략에서 했던 그대로에서 Items 클래스의 상속전략만 `SINGLE_TABLE` 로 바꿔준다.

```java
@Inheritance(strategy = InheritanceType.SINGLE_TABLE)
public class Items {
    ...
}
```
그리고 다시실행!
```bash
    /* insert intelli_mapping.Movie
        */ insert 
        into
            Items
            (name, price, actor, director, DTYPE, id) 
        values
            (?, ?, ?, ?, 'Movie', ?)
```

조인전략에서는 실행되는 insert 쿼리가 ITems, Movie 두번이었지만
단일테이블 전략은 한번 실행되는걸 확인가능하다.

테이블이 다시 생성되고,
하나의 테이블에 모든 데이터가 들어갔다.
실행된 query 를 보면 `@DiscriminatorColumn` 을 추가하지 않았지만,
`DTYPE` 이 자동으로 들어간것을 볼 수 있다.

```bash
create table Items (
       DTYPE varchar(31) not null,
        id bigint not null,
        name varchar(255),
        price integer not null,
        actor varchar(255),
        director varchar(255),
        author varchar(255),
        isbn varchar(255),
        artist varchar(255),
        primary key (id)
    )
```
![image](https://user-images.githubusercontent.com/28856435/75884771-bbe24780-5e68-11ea-84a2-0d168b20c0df.png)

<br/>

#### 서브타입 테이블로 변환

이 방법은 실로 잘 쓰이지 않는다고 한다.
각 테이블마다 데이터가 저장되고 조인이 가능한 값이 없어서 ..
만약 ITEM_ID 를 조회하고 싶다면, MOVIE, BOOK, ALBUM 세개 테이블을 모두 조회해봐야 한다는 단점이 있다.
또한, 추후 DB 변동시에도 수정이 어렵다고 한다.

```java
@Entity
@Inheritance(strategy = InheritanceType.TABLE_PER_CLASS)
public class Items {
    ...
}
```

Main은 조인전략과 같이 Movie 에 값을 넣어주도록.
실행하면, Moive 에만 값이 입력된다.
아무튼 비추라니까 .. 간단하게만 짚고 넘어가자.