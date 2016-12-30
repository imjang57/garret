Title: SSH Host-key identification
Date: 2016-12-30
Modified: 2016-12-30
Slug: ssh-host-key-identification
Authors: imjang57
Summary: This is about SSH Host-key identification.
Tags: SSH

# SSH host key

가끔 SSH Client 로 Remote 에 있는 SSH Server 에 접속할 때 아래와 같은 에러를 볼 수 있다.

```
imjang57@myserver:~$ ssh administrator@192.168.0.5
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@ WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!              @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle
attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
bf:e3:d3:21:c4:3c:60:cd:d9:2b:bb:a4:d1:6e:1f:df.
Please contact your system administrator.
Add correct host key in /home/imjang57/.ssh/known_hosts to get rid of
this message.
Offending ECDSA key in /home/imjang57/.ssh/known_hosts:8
  remove with: ssh-keygen -f "/home/imjang57/.ssh/known_hosts" -R
192.168.0.5
ECDSA host key for 192.168.0.5 has changed and you have
requested strict checking.
Host key verification failed.
```

_Host Key_ 가 달라서 발생하는 문제다. 자세히 말하면, 클라이언트 측에 등록된 SSH 서버의 호스트 키가 현재 접속 시도하면서 새롭게 받은 호스크 키와 달라서 발생한 문제이다.

SSH 서버에서 호스트 키를 새롭게 생성했거나, 클라이언트 측에서 SSH 서버의 호스트 키를 수동으로 입력했는데 잘못입력했거나, 서버를 재설치했거나, 기타 등등의 이유로 기존에 저장된 호스트 키와 연결시도하면서 새롭게 받은 호스트 키가 다를 수 있다.

이는 SSH 연결을 시도하는 서버가 정말 내가 연결하려는 서버가 맞는지를 체크할 수 있는 기능이다. HTTPS 를 사용할 때 신뢰할 수 있는 사이트인지 확인하는 것과 비슷한 이유로 제공되는 기능이다.

## 해결 방법

해결하는 방법은 여러개가 있다.

### known_host 삭제하여 해결

보통 사용자의 홈 디렉터리에 .ssh 라는 디렉터리가 있고, 여기에 사용자를 위한 SSH 설정이나 사용자 인증을 위한 키 파일이 저장된다. 그리고 <user_home>/.ssh 디렉터리 밑에 known_hosts 라는 파일이 있는데 여기에 SSH 서버의 호스트 키들이 저장되어 있다. 여기서 에러가 나는 SSH 서버의 호스트 키를 삭제하면 다시 연결할 수 있다.

```
ssh-keygen -f "/home/imjang57/.ssh/known_hosts" -R 192.168.0.5
```

위 명령으로 저장된 서버의 호스트 키를 삭제한 후 SSH 서버에 다시 접속하면 아래와 같이 호스트 키를 등록하냐고 물어보는 메시지가 나타난다.

```
imjang57@myserver:~$ ssh administrator@192.168.0.5
The authenticity of host '192.168.0.5' can't be established.
ECDSA key fingerprint is
bf:e3:d3:21:c4:3c:60:cd:d9:2b:bb:a4:d1:6e:1f:df.
Are you sure you want to continue connecting (yes/no)?
```

yes 를 입력하면 호스트 키를 <user_home>/.ssh/known_hosts 파일에 저장하고 SSH 접속하게 된다.

만약 명령어 치는게 귀찮으면 그냥 known_hosts 파일 삭제하면 된다.

### StrictHostKeyChecking 설정을 off 하여 해결

리눅스에서 ssh 설정은 보통 `/etc/ssh` 디렉터리에 있다. `ssh_config` 파일은 클라이언트 설정 파일, `sshd_config` 는 서버(데몬) 설정 파일이다.

`ssh_config` 파일에서 아래 내용을 찾아서 호스트 키 검사를 하지 않도록 설정하면 된다.

```
StrictHostKeyChecking no
UserKnownHostsFile=/dev/null
```

## 호스트 키 새로 생성하는 방법

서버를 운영하는 입장에서 서버를 추가할 때 기존 서버의 이미지를 사용해서 새로운 서버를 구성할 수 있다. 이 때 호스트 키를 새롭게 생성해야 한다.

호스트 키는 보통 `/etc/ssh` 에 저장되어 있다. _RSA_, _DSA_, _ECDSA_ 세 가지 종류의 키 파일들이 보통 생성되어 있다.

새로 호스트 키를 생성하기 위해 아래 명령을 실행해서 세 가지 종류의 호스트 키 파일들을 생성하면 된다.

```
sudo ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa
sudo ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa
sudo ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa -b 521
```

기존에 파일들이 있으면 overwrite 할 거냐고 묻는데 당연히 `y` 를 입력하자.
