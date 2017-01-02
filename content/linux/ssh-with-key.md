Title: SSH with key
Date: 2017-01-02
Modified: 2017-01-02
Tags: linux, ssh, key-gen
Slug: ssh-with-key
Authors: imjang57
Summary: Key 로 SSH 로그인 하기 위한 과정

# SSH with key file

SSH 를 사용할 때 비밀번호를 일일이 입력하기 귀찮을 때가 있다. 특히 개발용 서버에 수시로 접속할 때.. 이 때 key 파일을 이용한 로그인을 하면 비밀번호를 입력하는 번거로움을 피할 수 있다.

SSH 에서 key 를 이용한 로그인을 위해 RSA asymmetric encryption (RSA 비대칭키 암호화) 방식을 이용할 수 있다. 이 방법은 아래와 같은 절차를 따라 동작한다. (물론 당연히 다른 암호화 방식의 Key 를 사용해도 된다.)

1. Public Key (공개키) 와 Private Key (비공개키) 를 생성
2. Local Host (SSH Client) 에 Private Key 저장
3. Remote Host (SSH Server) 에 Public Key 등록
4. Local Host 가 Remote  Host 에 접속 요청을 하면서 Public Key 전달
5. Remote Host 는 Public Key 를 받아서 등록된 Public Key 인지 검사한 후 승인 또는 비승인

## Key 생성

먼저 Public Key 와 Private Key 를 생성한다. 리눅스에서는 아래와 같은 명령을 실행하면 된다.

```
$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/axl/.ssh/id_rsa): <return>
Enter passphrase (empty for no passphrase): <Type the passphrase>
Enter same passphrase again: <Type the passphrase>
```

`ssh-keygen` 을 실행하면 key file 이 저장될 위치와 passphrase 를 차례대로 묻는다. 저장될 위치는 기본값으로 `$HOME/.ssh` 이다. 특별히 변경할 일이 없다면 그대로 엔터를 입력하여 기본값으로 사용하자. passphrase 는 비공개키를 생성하는데 사용될 문자열로 이 문자열을 암호화하여 키를 생성한다. 자동 로그인을 원한다면 생략해야 한다.

키가 정상적으로 생성되면 키가 생성된 곳에 아래와 같은 파일들을 볼 수 있다. 참고로 파일들은 SSH 를 사용할 때 보안에 매우 중요한 파일들이다.

```bash
drwx------  2 ubuntu ubuntu 4096 Feb 18 18:54 .
drwxr-xr-x 16 ubuntu ubuntu 4096 Mar  1 06:02 ..
-rw-rw-r--  1 ubuntu ubuntu  790 Feb 19 06:04 authorized_keys
-rw-------  1 ubuntu ubuntu 1675 Feb 18 18:51 id_rsa
-rw-r--r--  1 ubuntu ubuntu  395 Feb 18 18:51 id_rsa.pub
-rw-r--r--  1 ubuntu ubuntu 2216 Feb 19 18:34 known_hosts
```

`authorized_keys` 파일은 없을수도 있다. `id_rsa` 파일은 private key 이다. 매우 중요하므로 절대로 타인에게 노출되면 안된다. `id_rsa.pub` 파일은 public key 이다. 접속하려는 Remote Host 의 `authorized_keys` 에 입력한다. `authorized_keys` 파일은 Remote Host 의 `.ssh` 디렉토리 아래에 위치하면서 `id_rsa.pub` 키의 값을 저장한다.

## Remote Host 에 Public Key 등록

이제 `id_rsa.pub` 파일을 리모트 서버의 `$HOME/.ssh/authorized_keys` 파일에 추가해줘야 한다. SSH Server의 `authorized_keys` 의 내용이 SSH Client의 `id_rsa.pub` 파일과 같아야 한다.

아래와 같이 SCP (Secure Copy) 를 이용하여 Public Key 를 Remote Host 에 복사한다.

```bash
scp $HOME/.ssh/id_rsa.pub root@server.net:id_rsa.pub
```

그리고 Public Key 를 Remote Host 의 authorized_keys 에 추가한다.

```bash
cat $HOME/id_rsa.pub >> $HOME/.ssh/authorized_keys
```

## SSH 접속

이후에는 비밀번호 없이 바로 SSH 접속이 가능하다.

만약 Private Key 를 다른 곳에 저장했다면 아래와 같이 `-i` 옵션을 사용하여 키를 지정할 수 있다.

```bash
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
