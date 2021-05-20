---
title: 🗯 리눅스서버EC2, 리눅스 기본
tags: ['linux']
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
status: ''
date: 2021-05-18 00:01:58
---

클라우드 컴퓨팅 환경에서 서버를 실행해보자. with AWS
리눅스 파일종류와 쉘(shell), 소프트링크/하드링크 
`#EC2` `#shell` `#Linux` `#hardlink` `#softlink`
<!-- excerpt -->
<!-- toc -->

---

# 리눅스 배포판(패키지)
- 리눅스 커널 및 다양한 소프트웨어 패키지를 묶어서 배포하는것
 - 리눅스 배포판(패키지)

# 클라우드 컴퓨팅 설정 방법 with AWS
- AWS 계정이 없다면, 만들어야 한다.

## EC2 또는 인스턴스(서버) 생성
- 인스턴스 서버를 생성하면 마지막에 `키페어` (.pem) 를 생성할 수 있다. 잘 저장해둔다.

<img width="1242" alt="aws_01" src="https://user-images.githubusercontent.com/28856435/118682817-bdb0e480-b83b-11eb-9915-0dc33531741b.PNG">

<br>

## Elastic IP(탄력적 IP)생성
 - 고정IP/동적IP
 - 탄력적 IP 를 생성하고, 인스턴스와 연결까지 해주어야 성공.

 <img width="836" alt="aws_02" src="https://user-images.githubusercontent.com/28856435/118682878-cdc8c400-b83b-11eb-8339-8d4e4d683dba.PNG">

<br>

## 자기 PC(클라이언트) 에서 EC2(서버) 접속
- 인스턴스를 생성할 때 다운 받은 `.pem` 파일을 시작하기 원하는 위치에 둔다.
- `.pem` 이 있는 위치에서 `ssh -i {.pem 파일} {ubuntu@고정IP}` 수행.
 - eg. `ssh -i suyeon.pem  ubuntu@3.34.112.149`
 - 권한문제는 `chmod 400 suyeon.pem`
* 아래와 같이 `ubuntu@ip-172-31-42-223:~$` 서버 AWS 서버접속이 되는것을 볼 수 있다.

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

---

# 리눅스 기본 구성

## 리눅스 파일
- 모든것은 파일이라는 철학을 따른다.
 - 모든 인터렉션은 read / write
 - 마우스, 키보드와 같은 모든 디바이스 관련된 기술도 파일과 같이 다루어진다.
- 파일 네임스페이스
 - 전역 네임스페이스를 사용한다.
   - eg. /tomcat/ows/driver.txt

## 리눅스 프로세스
- 리눅스 실행 파일 포멧 - `ELF` (Executable and Linkable Format)
  - 콜스택, 코드 (텍스트), 데이터 및 BSS 섹션 등
- 다양한 시스템 리소스와 관련되어 있다. (시스템콜 기반.)
  - 타이머, 시그널, 파일, 네트워크, 디바이스, IPC 기법
- `가상 메모리`를 지원한다.
- 각 프로세스는 `pid`(프로세스 ID) 고유값으로 구분되어 있다.
- `init 프로세스`(첫번째 프로세스) 를 기반으로 `fork()` 시스템콜을 사용해서 신규 프로세스가 생성되는 방식이다.

## 리눅스 권한
- 운영체제는 사용자/리소스 권한을 관리한다.
- 리눅스는 사용자/그룹으로 권한을 관리한다.
- root 는 슈퍼관리자이다.
- 파일마다 소유자, 소유자  그룹, 모든 사용자에 대해 읽기/쓰기/실행 권한을 관리한다. (rwx)
 - 접근 권한 정보는 inode 의 자료구조에 저장된다.
[리눅스 권한 예시👆](#ls-명령어)

## 리눅스 파일 종류
1. 디렉토리
   - 하나의 파일로, 상위 디렉토리 파일에 등록되어 있다.
2. 일반파일
   - 스트림 파일
3. 특수 파일
   - 장치파일 (Device file)
    - 블록 장치(특수)파일, 캐릭터 장치(특수)파일
   - 파이프
   - 소켓


>__블록 장치 파일__
>보통 파일 read/write 요청이 있으면 커널에 전달되어 파일스트림 드라이버에 의해 처리된다. 반면에 장치파일은 요청이 그 장치의 드라이버에 의해서 처리되며, 하드디스크, CD/DVD 등의 저장 장치 파일들이다. `블록단위`로 입출력을 수행한다.
>__캐릭터 장치 파일__
>터미널, 프린터, 키보드 등의 문자 기반 장치 파일을 의미한다. I/O 버퍼를 사용하지 않으며 `바이트 단위`의 입출력만 수행한다.
>__파이프 파일__
>특정 프로그램의 출력을 중간 파일을 거치지 않고 다른 파일의 입력으로 보내는 파일을 의미한다. `FIFO` 방식으로 처리된다.
>__소켓 파일__
>네트워크의 입출력을 담당하는 API(Application Program Interface) 로, 물리적인 두 호스트 컴퓨터 간의 데이터를 송수신 할 때 사용하는 논리적인 소프트웨어 장치파일이다.


---

# 쉘(shell) 이란?
- 사용자와 운영체제간 인터페이스이다.
- 사용자의 명령을 해석해서 커널에 명령을 요청한다.
- 관련된 시스템콜을 사용해서 프로그램이 작성되어 있다.

## 쉘의 종류
- Bourne-Again Shell (bash): GNU 프로젝트의 일환으로 개발되었다.

## 다중 사용자를 지원하는 시스템
- 다중 사용자 관련 명령어는 어떤것이 있을까?

### sudo 명령어
- /etc/sudors 설정 파일에서 설정을 변경할 수 있다.

* 아래와 같이 내가 만드려는 사용자를 `root` 아래에 추가해준다.

```bash
# User privilege specification
root    ALL=(ALL:ALL) ALL
suyn    ALL=(ALL:ALL) ALL
```

* `root` 권한으로 `adduser` 명령어를 사용해 새로운 사용자를 생성한다.
```shell
ubuntu@ip-172-31-42-223:~$ adduser suyn
adduser: Only root may add a user or group to the system.

ubuntu@ip-172-31-42-223:~$ sudo adduser suyn
Adding user `suyn' ...
Adding new group `suyn' (1001) ...
Adding new user `suyn' (1001) with group `suyn' ...
Creating home directory `/home/suyn' ...
Copying files from `/etc/skel' ...
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for suyn
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] y
ubuntu@ip-172-31-42-223:~$ sudo passwd suyn
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully

```

* 생성한 `suyn` 유저로 전환
```shell
ubuntu@ip-172-31-42-223:~$ su - suyn
Password:
suyn@ip-172-31-42-223:~$

```

### ls 명령어
- `al` 옵션을 주면 숨김파일 까지 조회할 수 있다.
- 파일 권한
 - 파일마다 소유자, 소유자그룹, 모든 사용자에대해 권한을 설정할 수 있다.
 - `drwxr-xr-x`
   - d : directory 를 나타냄. [리눅스 파일종류👆](#리눅스-파일-종류)
   - rwx 소유자는 rwx 가능
   - r-x 그룹은 rx 가능
   - r-x 모든 사용자는 rx 가능
 - 소유자 접근 권한 정보는 `inode` 에 저장되어 있다.

```shell
ubuntu@ip-172-31-42-223:~$ ls -al
total 36
drwxr-xr-x 5 ubuntu ubuntu 4096 May 18 15:40 .
drwxr-xr-x 4 root   root   4096 May 18 15:20 ..
-rw-r--r-- 1 ubuntu ubuntu  220 Apr  4  2018 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Apr  4  2018 .bashrc
drwx------ 2 ubuntu ubuntu 4096 May 17 15:29 .cache
drwx------ 3 ubuntu ubuntu 4096 May 17 15:29 .gnupg
-rw-r--r-- 1 ubuntu ubuntu  807 Apr  4  2018 .profile
drwx------ 2 ubuntu ubuntu 4096 May 17 15:24 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 May 18 15:19 .sudo_as_admin_successful
-rw------- 1 ubuntu ubuntu 2106 May 18 15:40 .viminfo
```

> [다시한번 짚고가기] __슈퍼블록 & inode__
>- `슈퍼블록`은 파일 시스템의 정보를 담고있다.
>   - SUPER_BLOCK [ [fileA] [fileB] ] 이런식이다.
>- inode 는 파일이름마다 `inode 고유값`이 매칭되며 `자료구조` 형식으로 관리된다. 또한, inode를 기반의 메타정보(파일권한, 소유자정보, 파일사이즈, 생성시간 등)를 담고있다. 파일 시스템에서는 inode 기반으로 파일에 엑세스한다.
>   - SUPER_BLOCK [ [fileA:inode] [fileB:inode] ] 이런식이다.


### ln 명령어
- 하드링크 : 기존파일의 inode 는 동일하다.
 - `cp` 명령어는 물리적인 공간이 늘어나는 반면에, 하드링크는 동일한 inode 를 사용하되 포인터만 늘어난다고 생각하면 된다. (전체 파일 용량은 달라지지 않는다.)
- 심볼릭 링크 (소프트링크)
 - inode 가 바뀐다. 기존 파일의 위치가 바뀌거나 파일이 삭제되면 소프트링크에 접근할 수 없게된다.

* 하드링크 예시
  - 아래 코드에서 inode 값을 확인! a.txt 와 a_link 의 inode 값은 동일하다.
 `256239` -rw-rw-r-- 2 ubuntu ubuntu 6 May 20 08:39 a.txt
 `256239` -rw-rw-r-- 2 ubuntu ubuntu 6 May 20 08:39 a_link.txt
```shell
ubuntu@ip-172-31-33-123:~$ cat a.txt
asdfg
ubuntu@ip-172-31-33-123:~$ ln a.txt a_link.txt
ubuntu@ip-172-31-33-123:~$ ls -ali *.txt
256239 -rw-rw-r-- 2 ubuntu ubuntu 6 May 20 08:39 a.txt
256239 -rw-rw-r-- 2 ubuntu ubuntu 6 May 20 08:39 a_link.txt
```

* 소프트링크 예시
  - 아래 코드에서 inode 값을 확인! a.txt 와 a_link.txt 의 inode 값은 다르다.
`256241` -rw-rw-r-- 1 ubuntu ubuntu 9 May 20 08:54 b.txt
`256238` lrwxrwxrwx 1 ubuntu ubuntu 5 May 20 08:55 b_link.txt -> b.txt
```shell
ubuntu@ip-172-31-33-123:~$ cat b.txt
softlink
ubuntu@ip-172-31-33-123:~$ ln -s b.txt b_link.txt
ubuntu@ip-172-31-33-123:~$ ls -ali b*
256241 -rw-rw-r-- 1 ubuntu ubuntu 9 May 20 08:54 b.txt
256238 lrwxrwxrwx 1 ubuntu ubuntu 5 May 20 08:55 b_link.txt -> b.txt
ubuntu@ip-172-31-33-123:~$ cat b_link.txt
softlink
```