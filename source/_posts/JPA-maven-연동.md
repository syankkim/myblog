---
title: JPA - maven 연동
date: 2020-02-14 01:19:04
tags: [JPA]
categories: 
thumbnail: ''
permalink: ''
---

JPA 처음 시작하기. 연동과정을 알아보고 H2 를 이용한 기본 CRUD 를 연습해봅니다.
​<!-- excerpt -->

<!-- toc -->
<br/>

*인프런 강의를 보고 공부하며 작성한 포스트입니다.*
<br/>

### JPA - maven 연동설정

#### pom.xml
 1) jpa 하이버네이트 
    추후에 스프링과 연동시 다운받은 스프링 버전과 같이 선택해주는것이 좋다.
 2) H2 데이터베이스
    설치한 버전과 같은 dependency 를 넣어줘야함.
<br/>

#### persistance.xml (rezsources/META-INF/persistance.xml)

`javax.~     속성`: 라이브러리를 바꿔도 사용 가능.
`hibernate.~ 속성`: 하이버네이트 라이브러리에서만 사용 가능.

```XML
<?xml version="1.0" encoding="UTF-8"?>
<persistence version="2.2"
             xmlns="http://xmlns.jcp.org/xml/ns/persistence" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/persistence http://xmlns.jcp.org/xml/ns/persistence/persistence_2_2.xsd">
    <persistence-unit name="hello">
        <properties>
            <!-- 필수 속성 -->
            <property name="javax.persistence.jdbc.driver" value="org.h2.Driver"/>
            <property name="javax.persistence.jdbc.user" value="sa"/>
            <property name="javax.persistence.jdbc.password" value=""/>
            <property name="javax.persistence.jdbc.url" value="jdbc:h2:tcp://localhost/~/test"/>
            <property name="hibernate.dialect" value="org.hibernate.dialect.H2Dialect"/>

            <!-- 옵션 -->
            <property name="hibernate.show_sql" value="true"/>
            <property name="hibernate.format_sql" value="true"/>
            <property name="hibernate.use_sql_comments" value="true"/>
            <!--<property name="hibernate.hbm2ddl.auto" value="create" />-->
        </properties>
    </persistence-unit>
</persistence>
```

<br/>
<br/>

---

### Hello JPA 실습

####  Could not load requested class : org.h2.Driver

h2 는 우선 설치해준다.
<br/>

<img width="590" alt="h2_down" src="https://user-images.githubusercontent.com/28856435/74457147-3273d100-4ecb-11ea-88e2-2a1cf03edf69.png">


분명히  pom.xml 에 H2 데이터베이스를 넣고, persistence.xml 에도 Database Driver 를 설정해주었는데도
JpaMain 코드를 실행하여 데이터베이스 연결을 테스트 했을 때 다음과 같은 connection 오류가 발생했다.

__*Could not load requested class : org.h2.Driver*__
<br/>

```java
public class JpaMain {
    public static void main(String[] args){
        EntityManagerFactory emf  = Persistence.createEntityManagerFactory("hello");
    }
}
```
알고 보니 pom.xml 의 scope 값에

`<scope>[database_name]</scope>`

이 부분의 database_name 이 잘못 들어가 있던것.


statck overflow 검색 결과..

***`On maven docs, it says that <scope>test</scope> dependency is not required for normal use of the application, and is only available for the test compilation and execution phases`***

​메이븐 docs 에느 scope 종속성은 일반적인 어플리케이션에서는 사용되지 않으며,
test 컴파일 및 실행단계에서만  사용된다.

​~~뭐 그렇다고 한다. 이런 기본적인 상식을 모르고 있었다니...~~ &#128580;	
아무튼 scopse 종속성을 제거후 실행하니 연결에 성공했다.

<img width="434" alt="h2_connected" src="https://user-images.githubusercontent.com/28856435/74457145-3273d100-4ecb-11ea-8f25-259f13c4c701.PNG">

<br/>
<br/>
<br/>

---

### INCERT, SELECT, UPDATE (JPQL)

<br/>

#### INCERT
<br/>

```java
public class JpaMain {
    public static void main(String[] args){
        EntityManagerFactory emf  = Persistence.createEntityManagerFactory("hello");

        // 객체를 대신 저장해줌
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();
        tx.begin();
        try{
            Member member = new Member();
            member.setId(1L);
            member.setName("HelloA");
            em.persist(member);
            tx.commit();
        }catch (Exception e){
            em.close();
        }finally {
            emf.close();
        }
    }
}
```

**실행결과**

<img width="78" alt="insert" src="https://user-images.githubusercontent.com/28856435/74457149-330c6780-4ecb-11ea-95c9-c46ef1f7dc9b.PNG">
<br/>
<br/>
<img width="401" alt="memberIncert" src="https://user-images.githubusercontent.com/28856435/74457130-30117700-4ecb-11ea-8dc2-ebeff748c516.PNG">

***
<br/>

#### UPDATE

```java
public class JpaMain {
    public static void main(String[] args){
        EntityManagerFactory emf  = Persistence.createEntityManagerFactory("hello");

        // 객체를 대신 저장해줌
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try{
            Member findMember = em.find(Member.class, 1L);
            System.out.println("findMember.id = "+ findMember.getId());
            System.out.println("findMember.id = "+ findMember.getName());
            findMember.setName("HelloJPA");
            tx.commit();
        }catch (Exception e){
            em.close();
        }finally {
            emf.close();
        }
    }
}
```

**실행결과**
<img width="71" alt="update" src="https://user-images.githubusercontent.com/28856435/74457142-31db3a80-4ecb-11ea-978a-7b333507e9ac.PNG">
<br/>
<img width="406" alt="update_console" src="https://user-images.githubusercontent.com/28856435/74457144-31db3a80-4ecb-11ea-97e0-a9a027734393.PNG">
<br/>
***

#### JPQL - SELECT
```java
public class JpaMain {
    public static void main(String[] args){
        EntityManagerFactory emf  = Persistence.createEntityManagerFactory("hello");

        // 객체를 대신 저장해줌
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = em.getTransaction();
        tx.begin();

        try{
            //jpql 사용 - database 의 방언에 맞춰짐
            List<Member> result = em.createQuery("select m from Member as m", Member.class)
                    .setFirstResult(1)
                    .setMaxResults(4)
                    .getResultList();

            for(Member member: result){
                System.out.println("member.name = "+member.getName());
            }
            tx.commit();

        }catch (Exception e){
            em.close();
        }finally {
            emf.close();
        }
    }
}
```
**실행결과**

```s
member.name = HelloJPA
```
<br/>

<img width="585" alt="select,update" src="https://user-images.githubusercontent.com/28856435/74456258-e2483f00-4ec9-11ea-9497-8de599e74ad6.PNG">
<br/>
<br/>


***

> EntityManagerFactory 는 하나만 생성, 애플리케이션 전체공유.
EntityManager  는  thread 간 공유가 안됨.
<br/>

**JPQL ? 객체지향 SQL**

- 단순한 조회는 EntityManager.find()
- ID 가 4이상 조회하고 싶다면?​
- SQL 을 추상화한 JPQL 이라는 객체지향 쿼리언어 제공.
- JPQL 은 엔티티 객체를 대상으로 쿼리
- SQL 은 데이터베이스 테이블을 대상으로 쿼리

