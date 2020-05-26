---
title: 개발일지🌟 DB Connection Pool Error (DBCP)
tags: ['DBCP','DataBase']
categories: [☁️ DataBase]
thumbnail: ''
permalink: ''
date: 2020-04-27 10:43:05
---

DB Connection Pool Error 의 원인을 찾아보며
`DB Connection Pool` 이 무엇인지, `DBCP` 의 개념, `Hikari Pool` 의 작동방식을 공부.
<!-- excerpt -->
<!-- toc -->

---

<br/>

## ISSUE[1] DB Connection Pool ERROR

### 현상
>__DB Connection pool error timeout waiting for idle object__
```
 DatabaseException - nested exception is org.apache.ibatis.exceptions.PersistenceException:
### Error updating database.  Cause: org.springframework.jdbc.CannotGetJdbcConnectionException: 
Could not get JDBC Connection; nested exception is java.sql.SQLException: Cannot get a 
connection, pool error Timeout waiting for idle object
```

### 당시 DataBase config
`#max-active` `#min-idle` `#max-idle`
>* 풀의 초기 커넥션 갯수 : 10
>* Idle상태에 풀이 소유한 최소 커넥션 갯수 : 10
>* Idle상태에 풀이 소유한 최대 커넥션 갯수 : 30
>* 최대 커넥션 갯수 : 50
>* 커넥션이 존재하지 않을 때, 커넥션을 얻기까지 대기하는 최대 대기시간 : 5000

### 원인 : @Transaction
특정 API 에서 `@Trnasaction` 이 걸려있었던 상태.
이 `transaction`이 `commit` 되지 않은 상태에서 이 API 의 요청이 급증하면서 connection 이 부족하게 되고, __DB Dead Lock__ 에 빠지게 되었다.

게다가 해당 API 내에서 또다른 API나 외부호출 기능 수행단계는 7단계를 거쳐야 했다. 그러니 요청이 많이 오거나 중간단계에서 실패하면 부하가 걸릴 수 밖에 없었던 것이다.

### 해결

결론적으로는 @Transactional 어노테이션이 제거하기로 하였다.

---
<br/>


`JDBC` `DBCP`
## 일반적으로 DB 에서 Connection 을 얻어오는 과정
>1. DB 서버접속을 위한 JDBC 드라이버를 로드한다.
2. DB 접속정보와 DriverManager.getConnection() 을 통해 DB Connection 을 얻는다.
3. Connection 객체로부터 쿼리 수행을 위한 PreparedStatement 객체를 받는다.
4. executeQuery 를 수행후 ResultSet 객체로 결과를 처리한다.
5. 완료 후, 사용된 리소스들을 close() 하여 반환한다.

웹 애플리케이션은 HTTP 요청에 의해 Thread 를 생성하게 되고 대부분의 비지니스 로직은 DB 서버로부터 데이터를 얻게 된다.
웹 어플리케이션을 지탱하는 WAS 에서 DB 서버에 접근을 시작하고 데이터를 가져오기까지 어느 단계에서 가장 많은 비용이 소비될까.

![image](https://user-images.githubusercontent.com/28856435/80331215-6764b280-8882-11ea-93f6-277ba2a0a99d.png)
     
위와 같은 모든 요청에의해 DB접속을 위한 Driver를 로드하고 Connection 객체를 생성하여 연결한다면 물리적으로 DB 서버에 지속적으로 접근해야 한다.

## DBCP (HikariCP)
>이러한 문제를 해결하기 위해 나온 것이 **DBCP** 이다. DB Connection 객체를 생성하고 연결하는데 드는 비용과 시간을 줄이고 네트워크 연결에 대한 부담을 줄여준다.
SpringBoot 2.x 출범 이후 HikariCP 를 기본JDBC Connection Pool 로 사용 가능하게 되었다고 한다. 다른 Connection Pool 에 비해 성능이 압도적이라고 한다.
_[HikariCP Dead lock에서 벗어나기 - 우아한형제들 기술블로그](https://woowabros.github.io/experience/2020/02/06/hikaricp-avoid-dead-lock.html) 를 바탕으로 작성되었습니다._

### getConnection
**1. hikariPool._getConnection()_**
Thread 는 HikariCP 로부터 `connection` 을 요청한다.

**2. hikariPool._concurrentBag.borrow()_**
**2-a)** 현재 Thread 가 이전에 사용했던 `connection` 리스트 중에 현재 사용가능한(idle) connection이 있는가
`?connection:2-b`
**2-b)** hikari pool 전체 connection 중 현재 사용가능한(idle) connection이 있는가
`?connection:2-c`
**2-c)** _concurrentBag.handOffQueue_ (다른 Thread 가 쓰고 반납) 에 사용가능한(idle) connection이 있는가
`?connection:2-d`
**2-d)** connectionTimeout 이 지났는지 확인한다. (HikariCP default Connection Timeout 은 30초)

### connection.close()
transaction 이 정상적으로 commit 혹은 오류로 인한 rollback 이 되면 `connection.close()` 가 호출되어 connection 을 Pool 에 반납한다.
1. Thread : connection.close() 
2. Hiraki
2-a) poolEntry.setState(SATE_NOT_IN_USE) idle Connetion 으로 변환.
2-b) concurrentBag.handOffQueue.off(poolEntry)

## 마치며
위에서 해결한 connection pool error 의 원인은 transaction 에 의한 오류였다. 다음 포스팅에서는 이상적인 `#max-active` `#min-idle` `#max-idle` 을 설정하기 위해서는 무엇을 고려해봐야 하는지 끄적여보려 한다.



