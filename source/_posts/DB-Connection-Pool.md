---
title: 개발일지🌟 DB Connection Pool Error (DBCP)
tags: ['DBCP','DataBase']
categories: [☁️ DataBase]
thumbnail: ''
permalink: ''
date: 2020-04-27 10:43:05
---

DB Connection Pool 이 무엇인지, pool error 의 근본적인 원인을 알아봅니다.
`#max-active` `#min-idle` `#max-idle`
<!-- excerpt -->
<!-- toc -->

## ISSUE[1] DB Connection Pool ERROR
최근 발생한 이슈 중 하나인데, 근본적인 원인은 아래와 같았다.
__DB Connection pool error timeout waiting for idle object__
```
 DatabaseException - nested exception is org.apache.ibatis.exceptions.PersistenceException:
### Error updating database.  Cause: org.springframework.jdbc.CannotGetJdbcConnectionException: 
Could not get JDBC Connection; nested exception is java.sql.SQLException: Cannot get a 
connection, pool error Timeout waiting for idle object
```

## 일반적으로 DB 에서 Connection 을 얻어오는 과정
1) DB 서버접속을 위한 JDBC 드라이버를 로드한다.
2) DB 접속정보와 DriverManager.getConnection() 을 통해 DB Connection 을 얻는다.
3) Connection 객체로부터 쿼리 수행을 위한 PreparedStatement 객체를 받는다.
4) executeQuery 를 수행후 ResultSet 객체로 결과를 처리한다.
5) 완료 후, 사용된 리소스들을 close() 하여 반환한다.

웹 애플리케이션은 HTTP 요청에 의해 Thread 를 생성하게 되고 대부분의 비지니스 로직은 DB 서버로부터 데이터를 얻게 된다.
웹 어플리케이션을 지탱하는 WAS 에서 DB 서버에 접근을 시작하고 데이터를 가져오기까지 어느 단계에서 가장 많은 비용이 소비될까.

![image](https://user-images.githubusercontent.com/28856435/80331215-6764b280-8882-11ea-93f6-277ba2a0a99d.png)
     
위와 같은 모든 요청에의해 DB접속을 위한 Driver를 로드하고 Connection 객체를 생성하여 연결한다면 물리적으로 DB 서버에 지속적으로 접근해야 한다.

이러한 문제를 해결하기 위해 나온 것이 DBCP 이다. DB Connection 객체를 생성하고 연결하는데 드는 비용과 시간을 줄이고 네트워크 연결에 대한 부담을 줄여준다.

## ISSUE[2] 
psql: FATAL: remaining connection slots are reserved for non-replication superuser connections