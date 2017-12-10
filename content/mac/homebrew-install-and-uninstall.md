Title: HomeBrew Install And Uninstall
Date: 2016-12-31
Modified: 2016-12-31
Tags: mac, homebrew, brew, brew cask
Slug: homebrew-install-and-uninstall
Authors: imjang57
Summary: HomeBrew 를 설치하고 삭제하는 방법

# HomeBrew

HomeBrew 는 OS X (이제는 MacOS) 에서 패키지 관리를 자동으로 해주는 도구이다. 이 글을 쓸 때는 최신 버전이 1.1.5 이다.

HomeBrew 를 설치하려면 "_Command Line Tools (CLT) for Xcode_"가 필요하다. 귀찮으니 그냥 Xcode 설치하자. Xcode 에 다 포함되어 있다.

## Install

[Homebrew Github Project](https://github.com/Homebrew)에 가면 [install repository](https://github.com/Homebrew/install) 가 있다. 여기에 `install` 과  `uninstall` 이라는 스크립트를 제공해서 HomeBrew 를 설치하고 삭제할 수 있게 해준다.(Bash 는 아니고 Ruby 인 듯)

`install` 스크립트로 설치하려면 아래와 같이 실행하면 된다.

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

위 스크립트로 설치하면 `/usr/local` 에 HomeBrew 가 설치된다. 그런데 이 때 HomeBrew 를 위한 local git repository (`.git` 디렉터리) 도 `/usr/local` 에 생기고 다른 라이선스 관련 파일 등도 여기에 생성된다.. 이건 좀.. 그래서 uninstall 스크립트로 삭제하면 깨끗하게 지워지니까 일단 넘어가자. 이게 정 마음에 안들면 [installation guide](https://github.com/Homebrew/brew/blob/master/docs/Installation.md#installation) 를 참고해서 직접 `git clone` 해서 설치하자.

`install` 스크립트로 실행하면 아래와 같이 설치되는 목록들을 보여준다.

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew
==> The following new directories will be created:
/usr/local/Cellar
/usr/local/Homebrew
/usr/local/Frameworks
/usr/local/include
/usr/local/opt
/usr/local/sbin
/usr/local/share/zsh
/usr/local/share/zsh/site-functions
/usr/local/var
```

## Uninstall

설치때와 마찬가지로 [install repository](https://github.com/Homebrew/install)에서 제공하는 `uninstall` 스크립트를 실행하면 된다.

```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
Warning: This script will remove:
/Library/Caches/Homebrew/
/Users/youngho/Library/Logs/Homebrew/
/usr/local/.git/
/usr/local/.gitignore
/usr/local/.travis.yml
/usr/local/.yardopts
/usr/local/CODEOFCONDUCT.md
/usr/local/CONTRIBUTING.md
/usr/local/Cellar/
/usr/local/LICENSE.txt
/usr/local/Library/
/usr/local/README.md
/usr/local/SUPPORTERS.md
/usr/local/bin/brew
/usr/local/share/doc/homebrew/
/usr/local/share/man/man1/brew.1
Are you sure you want to uninstall Homebrew? [y/N]
```

## Usage

사용법은 매우 쉬우니 대충 적고 넘어간다.

실행 명령어는 `brew` 이다.

```bash
$ which brew
/usr/local/bin/brew
```

brew man page 에 더 자세한 내용이 많으니 참고하자.

```bash
$ man 1 brew
```

주로 사용하는 명령들의 목록:

- `brew help`
- `brew config`
- `brew list [FORMULA...]`
- `brew info [FORMULA...]`
- `brew search <TEXT|/REGEX/>`
- `brew install FORMULA...`
- `brew uninstall FORMULA...`
- `brew upgrade [FORMULA...]`

HomeBrew 자체를 업그레이드하려면 `brew update` 명령을 실행하면 되는데 지금은 잘 되는지 모르겠다. 0.9 버전일 사용할 때 _El Capitan_ 되면서 _System Integrity Protection_ 이라는 기능이 생겨서 제대로 안됐었는데, 맥 복구 모드(recovery mode)로 부팅해서 기능을 끄고 해서 해결했었던가 기억이 잘 안난다. 나중에 업데이트 할 일 생기면 다시 시도해보자.

# Brew Cask

`brew-cask`는 `brew`를 기반으로 확장한 프로그램이다. `brew`처럼 패키지를 관리하는 것을 목표로 한다.

`brew`는 소스 코드를 직접 빌드하는 방법을 사용하지만 `brew-cask`는 바이너리를 직접 받아서 설치하고 필요한 설정들을 자동으로 세팅한다. 이는 `brew-cask`의 목적이 일반적으로 맥에서 애플리케이션을 설치할 때 사용하는 방법인 Drag-and-Drop 방법을 대체하기 위한 방법이기 때문이다. 때문에 `brew-cask`는 소스 코드가 공개되지 않은 상용 프로그램들의 설치도 가능하다.

## Install

`brew-cask` 설치는 아래와 같이 `brew`를 실행하면 된다.

```bash
$ brew tap caskroom/cask
```

## Usage

`brew-cask`로 맥의 터미널 앱인 iTerm2를 설치하려면 아래와 같이 실행하면 된다.

```bash
$ brew cask install iterm2
```

`brew-cask`로 크롬도 설치되고 왠만한 유명한 프로그램은 다 설치 가능하다.

# References

- [HomeBrew Web](http://brew.sh)
- [HomeBrew Github](https://github.com/Homebrew/brew)

