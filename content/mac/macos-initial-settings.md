Title: MacOS initial settings
Date: 2017-12-19
Modified: 2017-12-19
Tags: mac, macos
Slug: macos-initial-settings
Authors: imjang57
Summary: MacOS에서 가장 처음에 하는 환경설정 내용을 요약

# Mac Development Environment

Keyboard notation examples :

- `Control + b, c`는 `Control` 키를 누른 상태에서 `b`를 누르고, `Control` 키와 `b`에서 손을 뗀 후 `c`를 눌러라는 의미
- `Control + b, Control + c`는 `Control` 키를 누른 상태에서 `b`를 누르고, `b`에서 손을 뗀 후 `c`를 눌러라는 의미

## System Preferences

언어 우선순위를 영어, 한국어 순서로 변경 :

- `Language & Region` > `Preferred languages` : English > 한국어 (드래그로 순서 조정)
- locale 설정 때문에 오류가 발생하는 걸 방지
- 영어 에러가 구글검색이 잘됨

보안 설정 :

- `Security & Privacy` > `General` > `Require password` : select `immediately`
- `Security & Privacy` > `General` > `Show a message when the screen is locked` : input phone number, name, etc

Keyboard :

- `Keyboard` > `Text` : disable all automatic and smart options

Trackpad :

- `Trackpad` > `Point & Click` > `Tab to click` : Enable
- `Accessibility` > `Mouse & Trackpad` > `Trackpad options...` : check `Enable dragging` > select `three finger drag`

Dark menu bar :

- `General` > `Use dark menu bar and Dock` : Enable

Scroll bar :

- `General` > `Show scroll bars` : select `Always`

Screen Saver:

- `Desktop & Screen Saver` > `Screen Saver` > Start after : `10 Minutes`

## Finder Preferences

- `General` > `New Finder windows show` : your home directory
- `Advanced` > `Show all filename extensions` : Enable
- `Sidebar` > `Favorites` > check your home directory and others you want to add sidebar

## Install Magnet

- web site : http://magnet.crowdcafe.com

My Key settings:

- `Control + Option + h` : Left
- `Control + Option + j` : Up
- `Control + Option + k` : Down
- `Control + Option + l` : Right
- `Control + Option + u` : Top Left
- `Control + Option + i` : Top Right
- `Control + Option + m` : Bottom Left
- `Control + Option + ,` : Bottom Right
- `Control + Option + y` : Left Two Third
- `Control + Option + o` : Right Two Third
- `Control + Option + c` : Cender
- `Control + Option + Enter` : Maximize
- `Control + Option + Delete` : Restore
- Disable others

## Install Xcode Command Line Tools

Xcode를 설치해야 gcc 등의 개발 도구를 사용할 수 있다. Xcode 전체를 설치할 필요가 없다면 Xcode Command Line Tools만 따로 설치할 수도 있다.

```
> xcode-select --install
```

참고로 Mac 에서는 gcc가 아니라 llvm을 사용한다. `gcc` 명령을 실행하면 실제로는 llvm의 C언어 front-end인 `clang` 명령이 실행된다.

## Install Homebrew

- web site : https://brew.sh
- GitHub : https://github.com/Homebrew/brew/

Homebrew는 Mac에서 패키지 설치와 관리를 쉽게 해주는 도구이다. 다양한 개발 도구들을 쉽게 구성할 수 있다.

```
> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" 
> brew help
> brew cask
```

## Install packages

```bash
$ brew install git vim python3 node@8 wget maven
$ brew cask install iterm2 sublime-text google-chrome evernote java slack intellij-idea-ce docker
```

## 맥북 터치바 모델일 경우

- `System Preferences` - `Keyboard` > `Shortcuts` > `Function Keys` > `iTerm.app` 및 `Sublime Text.app` 등 추가
