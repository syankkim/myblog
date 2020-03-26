---
title: gradle 프로젝트 MariaDB 연동
tags: ['gradle', 'mariadb','jpa']
categories: ['Projects', 'JPA']
thumbnail: ''
permalink: ''
date: 2020-03-16 16:26:02
---

_작성중.._
gradle 프로젝트에서의 mariaDB 연동방법을 알아봅니다.
그리고 JPA 를 간단하게 실습해보기 !
<!-- excerpt -->
<!-- toc -->

---

### Test 소스 구조

![image](https://user-images.githubusercontent.com/28856435/77139690-4efebc80-6aba-11ea-858e-ae959d58ea4a.png)

<br/>

### build.gradle 에 의존성 주입

__build.gradle__
```java
plugins {
    id 'java'
    id 'org.springframework.boot' version '2.1.7.RELEASE'
    id 'io.spring.dependency-management' version '1.0.7.RELEASE'
}

group = 'com.sue'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '1.8'

repositories {
    mavenCentral()
    maven { url "https://plugins.gradle.org/m2/" }
}

dependencies {
    //mybatis
    implementation 'org.springframework.boot:spring-boot-dependencies:2.0.5.RELEASE'
    
    // 스프링 부트를 사용하기 위함
    implementation 'org.springframework.boot:spring-boot-starter-web'
    
    // 데이터를 연동하기 위함
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    
	 //mariadb 사용
    compile("mysql:mysql-connector-java:5.1.34")
    compile("org.mariadb.jdbc:mariadb-java-client")

    // Use JUnit test framework
    testImplementation 'junit:junit:4.12'
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
}

```


### application.yml 설정파일 생성

#### DB 연동 실패한 application.yml
```java
server:
  port: 8081
  servlet:
    context-path: /
      
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://127.0.0.1/sosi?autoReconnect=true&useUnicode=true&characterEncoding=utf8
    username: root
    password: mysql1234
    
    jpa:
    show-sql: true
    hibernate:
      ddl-auto: create
      naming:
        physical-strategy: org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl
      use-new-id-generator-mappings: false
    properties:
       hibernate:
          dialect: org.hibernate.dialect.MySQL5InnoDBDialect
          format_sql: true
    open-in-view: false

  http:
    encoding:
      charset: UTF-8
      enabled: true
      force: true
```

위와 같았던 application.yml 파일을 아래와 같이 고쳤더니 DB 연동에 성공했다.
DB 연동에 필요했던 profile 이 없었던것.
그리고 `datasource` 상위의 속성도 빠뜨려져 있었다.
`ddl-auto` 속성은 DB 생성 이후 `create` -> `update` 로 바꿔주었다.

#### DB 연동 성공한 application.yml
```java
server:
  port: 8081
  servlet:
    context-path: /
    
spring:
  profiles:
    active:       
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/sue
    username: root
    password: ehdrmf
    
  jpa:
    show-sql: true
    hibernate:
      ddl-auto: update
      naming:
        physical-strategy: org.hibernate.boot.model.naming.PhysicalNamingStrategyStandardImpl
      use-new-id-generator-mappings: false
    properties:
       hibernate:
          dialect: org.hibernate.dialect.MySQL5InnoDBDialect
          format_sql: true
    open-in-view: false

  http:
    encoding:
      charset: UTF-8
      enabled: true
      force: true
```






#### find... by...
1. 메소드의 `이름` 만으로 원하는 쿼리를 실행할 수 있는데, `select` 문에서만 가능하다.
2. 현재 실행하는 Repository 의 타입정보를 기준으로 동작함.

다음과 같은 문법들이 존재한다.
* find..By..
* read..By..
* query..By..
* get..By..
* count..By..


### jpa CRUD JUnit Test

