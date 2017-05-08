Title: Vim Basics
Date: 2017-05-03
Modified: 2017-05-04
Tags: vim
Slug: vim-basics
Authors: imjang57
Summary: Vim 기본 사용법

# VIM (VI Improved)

이 문서는 Vim 의 가장 기본적인 사용법을 정리한 문서이다.

- Web page : http://www.vim.org

CLI(Command Line Interface) 기반의 Text editor 이다. Linux, Mac, Windows 모두 지원한다. 처음 사용법이 익숙해지기가 어렵지만 한번 익히면 마우스 없이 대부분의 작업들을 빠르게 수행할 수 있다. 리눅스 서버는 대부분 CLI 환경만 제공되기 때문에 리눅스 서버 관리자라면 거의 필수로 익혀야 하는 Text editor 이다.

Vimscript 라는 것을 작성하여 플러그인을 만들 수 있다. 사용법을 손에 익히고 여러 플러그인을 설치하면 왠만한 IDE 뺨치는 기능을 사용할 수 있다.

# Vim modes

Vim 은 여러가지 모드를 제공한다. 대표적으로 사용되는 모드는 다음과 같다.

- _Normal mode_ : where you can execute commands. This is default mode in which Vim starts up.
- _Insert mode_ : where you are simply writing text.
- _Visual mode_ : where you visually select a bunch of text so that you can run a command or operation only on that part of the text.

Vim 을 실행하면 가장 먼저 _Normal mode_ 상태로 실행된다. 다른 모드에서 `ESC` 를 입력하면 _Normal mode_ 로 돌아온다.

_Normal mode_ 에서 `:` 를 입력하면 Command 를 입력할 수 있다. 보통 Command 를 실행할 때 2가지 방법으로 하게 되는데 하나는 `:` 를 입력한 후 Command 를 직접 입력하는 것이고, 다른 하나는 단축키를 사용하는 것이다. 2가지 모두 많이 사용되는 방법이다.

커서 이동, put, yank, delete, search, replace, 기타 등등 대부분의 작업은 _Normal mode_ 에서 실행된다.

# Help page

Vim 은 기본적으로 built-in help documentation 을 내장하고 있어서 작업 도중에 수시로 help documentation 을 참고할 수 있다.

Normal mode 에서 `:help` command 를 실행하면 확인할 수 있다. 자주 보게 되는 help 내용은 다음과 같다.

- `:help [keyword]` : shows documentation [for keyword]
- `:help abbreviation` : help for abbreviations
- `:help quickref` : Quick Reference
- `:help user-manual` : User Manuals

만약 플러그인을 설치할 때 플러그인이 help 를 제공하면 해당 플러그인의 help 문서도 확인가능하다.

# Switching between modes

- _Normal mode_ --(`i`, `I`, `a`, `A`, `o`, `O`, `r`, `R`, `s`, `S`)--> Insert mode
- _Normal mode_ --(`v`, `V`)--> Visual mode
- _Insert mode_ --(`ESC`)--> Normal mode
- _Visual mode_ --(`ESC`)--> Normal mode

# Move cursor

- move left / up / right / down : `h` / `j` / `k` / `l`
- move left / up / right / down 3 times repeatedly : `3h` / `3j` / `3k` / `3l`
- move the cursor to the next word : `w`
- move the cursor to the previous word : `b`
- go to specific line number : `<line-number>G`
- go to head of line : `^`, `0`
- go to tail of line : `$`
- page up / down : `ctrl + b` / `ctrl + f`
- page up / down half : `ctrl + d` / `ctrl + u`
- jump to start of file : `gg`
- jump to end of file : `G`
- jump to top / bottom / middle of window : `H` / `L` / `M`
- move to previous / next sentence : `(` / `)`
- move to previous / next paragraph : `{` / `}`

# Editing

- insert before the curosr : `i`
- insert at the beginning of the line : `I`
- insert (append) after the cursor : `a`
- insert (append) at the End of the line : `A`
- append (open) a new line below the current line : `o`
- append (open) a new line above the current line : `O`
- replace a single character : `r`
- replace from current cursor : `R`
- join line below to the current one : `J`
- exit _Insert mode_ (swith to _Normal mode_) : `ESC`

# Open and Close file

Vim 에서 파일을 열면 _buffer_ 라는 것을 생성하여 파일의 내용을 메모리에 올린 후 작업을 수행하게 된다.

- Open file (buffer) : `:e <path>`, `:edit <path>`
- Save file (buffer) : `:w`, `:write`
- Save file (buffer) as : `:saveas <path>`
- Close file (buffer) : `:bd`, `:bw`
- Quit Vim : `:q`
- Print Working Directory : `:pwd`
- Print path of current file : `:echo @%`
- Print absolute path of current file : `echo expand('%:p')`

# Use Mark

Vim 에서 _buffer_ 의 특정 위치를 alphabet(a-zA-Z) 으로 마킹할 수 있다. 자세한 내용은 `:help mark` 와 `:help mark-motions` help page 를 참고하자.

- mark current location as a : `ma`
- goto mark a : `'a` (cursor located on first non-blank character), `a (cursor located on marked character)
- list of marks : `:marks`

# Abbreviation

- set abbreviation foo with foooo : `:ab foo foooo`
- unset abbreviation foo : `:unab foo`

위의 예의 경우, _Insert mode_  에서 foo 와 <SPACEBAR|ENTER> 를 입력하면 foooo 가 입력된다.

# Cut (Delete), Copy (Yank) and Paste (Put)

- cut (delete) word : `dw` (start from cursor), `daw` (whole word)
- cut (delete) current line : `dd`, `:d`
- cut (delete) 4 lines : `4dd`
- cut (delete) to the end of the line : `d$`
- cut (delete) from cursor to end of current line : `D`
- cut (delete) one character of cursor : `x`
- cut (delete) one character before cursor : `X`
- cut (delete) 3 character of cursor : `3x`
- cut (delete) 3 character before cursor : `3X`
- cut (delete) lines from 4 to 10 inclusive : `:4,10d`
- copy (yank) word : `yw` (start from cursor), `yaw` (whole word)
- copy (yank) current line : `yy`, `Y`, `:y`
- copy (yank) 4 lines : `4yy`
- copy (yank) lines from 4 to 10 inclusive : `:4,10y`
- paste (put) at after current : `p`
- paste (put) at before current : `P`
- cut (delete) from current line to end of text : `dG`
- cut (delete) from current line to start of text : `dgg`

# Undo and Redo

- undo : `u`
- redo : `ctrl + r`

# Select

- swith to visual mode to select texts : `v`
- swith to visual mode to select line by line : `V`
- swith to visual mode to select vertical : `Ctrl + v`

You can select texts in visual mode using vi move keys such as `h`, `j`, `k`, `l`, `G`, `gg`, `w`, `b`, `H`, `L`, `M`, etc. After selection, you can use `d` for cut, `y` for copy, etc.

# Search

- search text : `/searchtext` in _Normal mode_

If you want to search text _Hotkeys_, input `/Hotkeys`. Searching text is case-sensitive. If you want to ignore case, input `:set ignorecase`.

After run `/searchtext` command, you can move to next and previous occurrence by `n` and `N`.

Vim provide incremental search. This is helpful when you know only a part of the phrase. After `:set incsearch`, vim will start searching by everytime you type.

The `searchtext` can be regular expression. For example:

- delete lines which are matched to pattern : `:g/pattern/d`
- delete empty lines : `:g/^$/d`
- delete lines which are include hello : `:g/hello/d`

# Macro

- record macro as a : `qa`
- stop recording macro : `q`
- run macro a : `@a`
- rerun last run macro : `@@`

# References

- [Vim Cheat Sheet](https://vim.rtorr.com/)
- [Vim Cheat Sheet Github](https://github.com/rtorr/vim-cheat-sheet)
