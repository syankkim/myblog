---
title: 리눅스서버EC2
tags: []
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
status: 'ing'
date: 2021-05-18 00:01:58
---

클라우드 컴퓨팅 환경을 경험해보기. with AWS
<!-- excerpt -->
<!-- toc -->

---



# 리눅스 배포판(패키지)
- 리눅스 커널 및 다양한 소프트웨어 패키지를 묶어서 배포하는것
 - 리눅스 배포판(패키지)

# 클라우드 컴퓨팅 설정 방법
1. EC2 또는 인스턴스(서버) 생성
2. Elastic IP(탄력적 IP)생성
 - 고정IP/동적IP
3. 지기 PC(클라이언트) 에서 EC2(서버) 접속




```shell
$ chmod 400 suyeon.pem
$ ll
total 4
-r--r--r-- 1 SUYEON 197609 1700  5월 18 00:23 suyeon.pem
$
$ ssh -i suyeon.pem  ubuntu@3.34.112.149
The authenticity of host '3.34.112.149 (3.34.112.149)' can't be established.
ECDSA key fingerprint is SHA256:u5P/Pib6W0sp1nNLTvMtbweg4qAibDzeqtC6T5EVWWg.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '3.34.112.149' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 18.04.5 LTS (GNU/Linux 5.4.0-1045-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon May 17 15:29:10 UTC 2021

  System load:  0.0               Processes:           94
  Usage of /:   3.9% of 29.02GB   Users logged in:     0
  Memory usage: 19%               IP address for eth0: 172.31.42.223
  Swap usage:   0%

0 packages can be updated.
0 of these updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ip-172-31-42-223:~$
```