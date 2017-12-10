Title: Linux에서 hostname 관리
Date: 2017-01-18
Modified: 2017-01-18
Tags: bash, linux, du, disk
Slug: linux-hostname-management
Authors: imjang57
Summary: Linux에서 호스트명(hostname)을 확인 및 변경하는 방법

# 리눅스(Linux) 호스트명(Hostname) 관리

- Target : CentOS, Ubuntu

## 호스트명 조회

명령어를 실행해서 현재 호스트명 확인 :

```
$ hostname
younghotestserver
```

Redhat 리눅스에서 호스트명이 저장된 파일 확인 :

```
$ cat /etc/sysconfig/network | grep HOSTNAME
younghotestserver
```

Ubuntu 리눅스에서 호스트명이 저장된 파일 확인 :

```
$ cat /etc/hostname
younghotestserver
```

## 호스트명 변경

리눅스 호스트명 변경 :

```
$ sudo hostname newhostname
```

또는

```
$ sudo echo newhostname > /proc/sys/kernel/hostname
```

이 방법은 리눅스가 재부팅될 경우 다시 이전 설정으로 되돌아 간다. 재부팅 후에도 유지되게 하려면 다음과 같이 한다.

- Redhat 리눅스 : `/etc/sysconfig/network` 파일에서 HOSTNAME=호스트명 추가 또는 변경
- Ubuntu 리눅스 : `/etc/hostname` 파일에서 호스트명 변경. 참고로 이 파일은 파일 내용 전체가 호스트명이다.

호스트명을 변경하면 `/etc/hosts` 파일도 같이 체크해주자. 이 파일은 IP 주소와 호스트명을 매핑하기 위한 정보가 포함되어 있다. 자기 자신을 가리키는 정보도 포함되어 있으므로 같이 수정해주는 것이 좋다.

`/etc/hosts` 파일의 내용 :

```
127.0.0.1    localhost    newhostname
::1          localhost    newhostname
```
