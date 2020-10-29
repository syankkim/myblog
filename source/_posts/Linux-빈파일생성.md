---
title: 💻 Linux 빈 파일생성을 위한 cat, cp 성능비교 및 strace
tags: ['linux', 'vi', 'bash']
categories: [☁️ Linux]
thumbnail: ''
permalink: ''
date: 2020-10-29 11:03:52
---

📁 vi 에서 파일 생성법 배우기.
Bash 실행파일을 만들다가 로그를 찍기위해 찾아보게 되었습니다.
`linux` `strace` `cat` `cp`
<!-- excerpt -->
<!-- toc -->

---

<br/>


## cp /dev/null {filename} VS cat /dev/null>>{filename} 
두 명령어의 성능을 비교하기 위해 `strace` 명령을 사용했다.
>strace : 특정 프로그램의 시스템 콜과 시그널을 추적하는 명령
명령어 추적 결과, ✔️cat 의 성능이 더 좋다는 사실.

<br/>

### strace 결과 : cat /dev/null >> {filename}

<div style="border: 1px solid #CACACA; border-radius: 0.5em; padding: 0.1em">
```
> strace -c cat dev/null>> access_test.log   
cat: dev/null: No such file or directory
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0         3           read
  0.00    0.000000           0         4           write
  0.00    0.000000           0        11         7 open
  0.00    0.000000           0         6           close
  0.00    0.000000           0         5           fstat
  0.00    0.000000           0        10           mmap
  0.00    0.000000           0         3           mprotect
  0.00    0.000000           0         2           munmap
  0.00    0.000000           0         3           brk
  0.00    0.000000           0         1         1 access
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         1           arch_prctl
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                    50         8 total
```
</div>
<br/>
<div style="border: 1px solid #CACACA; border-radius: 0.5em; padding: 0.1em">
```
> strace -e open cat dev/null>> access_test.log   
open("/etc/ld.so.cache", O_RDONLY)      = 3
open("/lib64/libc.so.6", O_RDONLY)      = 3
open("/usr/lib/locale/locale-archive", O_RDONLY) = 3
open("dev/null", O_RDONLY)              = -1 ENOENT (No such file or directory)
cat: dev/nullopen("/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = 3
open("/usr/share/locale/en_US.UTF-8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US.utf8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.UTF-8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.utf8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
: No such file or directory
+++ exited with 1 +++
```
</div>

<br/>

###  strace 결과 : cp /dev/null {filename}

<div style="border: 1px solid #CACACA; border-radius: 0.5em; padding: 0.1em">
```
> strace -c cp dev/null access_test.log   
cp: cannot stat `dev/null': No such file or directory
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0        11           read
  0.00    0.000000           0         4           write
  0.00    0.000000           0        23        11 open
  0.00    0.000000           0        15           close
  0.00    0.000000           0         2         1 stat
  0.00    0.000000           0        12           fstat
  0.00    0.000000           0        27           mmap
  0.00    0.000000           0        15           mprotect
  0.00    0.000000           0         3           munmap
  0.00    0.000000           0         3           brk
  0.00    0.000000           0         2           rt_sigaction
  0.00    0.000000           0         1           rt_sigprocmask
  0.00    0.000000           0         1         1 access
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         1           getrlimit
  0.00    0.000000           0         1           geteuid
  0.00    0.000000           0         1           statfs
  0.00    0.000000           0         1           arch_prctl
  0.00    0.000000           0         2         1 futex
  0.00    0.000000           0         1           set_tid_address
  0.00    0.000000           0         1           set_robust_list
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                   128        14 total
```
</div>

<br/>
<div style="border: 1px solid #CACACA; border-radius: 0.5em; padding: 0.1em">
```
gigasurv@DEV_LOGW:~:> strace -e open cp dev/null access_test.log  
open("/etc/ld.so.cache", O_RDONLY)      = 3
open("/lib64/libselinux.so.1", O_RDONLY) = 3
open("/lib64/librt.so.1", O_RDONLY)     = 3
open("/lib64/libacl.so.1", O_RDONLY)    = 3
open("/lib64/libattr.so.1", O_RDONLY)   = 3
open("/lib64/libc.so.6", O_RDONLY)      = 3
open("/lib64/libdl.so.2", O_RDONLY)     = 3
open("/lib64/libpthread.so.0", O_RDONLY) = 3
open("/proc/filesystems", O_RDONLY)     = 3
open("/usr/lib/locale/locale-archive", O_RDONLY) = 3
open("/usr/share/locale/locale.alias", O_RDONLY|O_CLOEXEC) = 3
open("/usr/share/locale/en_US.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.UTF-8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.utf8/LC_MESSAGES/coreutils.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en/LC_MESSAGES/coreutils.mo", O_RDONLY) = 3
cp: cannot stat `dev/null'open("/usr/share/locale/en_US.UTF-8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US.utf8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en_US/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.UTF-8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en.utf8/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
open("/usr/share/locale/en/LC_MESSAGES/libc.mo", O_RDONLY) = -1 ENOENT (No such file or directory)
: No such file or directory
+++ exited with 1 +++
```
</div>

<br/>


## 결과 비교 

💡 위 결과를 눈대중으로만 봐도 `cat` 은 적은 양의 라이브러리를 참조하며, open 하는 파일의 횟수도 상대적으로 적다. 
그에 반해 `cp` 는 `cat`보다 많은 양의 라이브러리를 참조하는것을 알 수 있으며, open file 도 많고, system call 또한 상대적으로 빈번하게 일어난다.

---

<br/>

## Bash 에서 파일 생성법

그래서 `cat` 을 파일생성에 사용하기로 했다.
사용법은 위에서 strace 시험에서 쓰인 명령어 처럼 하면된다.
>cat dev/null>> {filename}