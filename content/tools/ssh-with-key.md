Title: SSH with key
Date: 2017-01-02
Modified: 2017-01-02
Tags: ssh, key-gen
Slug: ssh-with-key
Authors: imjang57
Summary: Key 로 SSH 로그인 하기 위한 과정

# SSH with key file

SSH를 사용할 때 비밀번호를 일일이 입력하기 귀찮을 때가 있다. 특히 개발용 서버에 수시로 접속할 때... 이 때 키(Key) 파일을 이용한 로그인을 하면 비밀번호를 입력하는 번거로움을 피할 수 있다. 또한, 비밀키(Private Key) 를 잘 관리하여 SSH 접속에 대한 보안을 강화할 수도 있다. 물론 모든 보안이 그렇듯이 얼마나 비밀키를 잘 관리하느냐가 중요하다.

SSH에서 키를 이용한 로그인을 위해 키파일(Key file)을 생성하고 SSH 서버에 키의 정보를 등록해주어야 한다. 키를 생성할 때 여러 암호화 알고리즘을 사용할 수 있지만 보통 RSA 비대칭키 암호화(RSA asymmetric encryption) 방식을 많이 사용한다. RSA 키파일을 생성하고 이 키를 이용하여 SSH 로그인하기 위해 다음과 같은 과정이 필요하다.

1. 공개키(Public Key) 와 비밀키(Private Key) 를 생성
2. 로컬 호스트(Local Host), 즉 SSH 클라이언트(SSH Client)에 비밀키를 저장
3. 원격 호스트(Remote Host), 즉 SSH 서버(SSH Server)에 공개키를 등록

SSH 접속이 진행되는 과정을 살펴보면 다음과 같다.

1. SSH 클라이언트가 SSH 서버 측에 접속 요청
2. SSH 서버는 자신의 공개키(위에서 생성한 키가 아니라 원래 SSH 서버가 가지고 있는 키)를 SSH 클라이언트에게 전달
3. SSH 클라이언트는 SSH 서버가 전달한 공개키로 자신의 비밀키를 암호화하여 SSH 서버에게 전달
4. SSH 서버는 자신이 가진 공개키 목록을 보고 SSH 클라이언트가 전달한 비밀키와 매칭되는 공개키가 있으면 로그인을 승인

위에서 언급한 대로 로그인 과정에서는 비대칭키를 사용한다. 하지만 로그인이 성공한 이후에는 대칭키를 만들고, 비대칭키로 생성된 대칭키를 공유하고, 이후 데이터 전송에는 이 대칭키(Symmetric key)를 사용한다. 비대칭키는 연산이 더 오래걸리기 때문이다.

## Key 생성

먼저 Public Key 와 Private Key 를 생성한다. 리눅스에서는 아래와 같은 명령을 실행하면 된다.

```
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/axl/.ssh/id_rsa): <return>
Enter passphrase (empty for no passphrase): <Type the passphrase>
Enter same passphrase again: <Type the passphrase>
```

`ssh-keygen` 을 실행하면 key file 이 저장될 위치와 passphrase 를 차례대로 묻는다. 저장될 위치는 기본값으로 `$HOME/.ssh/` 이다. 특별히 변경할 일이 없다면 그대로 엔터를 입력하여 기본값으로 사용하자. `passphrase` 는 비밀키를 생성하는데 사용될 문자열로 이 문자열을 암호화하여 키를 생성한다. 자동 로그인을 원한다면 생략해야 한다.

키가 정상적으로 생성되면 키가 생성된 곳에 아래와 같은 파일들을 볼 수 있다. 참고로 아래 파일들은 SSH 를 사용할 때 보안에 매우 중요한 파일들이다.

```bash
drwx------  2 ubuntu ubuntu 4096 Feb 18 18:54 .
drwxr-xr-x 16 ubuntu ubuntu 4096 Mar  1 06:02 ..
-rw-rw-r--  1 ubuntu ubuntu  790 Feb 19 06:04 authorized_keys
-rw-------  1 ubuntu ubuntu 1675 Feb 18 18:51 id_rsa
-rw-r--r--  1 ubuntu ubuntu  395 Feb 18 18:51 id_rsa.pub
-rw-r--r--  1 ubuntu ubuntu 2216 Feb 19 18:34 known_hosts
```

`authorized_keys` 파일은 없을수도 있다. 보통 SSH 서버 측에서 접속을 허용할 공개키 정보를 저장하는 파일이다. `id_rsa` 파일은 비밀키를 저장한 파일이다. 매우 중요하므로 절대로 타인에게 노출되면 안된다. 또한, 함부로 수정되어서는 안되므로 파일 권한을 꼭 600으로 지정해주자. `id_rsa.pub` 파일은 공개키를 저장한 파일이다. 접속하려는 원격 호스트의 `authorized_keys`에 `id_rsa.pub`파일에 저장된 공개키를 추가해야 키를 이용한 로그인을 할 수 있다.

## Remote Host 에 Public Key 등록

이제 `id_rsa.pub` 파일을 리모트 서버의 `$HOME/.ssh/authorized_keys` 파일에 추가해줘야 한다. SSH Server의 `authorized_keys` 의 내용이 SSH Client의 `id_rsa.pub` 파일과 같아야 한다.

아래와 같이 SCP (Secure Copy) 를 이용하여 Public Key 를 Remote Host 에 복사한다.

```
scp $HOME/.ssh/id_rsa.pub root@server.net:id_rsa.pub
```

그리고 Public Key 를 Remote Host 의 authorized_keys 에 추가한다.

```
cat $HOME/id_rsa.pub >> $HOME/.ssh/authorized_keys
```

## SSH 접속

이후에는 비밀번호 없이 바로 SSH 접속이 가능하다.

만약 Private Key 를 다른 곳에 저장했다면 아래와 같이 `-i` 옵션을 사용하여 키를 지정할 수 있다.

```
$ ssh root@server.net -i keyfile
```

## Remote Host 의 SSHD 설정

Key 를 이용한 SSH 로그인을 사용하기 위해서는 Remote Host 의 SSHD 설정에서 RSA 키 인증을 사용하도록 설정해야 한다. 아래와 같은 내용이 있는지 SSHD 설정 파일 (`/etc/ssh/sshd_config`) 을 확인한다.

```
RSAAuthentication yes
#DSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
```
