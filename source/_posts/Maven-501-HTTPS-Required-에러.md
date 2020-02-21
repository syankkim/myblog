---
title: Maven 501 HTTPS Required , protocol_version Error
tags: [maven, maven-err]
categories: [Maven]
thumbnail: ''
permalink: ''
date: 2020-02-18 14:58:11
---

+Maven 빌드 중, 501 HTTPS Required 에러
+jdk 버전에 따른 protocol_version 버전 불일치 에러
+cached in the local repository, resolution will not be reattempted
<!-- excerpt -->
<!-- toc -->

---

### Maven Repository 정책변경

2020.01.15 이후 Maven Repository 정책이 아래와 같이 변경되었다.

```text
Effective January 15, 2020, The Central Repository no longer supports insecure communication over plain HTTP and requires that all requests to the repository are encrypted over HTTPS.
If you're receiving this error, then you need to replace all URL references to Maven Central with their canonical HTTPS counterparts.
```

![image](https://user-images.githubusercontent.com/28856435/74709270-1de45f80-5262-11ea-94af-7495280c30c0.png)

Central Repository  는 일반 HTTP를 통한 통신을 지원하지 않으며 `HTTPS` 를 통해 암호화 되어야 한다는 이야기다. settings.xml 에 Maven Central 에 대한 URL 참조를 `HTTP -> HTTPS` 로 바꿔주면 된다.

아래와 같이 <url> 값을 바꿔주고 <pluginRepositories> 설정을 추가해준다.

---

#### maven 501 해결법 ?

__settings.xml 에 수정__

```xml
<profile>
         <id>myprofile</id>
         <repositories>
            <repository>
               <releases>
                  <enabled>true</enabled>
               </releases>
               <id>central</id>
			   <name>Central Repository</name>
               <url>https://repo.maven.apache.org/maven2</url>         
			    <layout>default</layout>
				<snapshots>
					<enabled>false</enabled>
				</snapshots>
            </repository>
         </repositories>
         <pluginRepositories>
            <pluginRepository>
               <releases>
                  <enabled>true</enabled>
				  <updatePolicy>never</updatePolicy>
               </releases>
               <id>central</id>
			   <name>Central Repository</name>
               <url>https://repo.maven.apache.org/maven2</url>
			   <layout>default</layout>
				<snapshots>
					<enabled>false</enabled>
				</snapshots>
            </pluginRepository>
         </pluginRepositories>
      </profile>
```
<br/>

### Received fatal alert: protocol_version

501 에러는 벗어났지만 위와 같은 설정후에도 또 다른 오류가 났다.
이번엔 프로토콜 오류.

`Received fatal alert: protocol_version`
아래 로그에서 이 오류를 찾을 수 있다.

```bash
[ERROR] The build could not read 1 project -> [Help 1]
[ERROR]
[ERROR]   The project com.olleh.gigaeyes:gigaeyes-cvsaas-ems:1.3.3 (C:\Users\ksso7\eclipse_trunk\vsaas-api-center\gigaeyes-cvsaas-ems\pom.xml) has 1 error
[ERROR]     Non-resolvable parent POM for com.olleh.gigaeyes:gigaeyes-cvsaas-ems:1.3.3: Could not transfer artifact org.springframework.boot:spring-boot-starter-parent:pom:1.5.2.RELEASE from/to central (https://repo.maven.apache.org/maven2): Transfer failed for https://repo.maven.apache.org/maven2/org/springframework/boot/spring-boot-starter-parent/1.5.2.RELEASE/spring-boot-starter-parent-1.5.2.RELEASE.pom and 'parent.relativePath' points at no local POM @ line 12, column 10: Received fatal alert: protocol_version -> [Help 2]
```

#### protocol_version 해결법 ?

JDK 버전에 따라 지원하는 TLS 버전이 달랐다

|JDK version|지원 프로토콜 버전|
|-----------|---------------|
|JDK 1.7|TLS v1.0~v1.1|
|JDK 1.8|TLS ~v1.2|

1) JDK 버전이 1.7 이라면 1.8 로 버전업 시켜주거나
2) maven build 시에 아래 옵션을 추가해준다.
 `-Dhttps.protocols=TLSv1.2`

```bash
$ mvn install -Dhttps.protocols=TLSv1.2
```

### cached in the local repository, resolution will not be reattempted

그리고 또다른 오류 직면 ..

```bash
[ERROR] Failed to execute goal on project gigaeyes-cvsaas-ems: Could not resolve dependencies for project com.olleh.gigaeyes:gigaeyes-cvsaas-ems:war:1.3.3: Failure to find com.olleh.gigaeyes:gigaeyes-cvsaas-lib-commons:jar:1.1.0 in https://repo.maven.apache.org/maven2 was cached in the local repository, resolution will not be reattempted until the update interval of central has elapsed or updates are forced -> [Help 1]
```

#### 메이븐 강제 업데이트하기

`-U` 를 추가해준다. 메이븐 강제 업데이트 옵션이다.
>-U 명령어 = Force Update of Snapshots/Releases

```bash
$ mvn -Dhttps.protocols=TLSv1.2 -U install
```
