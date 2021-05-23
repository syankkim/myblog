---
title: AWS-Docker,Jira 설치
tags: []
categories: [☁️ AWS]
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-05-22 20:46:29
---

AWS 에서 Jira와 Docker를 설치해보자.
<!-- excerpt -->
<!-- toc -->

---

# AWS 인스턴스에서 Docker 설치
- jira container 는 메모리를 많이 차지하기 때문에 AWS 인스턴스는 최소 `t2.larg` 로 선택해야 한다.
> $ sudo yum install docker-io


<!-- [rectangle setX: 10 y: 10 width: 20 height: 20]; -->

```shell
$ ssh -i suyeon.pem ec2-user@15.164.50.108
The authenticity of host '15.164.50.108 (15.164.50.108)' can't be established.
ECDSA key fingerprint is SHA256:KwsFct4EwSLlShPOuWPC0yr0ewcI4lGT352J9tLKKwQ.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '15.164.50.108' (ECDSA) to the list of known hosts.

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
[ec2-user@ip-172-31-36-132 ~]$ ^C
[ec2-user@ip-172-31-36-132 ~]$ docker
-bash: docker: command not found
[ec2-user@ip-172-31-36-132 ~]$ sudo yum install docker-io

```

## docker ps -a 리스트 확인
- Is the docker daemon running? : 도커를 실행해준다.
 - `sudo systemctl start docker`
- dial unix /var/run/docker.sock: connect: permission denied : 권한 부여
 - `sudo setfacl -m user:ec2-user:rw /var/run/docker.sock`

```shell
[ec2-user@ip-172-31-36-132 ~]$ docker ps -a
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
[ec2-user@ip-172-31-36-132 ~]$ sudo systemctl start docker
[ec2-user@ip-172-31-36-132 ~]$ docker ps -a
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json?all=1": dial unix /var/run/docker.sock: connect: permission denied
[ec2-user@ip-172-31-36-132 ~]$ sudo setfacl -m user:ec2-user:rw /var/run/d
dbus/               dhclient-eth0.pid   dmeventd-server     docker.pid
dhclient6-eth0.pid  dmeventd-client     docker/             docker.sock
[ec2-user@ip-172-31-36-132 ~]$ sudo setfacl -m user:ec2-user:rw /var/run/docker.sock
```

- 잘 실행된다.

```shell
[ec2-user@ip-172-31-36-132 ~]$ docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

---

# Jira 협업툴 설치

1. 기존 지라 도커 컨테이너 삭제
2. 지라 도커 컨테이너 설치
```shell
$ docker pull cptactionhank/atlassian-jira-software:latest
```
3. 지라 도커 컨테이너 생성
- ``
```shell
$ docker create --restart=no --name "jira-container"\
 --publish "8080:8080"\
 --volume "hostpath:/var/atlassian/jira"\
 --env "CATALINA_OPTS= -Xms1024m -Xmx1024m -Datlassian.plugins.enable.wait=300"\
 cptactionhank/atlassian-jira-software:latest
$ 0c8922efd3800885da4b46af5bc17e6804fc91b102e186dec61efa41e39f117d
```
4. 지라 도커 컨테이너 실행
```shell
```

