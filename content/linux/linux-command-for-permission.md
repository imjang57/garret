Title: Linux 에서 사용자 권한 관리
Date: 2017-01-01
Modified: 2017-05-08
Tags: linux, permission
Slug: linux-command-for-permission
Authors: imjang57
Summary: Linux 에서 사용자 권한 관리에 대한 글

# permissions

보통 Linux syste 에는 root 라는 사용자가 있는데, 이는 Linux system 에서 가장 높은 권한을 가진 사용자이며 대부분의 리눅스 배포판(Linux distribution)에서 기본적으로 제공되는 username 이다. 물론 요즘은 Mac 이나 Ubuntu 처럼 root 를 제공하지 않고 관리자 권한을 가진 계정을 제공하기도 한다. 어쨌든 관리자 권한을 갖고 시스템 전체에 접근하고 변경할 수 있도록 설정된 사용자가 존재한다.

이 외의 일반 사용자들은 제한된 권한으로 시스템을 사용하게 되는데 설정에 따라 어떤 사용자들은 잠시 최상위 권한을 얻을 수 있다. 최상위 권한을 얻을 수 있도록 설정된 사용자는 `sudo` 라는 명령어를 통해 이 권한을 얻을 수 있으며, 이 설정은 `/etc/sudoers` 라는 파일을 통해서 관리된다.

# sudo

`sudo` 는 일반사용자가 루트 권한을 임시적으로 획득하여 특정 명령을 할 수 있도록 하는 명령어이다. substitute user do 를 줄인 단어로, 다른 사용자의 권한으로 명령을 이행하라는 뜻이다

`sudo` 의 man pages 에는 다음과 같이 설명한다:

> sudo — execute a command as another user
> sudo allows a permitted user to execute a command as the superuser or another user, as specified by the security policy.
> The default security policy is sudoers, which is configured via the file /etc/sudoers

일반사용자가 `sudo` 명령어를 사용하기 위해서는 `/etc/sudoers` 파일이나 `/etc/sudoers.d/<filename>` 에 등록되어 있어야 한다.

# 사용자에게 sudo 권한 추가

우분투는 기본적으로 root 계정을 사용하지 못하게 하고, root 계정이 필요한 경우 sudo 명령을 통해서 root 가 아닌 계정에서 명령을 실행할 수 있도록 되어있다.

그런데 아무 계정에서나 `sudo` 명령을 실행할 수 있는 것은 아니다. 기본적으로는 admin 이라는 group 에 계정이 속해있어야 가능하다(group 이름이 admin 이 아닐 수도 있지만 어쨌든 관리자들을 위한 group 이 대부분 존재한다).

이 글에서는 admin 이 아닌 다른 그룹에 계정을 생성했을 때, `sudo` 명령어를 사용할 수 있도록 설정하는 법을 적었다.

관리자 권한은 `/etc/sudoers` 파일에서 관리되는데 이 파일은 쓰기 권한이 없다. 이 파일을 수정하기 위해서는 2가지 방법이 있다.

1. `visudo` 명령어를 실행하여 수정하는 방법
2. `/etc/sudoers` 파일에 임시로 쓰기 권한((`chmod +w /etc/sudoers`)을 추가한 다음 수정 후 다시 원래 권한(`chmod 440 /etc/sudoers`)으로 되돌리는 방법

임의로 권한을 변경하는 것은 위험한 작업이므로 `visudo` 를 이용하는 것이 좋다.

먼저 `sudo` 설정 파일(`/etc/sudoers`)을 수정하기 위해 아래와 같이 입력한다:

```
$ sudo visudo
```

또는 `/etc/sudoers` 파일의 권한을 쓰기를 추가한 다음(chmod +w /etc/sudoers) 작업을 끝낸 후 다시 440 모드(chmod 440 /etc/sudoers)로 바꿔줘도 괜찮다.

/etc/sudoers 파일에 아래와 같은 내용을 추가한다:

```
# 특정 사용자에게 sudo 권한을 허락하는 경우
userid ALL=(ALL:ALL) ALL
# 특정 그룹에 sudo 권한을 허락하는 경우
%groupid ALL=(ALL) ALL
```

아래와 같이 입력하면 `sudo` 실행 시 패스워드를 생략할 수 있다:

```
%groupname ALL=(ALL) NOPASSWD: ALL
```

# sudo 명령 시 특정 환경변수를 유지하도록 설정하는 법

예를 들어, HTTP Proxy 를 사용하는 환경에서 `sudo` 를 이용하여 HTTP 요청을 하면 정상적으로 동작하지 않는 경우가 있다:

```
$ sudo curl http://www.host.com
```

이는 `http_proxy` 라는 환경변수가 sudo shell environment 에 없기 때문이다. 아래와 같이 명령을 입력하면 `sudo` 로 실행되는 환경에서는 `http_proxy` 가 없음을 알 수 있다.

```
$ sudo env
```

이를 해결하기 위해서는 `/etc/sudoers` 에 특정 환경변수를 유지하도록 설정해주어야 한다.

아래 명령으로 `/etc/sudoers` 파일을 열자:

```
$ sudo visudo
```

그리고 아래와 같은 라인을 추가하자:

```
Defaults env_keep += "http_proxy https_proxy"
```

# /etc/sudoers 파일이 잘못되어서 sudo 명령이 되지 않을 때

`sudo` 권한을 관리하기 위해 `/etc/sudoers` 파일을 수정하다보면 실수로 파일이 깨지거나 문법에 맞지 않게 설정할 때도 있다. 이러면 아무리 `sudo` 명령을 때려도 `/etc/sudoers` 파일 parse error 라면서 아래와 같은 메시지를 던지게 된다.

```
"/private/etc/sudoers: syntax error near line 28
sudo: parse error in /private/etc/sudoers near line 28
sudo: no valid shudders sources found, quitting
```

이 경우 root 로 로그인 하여 해당 파일을 수정하면 해결할 수 있다. 하지만, Ubuntu 의 경우 기본적으로 root 의 password 가 설정되어 있지 않기 때문에 별도로 root 를 활성화한 경우가 아니라면 낭패를 보기 쉽다.

이 때, `pkexec` 를 이용하여 `/etc/sudoers` 파일을 수정할 수 있다.

## __pkexec__

`pkexec` 의 man pages 에 다음과 같이 설명되어 있다.

> pkexec allows an authorized user to execute PROGRAM as another user. If username is not specified, then the program will be executed as the administrative super user, root.

즉, `pkexec` 를 이용하면 `root` 사용자로 실행할 수 있다:

```
pkexec vi /etc/sudoers
```

위 명령으로 `/etc/sudoers` 파일을 수정하면 root 가 비활성화된 Ubuntu에서도 해결가능하다.
