Title: iTerm2
Date: 2017-12-18
Modified: 2017-12-18
Tags: mac, iterm2, terminal
Slug: iterm2
Authors: imjang57
Summary: iTerm2 설치 및 사용법

# iTerm2

iTerm2 는 맥에서 가장 많이 사용되는 터미널(Terminal) 프로그램이다.

## Installation

iTerm2 에서 제공하는 공식 바이너리로 쉽게 설치할 수도 있지만 나는 왠만하면 모든 패키지들을 `brew`로 관리하기를 원해서 `brew-cask`로 설치했다.

```bash
$ brew cask install iterm2
```

## Configuration

내가 사용하는 환경을 위한 설정들을 해보자.

- `Preferences(cmd + ,)` => `Profiles` => `Colors` => `spacegray`
- `Preferences(cmd + ,)` => `Profiles` => `Text` => `Font` => `Change Font` => 13pt, Meslo LG M Regular for Powerline
- `Preferences(cmd + ,)` => `Profiles` => `Window` => `Window Appearance` => `Transparency`
- `Preferences(cmd + ,)` => `Profiles` => `Window` => `Settings for New Windows` => `Columns` : 200, `Rows` : 50
- `Preferences(cmd + ,)` => `Profiles` => `Terminal` => `Scrollback Buffer` => check `Unlimited scrollback`

참고:

- spacegray theme : https://github.com/ajh17/Spacegray.vim
- powerline font : https://github.com/powerline/fonts

## Key Mappings

자주 사용하는 단축키들은 다음과 같다.

- 새 창 : `Command + n`
- 새 탭 : `Command + t`
- 탭 닫기 : `Command + w`
- 전체 창 전환 : `Command + enter`
- 탭 순환 이동 : `Command + tab`
- 탭 이동 : `Command + 번호`, `Command + 방향키`
- 탭 세로 분할 : `Command + d`
- 탭 가로 분할 : `Command + Shift + d`
- 탭 분할 시 포커스 찾기 : `Command + /`
- 탭 분할 포커스 이동 : `Command + [` , `Command + ]`
- 탭 투명하게 설정 : `Command + i`
- 탭 투명하게 on/off : `Command + u`
- 검색 : `Command + f`
- 검색 결과 탐색 : `Command + g`, `Command + Shift + g`
- 전체 검색 : `Command + Option + e`
- 클립보드 : `Command + Shift + h`
- 자동완성 : `Command + ;`
- 작업시간 보여주기 : `Command + Shift + e`
- Preferences : `Command + ,`
- Profiles Preferences : `Command + i`
- iTerm2 종료 : `Command + q`

# References

- https://www.iterm2.com
