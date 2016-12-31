Title: TMUX Introduction
Date: 2016-12-31
Modified: 2016-12-31
Tags: tmux
Slug: tmux-introduction
Authors: imjang57
Summary: TMUX 설치 및 사용법에 대한 간단한 소개

# TMUX (Terminal Multiplexer)

_tmux_ 는 terminal session 을 관리하기 위한 tool 이다. 여러 session 을 생성하여 서로 다른 workspace 를 만들 수 있고, session 을 유지시켜서 server 가 완전히 power off 되지않는다면 workspace 를 유지할 수도 있다.

_tmux_ + _vim_ + _bash_ 는 매우 강력한 linux environment 를 제공한다.

## 설치

- OS X: `brew install tmux`
- Ubuntu: `apt-get install libevent-dev tmux`
- CentOS: `yum install libevent-dev tmux`

Linux 에서는 환경에 따라서 libncurses 모듈이 필요할 수 있다

# tmux basic concepts

_tmux_ 를 이용하기 전에 아래와 같은 개념에 대해 알고 가자.

- _session_ : _tmux_ 실행 단위이다. 하나의 workspace 라고 생각할 수 있다.
- _window_ : _session_ 내에 생성되는 하나의 terminal
- _pane_ : terminal 화면을 분할한 단위
- _status bar_ : 화면 아래부분에 표시되는 _session_ 의 status bar

99% 정도되는 대부분의 command 는 `ctrl + b` 를 누른다음 이어서 command key 를 입력하여 실행된다. 예를 들어 command mode 로 직접 명령어를 입력하고 싶을 때는 `ctrl + b, :` 와 같이 키를 입력한다. 정확하게는 `ctrl + b` 를 누른 후 5초 내에 `:` 를 입력한다. 5초 내에 command key 를 입력하면 된다.

## Session

_tmux_ 를 실행하면 _session_ 이라는 것이 생성된다. _session_ 은 실제 작업이 이루어지는 workspace 이며, _tmux_ 는 이 _session_ 을 관리하는 tool 이다.

### create, rename, exit session

새로운 session 을 생성:

```bash
$ tmux
$ tmux new-session -s <session name>
$ tmux new -s <session name>
```

session name 을 직접 정하지 않았을 경우 숫자가 기본 session name 이 된다. 변경하고 싶으면 아래와 같은 command 를 입력한다.

```bash
$ tmux rename-session -t <target session> <new session name>
```

위의 명령에서 `tmux` 를 제외한 부분(`rename-session` 부터)을 _session_ 내에서 command mode(`ctrl + b, :`) 에서 사용해도 된다.
또는 session 내에서 `ctrl + b, $` 를 입력한다. 그러면 status bar 가 아래처럼 나타난다.

```
(rename-session) 0
```

기존의 session name 인 0 을 삭제하고 새로운 session name 을 입력한다.

```
(rename-session) testsession
```

생성된 session 을 종료하고 싶으면 session 내에서 `exit` 를 실행한다. 또는 `ctrl + d` 를 입력한다.

### attach and detach session

_session_ 을 실행한 후 이를 유지하고 _session_ 밖으로 나갈 수도 있다. 서버만 내려가지 않는다면 이 _session_ 을 계속 유지시킬 수 있다. 이렇게 동작하는 것을 _session_ 을 detach 한다고 하는데 command mode 에서 `detach` 를 입력하여 실행할 수 있다. 또는 `ctrl + b, d` 를 입력해도 된다.

이미 생성된 session 의 목록을 확인하려면 아래 명령을 실행한다.

```bash
$ tmux list-sessions
testsession: 1 windows (created Thu Dec 22 09:31:45 2016) [224x41]
```

특정 session 에 다시 접속하려면 아래 명령을 실행한다.

```bash
$ tmux attach-session -t testsession
```

위 명령을 아래 처럼 짧게 사용할 수도 있다.

```bash
$ tmux attach -t testsession
```

## Window

_window_ 는 _session_ 내에서 나누어지는 공간이다. 일반적으로 인터넷 브라우저나 다른 어플리케이션에서 볼 수 있는 탭과 같은 것이다. _session_ 이라는 workspace 에 여러 _window_ 를 생성하여 한번에 여러가지 일들을 동시에 할 수 있게 된다.

### create, rename, close window

최초에 _session_ 이 생성되면 무조건 1 개의 _window_ 가 생성된다. 최대 10개까지 생성할 수 있다. 화면 아래에 있는 status bar 에서 현재 _window_ 는 `*` 가 window name 옆에 표시된다.

현재 _session_ 에서 새로운 _window_ 를 생성하려면 `ctrl + b, c` 를 입력한다. _tmux_ 로 새로운 _session_ 을 생성하면서 동시에 _session_ 과 _window_ 의 이름을 지정하려면 `tmux new-session -s testsession -n testwindow` 명령으로 _tmux_ 를 실행하면 된다:

현재 활성화된(`*` 로 표시된) _window_ 의 name 을 변경하려면 `ctrl + b, ,` 을 입력한다.

현재 활성화된 _window_ 를 삭제하려면 `ctrl + b, &` 를 입력하거나 `ctrl + d` 를 입력한다.

### Move to window

_window_ 사이를 이동하려면 `ctrl + b, <window number: 0–9>` 를 입력한다. 또는 `ctrl + b, n` 으로 다음 _window_ 로, `ctrl + b, p` 로 이전 _window_ 로 이동할 수 있다. 바로 직전에 작업하고 있던 _window_ 로 가려면 `ctrl + b, l` 을 사용한다. l 의 의미는 last-window 이다.

또 다른 _window_ 를 이동하는 방법은 `ctrl + b, w` 를 사용하는 방법이다. 이 키를 입력하면 화면에 현재 _session_ 내에 열려 있는 _window_ 들이 list-up 된다. 원하는 _window_ 를 선택하여 바로 이동할 수 있다.

`ctrl + b, f` 를 이용하면 검색을 이용하여 _window_ 를 이동할 수 있다. 검색 결과가 복수이면 해당 _window_ 들이 list-up 된다. 원하는 _window_ 를 선택해서 이동할 수 있다.

### Exit window

현재 _window_ 를 종료하려면 terminal 에서 `exit` command 를 실행한다. 또는 `ctrl + d` 를 입력한다. 모든 _window_ 가 종료되면 _session_ 도 종료된다.

## Pane

_pane_ 은 _windows_ 를 구성하는 화면들이다. _windows_ 는 1개 또는 여러 개의 pane 들로 구성될 수 있다. 때문에 2개의 _pane_ 을 만들어서 _window_ 를 좌우로 나누어 사용할 수도 있다.

###  Split

좌우로 window 분할(Split vertical)하려면 `ctrl + b, %` 를 입력한다. 또는 command mode 로 `split-window -h` 를 입력한다.

상하로 window 분할(Split horizontal)하려면 `ctrl + b, “` 를 입력한다. 또는 command mode 로 `split-window -v` 를 입력한다.

### Move to pane

`ctrl + b, q` 를 입력하면 각 _pane_ 에 숫자가 잠시 표시된다. 이 때 원하는 pane 의 숫자를 입력하면 해당 _pane_ 으로 이동한다. 2초 간의 timeout 내에 입력해야 한다.

`ctrl + b, o` 를 입력하면 정해진 순서에 따라 현재 _window_ 에 생성된 _pane_ 들을 차례대로 이동한다.

`ctrl + b, 방향키(Arrow key)` 를 입력하면 인접한 방향의 _pane_ 으로 이동한다.

### Exit pane

현재 _pane_ 을 종료시키려면 terminal 에서 `exit` command 를 실행한다. 또는 `ctrl + d` 를 입력한다.

`ctrl + b, x` 를 입력하면 status bar 에 y/n 을 묻는 prompt 가 표시된다. y 를 선택하면 종료된다.

모든 _pane_ 들이 종료되면 _window_ 도 종료된다.

### Resizing pane

command mode 에서 명령을 입력하며 _pane_ 의 size 를 조절할 수 있다.

- 왼쪽으로 10 줄이기 : `resize-pane -L 10`
- 오른쪽으로 10 늘리기 : `resize-pane -R 10`
- 아래쪽으로 10 늘리기 : `resize-pane -D 10`
- 위쪽으로 10 늘리기 : `resize-pane -U 10`

# Configuration file

tmux configuration file 은 `~/.tmux.conf` 이다.

# Key binding

`ctrl + b + ?` 을 입력하면 현재의 key binding 리스트를 볼 수 있다.

사용자가 원하면 `~/.tmux.conf` 파일에 key binding 를 설정할 수 있다. 자세한 내용은 tmux manpage 를 참고하자.

# Copy mode

tmux 를 실행하고 있는 환경에서는 scroll bar 가 없다. 이때 _Copy mode_ 를 사용하면 이전 출력들을 볼 수 있다. 또한 _session_ 안에서 원하는 text 를 copy / paste 할 수 있다.

`ctrl + b, [` 를 입력하면 _Copy mode_ 로 진입한다. _pane_ 의 오른쪽 상단에 buffer 에 저장된 총 line 수가 출력된다. _Copy mode_ 를 종료하고 싶으면 `Enter` 를 입력하거나 `q` 를 입력한다.

_Copy mode_ 에서 이동은 `방향키(Arrow key)`, `PageUp`, `PageDown` 키들을 사용한다. 만약 vi editor 의 방식으로 이동하고 싶으면 `~/.tmux.conf` 파일에 `setw -g mode-keys vi` 를 추가한다. 이 설정을 하면 `h`, `j`, `k`, `l`, `G`, `g`, `ctrl + f`, `ctrl + b` 등 vi editor 에서 cursor 이동에 사용되는 key 들을 사용할 수 있다.

_Copy mode_ 에서 검색은 `?` 와 `/` 를 사용한다. `?` 또는 `/` 를 입력하면 _pane_ 왼쪽 아래부분에 `Search Up:` 이라고 표시된다. 여기에 검색어를 입력한다. `?` 를 입력하면 위로 검색, `/` 를 입력하면 아래로 검색한다. 다음, 이전 검색은 `N`, `n` 을 입력한다.

_Copy mode_ 에서 `SPACEBAR` 키를 입력하면 _Visual mode_ 가 되며, Text 를 선택할 수 있게 된다. 선택한 Text 를 복사하고 싶으면 `Enter` 키를 입력한다. _Copy mode_ 에서는 quit 의 의미이지만 _Visual mode_ 에서는 복사와 함꼐 quit 를 수행한다. 복사한 Text 를 붙여넣고 싶다면 `ctrl + b, ]` 를 입력한다.

`ctrl + b, :` 를 입력하여 command mode 를 실행한 후 `list-buffers` 를 실행하면 현재 저장된 모든 buffer 들을 볼 수 있다. `choose-buffer` 를 입력하면 모든 buffer 들의 리스트가 출력되고 원하는 buffer 를 선택할 수 있다. `show-buffer` 를 입력하면 0번째 buffer 의 내용을 보여준다. 참고로 `ctrl + b, ]` 는 무조건 0번째 buffer 를 붙여넣기 한다.

# Start with script

_session_ 을 만들고, 화면을 분할하고, 특정 directory 를 생성하고, 패키지를 설치하고, 기타 필요한 작업들을 script 로 작성하여 _session_ 을 생성할 때 한꺼번에 수행되도록 할 수 있다.

tmux initilizing automation script example:

```bash
$ cat start_with_tmux.sh
#!/bin/bash
SESSION=tmuxtest
PROJECT_HOME="~/Projects"
PROJECT_NAME=${1:-node-project}
TMUX="tmux"
# Create new session
$TMUX new-session -d -s $SESSION
# Create new windows
$TMUX new-window -t $SESSION:1 -n withindex
$TMUX new-window -t $SESSION -n withoutindex
# Select window
$TMUX select-window -t withindex
# Split window
$TMUX split-window -h
# Select pane and run commands
$TMUX select-pane -t 0
$TMUX send-keys "mkdir -p $PROJECT_HOME" Enter
$TMUX send-keys "cd $PROJECT_HOME" Enter
$TMUX send-keys "echo 'date' > test.txt" Enter
$TMUX split-window -v
# C-m means Carriage Return (one of control characters)
$TMUX send-keys "cd $PROJECT_HOME" Enter
$TMUX send-keys "tail -f test.txt" C-m
# Select pane and run commands
$TMUX select-pane -t 2
$TMUX send-keys "ls -ail" Enter
References
http://tmux.github.io/
https://github.com/tmux/tmux
http://haruair.com/blog/2124
http://nodeqa.com/nodejs_ref/99
```

# References

- [tmux web](https://tmux.github.io)
- [tmux github](https://github.com/tmux/tmux)

