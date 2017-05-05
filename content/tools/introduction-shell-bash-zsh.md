Title: Shell, Bash, Zsh
Date: 2016-12-31
Modified: 2016-12-31
Tags: shell, bash, zsh
Slug: introduction-shell-bash-zsh
Authors: imjang57
Summary: 내가 사용하는 Shell 에 대한 소개와 설치 과정

# Shell

_Shell_ 은 _OS_ (_Operating System_) 가 제공하는 여러 서비스들을 사용하기 위한 User interface 를 말한다. _CLI_ (_Command-line interface_) 도 _Shell_ 이고 _GUI_ (_Graphical User Interface_) 도 _Shell_ 이다.

_Linux_ 와 _OS X_ 에서는 보통 _Bash_ 가 Default shell 로 제공된다. 이 외에 _csh_, _ksh_, _zsh_ 등 많은 _Shell_ 들이 있다.

요즘 가장 많이 사용되는 Linux 와 OS X  에서 Default shell 이고 수 많은 shell script 들이 _Bash_ 를 기반으로 작성되기 때문에 _Bash_ 는 필수이다. 여기에 나는 개인적으로 사용되는 환경에서는 _Zsh_ 을 추가로 설치해서 사용한다.

이 _Shell_ 들은 마음에 드는 프롬프트를 만들고, 자주 사용하는 명령들을 alias 하고, 환경변수를 지정해서 사용하는 등 개인 취향에 따라 customizing 할 수 있다. 그래서 이 글에 내가 사용하는 Bash 설정과 Zsh 을 설치하고 설정하기 위한 과정들을 남긴다.

## Shell 확인 및 변경

_Shell_ 확인은 다음과 같이 가능하다.

- 현재 내가 사용중인 Shell 확인 : `echo $SHELL`
- System 에서 사용가능한 Shell 목록 확인 : `cat /etc/shells`

만약 내가 사용 중인 Shell 을 변경하고 싶다면 `chsh -s /path/to/other/shell` 를 실행하면 된다.

```bash
$ chsh -s /usr/local/bin/zsh
```

## Shell 의 실행 형태

_Shell_ 의 실행 형태는 _Interacctive shell_ 과 _Non-interactive shell_ 2가지가 있다. _Interactive shell_ 은 사용자가 명령을 입력하고 이를 실행하는 형태의 _Shell_ 이고 _Non-interactive shell_ 은 Script 를 실행할 때 사용되는 형태이다. 그리고 _Interactive shell_ 은 _Login shell_ 과 _Non-login Shell_ 이 있다. _Shell_ 은 실행 형태에 따라 사용자가 로그인할 때, 로그아웃할 때 각각 수행되는 스크립트들이 있다.

_Bash_ 의 경우를 예로 살펴보자. _Interactive Login Shell_ 일 경우 로그인할 때는 `/etc/profile` 이 먼저 실행되고 `~/.bash_profile`, `~/.bash_login`, `~/.profile` 들 중 처음 나오는 1개가 실행되다. 로그아웃할 때는 `~/.bash_logout` 을 실행한다. _Interactive Non-login Shell_ 일 경우 `~/.bashrc` 가 실행된다. _Non-interactive shell_ 은 $BASH_ENV (script 를 sh 로 실행한 경우는 $ENV) Environment variable 을 찾아서 이 변수에서 지정하는 파일 내의 명령들을 실행한다. 대부분의 경우 System-wide environment variables 는 `/etc/profile` 에 설정하고, 각 사용자가 필요한 내용은 `~/.bash_profile` 에서 설정한다.

_Zsh_ 은 `/etc/profile` 대신 `/etc/zprofile`, `~/.bash_profile` 대신 `~/.zprofile`, `~/.bashrc` 대신 `~/.zshrc` 를 사용한다.

## Prompt

_Interactive Shell_ 이 실행된 경우 사용자의 입력을 기다리고 있음을 나타내기 위해 `<username@hostname>` 과 같은 내용을 표시하는데 이를 Prompt 라고 한다. 이 프롬프트는 $PS1 환경 변수에 의해 설정된다. 만약 `export PS1="\$? > "` 를 실행하면 프롬프트는 `0 > ` 와 같이 출력된다. 숫자 0은 이전 명령에 대한 리턴값이다.

나는 bash prompt 를 다음과 같이 설정해서 사용한다.

```bash
# Colorize bash prompt using ANSI escape codes.
#     below print : username@hostname:cwd $
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
```

## alias

`alias` 명령을 사용하면 긴 명령이나 자주 사용하는 명령을 내가 원하는 명령으로 지정할 수 있다. `alias ll='ls -GFhil'` 을 실행하면 이후부터 `ll` 을 입력했을 때 `ls -GFhil` 가 실행된다.

내가 주로 사용하는 `alias`:

```
alias ll='ls -GFhil'
alias lt='ls -altr'
alias vi='vim'
ssh='ssh -o StrictHostKeyChecking=no -t'
```

# Bash

_Bash_ 는 최초의 _Shell_ 인 Bourne shell 을 다시 만든 _Shell_ 로 Bourne-again Shell 을 줄여서 _Bash_ 라고 한다. Linux 와 OS X 에는 Default shell 이며 다른 Unix 에서는 Csh 을 쓰는 듯 하다.

요즘 대부분 개발자들이 사용하는 환경은 Linux, OS X, Windows 라서 _Bash_ 는 따로 설치해본 적이 없다. Linux 와 OS X 응 Default shell 이고 Windows 는 Bash 안쓰니까.. 그러니까 _Bash_ 에 대한 얘기는 넘어가자.

# Zsh

_Zsh_ 은 _Bash_ 의 확장판 같은 거라고 한다(그렇다고 함..). 사실 _Zsh_ 을 사용하는 이유는 _oh-my-zsh_ 때문이다. _Zsh_ 자체도 (자기들 주장에는) 좋다고 하는데 사실 나는 _Bash_ 와 비교해서 딱히 뛰어난 걸 잘 못느꼈다. 게다가 대부분의 Shell script 는 _Bash_ 를 기준으로 하기 때문에 _Zsh_ 이 아무리 _Bash_ 와 호환된다 해도 사용할 이유를 느끼지 못했었다. _oh-my-zsh_ 이 없었으면 아마 사용 안했을 듯 하다.

## Zsh + oh-my-zsh 설치 및 설정

zsh 설치는 `yum install zsh`, `apt-get install zsh`, `brew install zsh` 중 자기 OS 에 맞는 걸로 사용해서 설치하자. zsh 소스를 받아서 컴파일 하여 설치하는 것은 [Zsh Homepage](http://www.zsh.org) 가서 알아보자.

이제 oh-my-zsh 을 설치하자. [oh-my-zsh github](https://github.com/robbyrussell/oh-my-zsh) 에 설명이 잘 나와있으니 자세한 내용은 가서 읽어보자. 나는 curl 을 이용해서 설치했다.

```bash
$ curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh
```

위 명령을 실행하면 git repository 가 ~/.oh-my-zsh 디렉터리에 clone 되고 설치 작업이 수행된다. 그리고 ~/.zshrc 파일이 자동으로 생성된다.

설치는 이렇게 쉽게 끝났고, oh-my-zsh 은 다양한 theme plugin 을 지원하므로 내가 원하는 theme 를 적용해보자. 나는 [agnoster](https://gist.github.com/agnoster/3712874) theme 가 마음에 들어서 아래와 같이 ~/.zshrc 파일을 변경하였다.

```
ZSH_THEME="agnoster"
```

변경 후 `~/.zshrc` 파일을 다시 적용하면 theme 가 적용된다. 만약 `ZSH_THEME="random"` 으로 하면 여러 테마들이 로그인할 때마다 랜덤으로 적용된다.

agnoster 테마는 Powerline font 를 필요로 한다. 이 폰트는 [Powerline github](https://github.com/powerline/fonts) 에서 받을 수 있다. 이 저장소를 clone 한 후 `install.sh` 파일을 실행하면 알아서 폰트를 설치해준다.

OS X 의 경우 터미널 앱의 환경설정으로 가서 테마에서 서체를 새로 설치한 _Meslo LG M for Powerline_ 으로 바꿔주자.

