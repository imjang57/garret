Title: Vim Basics More
Date: 2017-05-03
Modified: 2017-05-04
Tags: vim
Slug: vim-basics-more
Authors: imjang57
Summary: Vim 기본 사용법에 대해 더 알면 좋은 내용들에 대한 글이다.

# Vim Basics More

Vim 에 대해 추가적으로 알면 좋은 내용들에 대해 정리한 글이다.

# _buffer_, _window_, _tab_

Vim 에서 _buffer_  는 열려 있는 파일(file which is opened)를 뜻한다.

_window_ 는 Vim 이 어떤 것을 출력하기 위한 component 로 _buffer_ 를 출력하는 방법이다. 사실 Vim 의 _buffer_ 는 text 만 출력할 수 있는 것이 아니다. Vim 화면을 가로나 세로로 분할하면 이 _windows_ 가 새로 만들어 지고 각 _window_ 에 _buffer_ 가 출력된다.

_tab_ 은 Vim 의 Layout 이다. 여러 _windows_ 들의 집합이다. 대부분의 Text editor 나 Internet browser 에서 사용하는 tab 과는 개념이 다르다.

- A buffer is the in-memory text of a file.
- A window is a viewport on a buffer.
- A tab page is a collection of windows.

대충 간략하게 정리하면 파일은 _buffer_ 에 로드되고, _buffer_ 는 _window_ 에 의해 출력되고, _window_ 는 _tab_ 에 의해 layout 이 결정된다.

## Vim _buffer_ management

- list of current buffers : `:ls`
- open new file (buffer) : `:e <path>`, `:edit <path>` (with enhanced tab completion (put set wildmenu in your .vimrc))
- save file (buffer) : `:w`, `:write`
- close file (buffer) : `:bd`, `:bw`
- switch between all open files (buffers) : `:b<buffer number>` (`:b#` chooses the last visited file)
- previous buffer : `:bp`, `:bprevious`
- next buffer : `:bn`, `:bnext`
- delete buffer : `:bd [buffer numbers...]`, `:bw`
- Close all buffer : `:%bd`
- Close buffer from buffer number 1 to 1000 : `:1,1000bd`

`:ls` 를 실행하면 Vim 의 하단에 다음과 같이 현재 열려진 _buffer_ 들을 보여준다. 아래 화면에서 _buffer_ 를 선택하여 이동할 수 있다.

```
1 %a   "./checkin.pl"            line 1
2 #    "./grabakamailogs.pl"     line 1
3      "./grabwmlogs.pl"         line 0
  etc.
```

`%` 는 현재 편집 중인 _buffer_ (current buffer) 를 참조한다. `#` 는 직전에 편집하던 _buffer_ (alternative buffer) 를 참조한다. `ctrl + shift + 6` 를 실행하면 두 _buffer_ 사이를 switch 한다.

`e <path>` 를 실행하면 새로운 _buffer_ 를 만들고 전달 받은 파일의 내용을 로드한다. `:e foo.txt bar.txt`, `e /foo/bar/*.txt` 와 같이 한 번에 여러 _buffer_ 를 생성하지는 못한다. 만약, 여러 파일을 한 번에 열고 싶으면 처음에 Vim 을 실행할 때 `Vim file1.txt file2.txt` 와 같이 실행하면 된다. 아니면 `arga [paths...]` 를 실행하면 여러 파일들로 새로운 _buffer_ 를 생성하고 대신 새로운 _buffer_ 로 switch 를 하지는 않는다.

```
:arga foo.txt bar.txt
:argadd /foo/bar/*.txt
```

## Install _BufOnly_ plugin

Vim 으로 _buffer_ 를 사용하다보면 불편할 때가 있는데, 예를 들면 지금 편집중인 _buffer_ 를 빼고 나머지 _buffer_ 들을 모두 닫고 싶을 때이다. `:ls` 로 현재 생성되어 있는 _buffer_ 를 확인하고 `bd <buffer number>` 로 일일이 하나씩 _buffer_ 를 삭제해야 한다. 그래서 나는 _BufOnly_ 라는 plugin 을 설치해서 사용한다.

1. Download `BufOnly.vim` Vimscript at [BufOnly page](http://www.vim.org/scripts/script.php?script_id=1071).
2. Goto `$VIMRUNTIME` : `:echo $VIMRUNTIME`, `:!explorer $VIMRUNTIME` in Vim.
3. Copy downloaded `BufOnly.vim` to `$VIMRUNTIME` directory or `~/.vim/plugin/BufOnly.vim`.
4. Restart Vim

참고로 `$VIMRUNTIME` 은 Vim 실행 후 _Normal mode_ 에서 `:echo $VIMRUNTIME` 으로 확인할 수 있으며 Vim 이 실행되는 root path 이다.

- close buffers : `:BufOnly [buffer number]`

## Vim _window_ management

- split window horizontal : `:sp [path]`, `:split [path]`, `Ctrl + w, s`
- split window vertical : `vs [path]`, `:vertical split [path]`, `Ctrl + w, v`
- resize all windows same : `Ctrl - w, =`
- resize horizontal : `:resize 60`, `:res 60`, `:resize +5`, `:res +5`, `:resize -5`, `:res -5`, `ctrl + w, +`, `ctrl + w, -`
- resize vertical :  `:vertical resize 60`, `:vertical res 60`, `:vertical resize +5`, `:vertical res +5`, `:vertical resize -5`, `:vertical res -5`, `ctrl + w, >`, `ctrl + w, <`
- switch between splitscreens : `ctrl + w, arrow key`, `ctrl + w, <h|j|k|l>`, `ctrl + w, n`, `ctrl + w, p`, `ctrl + w, w`
- close the current window : `ctrl + w, c`, `:q`
- close all windows except the current one : `ctrl + w, o`

To resize in different steps, you can create maps that will adjust the window size differently. For example to increase the window size by a factor of 1.5 and decrease the window size by 0.67, you can map this:

```
nnoremap <silent> <Leader>+ :exe "resize " . (winheight(0) * 3/2)<CR>
nnoremap <silent> <Leader>- :exe "resize " . (winheight(0) * 2/3)<CR>
```

## Vim _tab_ management

- add new tab : `:tabe <path>`, `:tabedit <path>`
- add buffer to tab : `:<tab number>tabe <path>`, `:<tab number>tabedit <path>`
- close tab : `:tabc`, `:tabclose`, `:<tab number>tabc`, `:<tab number>tabclose`
- switch between tabs : `:tabn`, `:tabnext`, `:tabp`, `:tabprevious`
- switch to next tab by number : `gt`, `<number>gt`, `ctrl + PageDown`, `<number>ctrl + PageDown`
- switch to previous tab by number : `gT`, `<number>gT`, `ctrl + PageUp`, `<number>ctrl + PageUp`
- go to tab : `:tabmove <tab number>`, `:tabm <tab number>`

If you map `:tabn` and `:tabp` to your `F7` and `F8` keys you can easily switch between files.

# Selection

- select : `v, [h|j|k|l|g|G|...]`
- select lines : `shift + v, [j|k|g|G|...]`
- select vertical : `ctrl + v, [h|j|k|l|g|G|...]`

# Indentation

In command mode,

- indent current line by shiftwidth spaces : `>>`, `:>`
- de-indent current line by shiftwidth spaces : `<<`, `:<`
- re-indent current line : `==`
- indent 5 lines : `5>>`
- de-indent 5 lines : `5<<`
- re-indent 5 lines : `5==`
- indent lines 4 to 8, inclusive : `:4,8>`
- indent selected lines : Select lines and use `>`
- increase indent of a curly-braces block : put cursor on one of the curly braces and use `>, %`
- decrease indent of a curly-braces block : put cursor on one of the curly braces and use `<, %`
- re-indent a curly-braces block : put cursor on one of the curly braces and use `=, %`
- Paste text, aligning indentation with surroundings : `]p`
- re-indent entire buffer : `gg=G`

In insert mode,

- insert indent at start of line : `ctrl + t`
- remove indent at start of line : `ctrl + d`

vim settings in `.vimrc` file for indentation:

```
set expandtab       "Use softtabstop spaces instead of tab characters for indentation
set shiftwidth=4    "Indent by 4 spaces when using >>, <<, == etc.
set softtabstop=4   "Indent by 4 spaces when pressing <TAB>

set autoindent      "Keep indentation from previous line
set smartindent     "Automatically inserts indentation in some cases
set cindent         "Like smartindent, but stricter and more customisable
```

Vim has intelligent indentation based on filetype. Try adding this to your `.vimrc`:

```
if has ("autocmd")
    " File type detection. Indent based on filetype. Recommended.
    filetype plugin indent on
endif
```

# Folding

여러 line 들을 folding 하면 필요 없는 부분들을 숨겨서 긴 source code 등을 보는데 더 수월할 때가 많다.

folding 을 하는 가장 기본적인 방법은 원하는 line 들을 선택한 후 `z, f`, `:fold`, `:fo` 를 실행하는 것이다.

unfolding 은 folding 된 line 에서 `z, o`, `:foldopen`, `:foldo` 중 하나를 실행하면 된다.

자세한 내용은 `:help fold` 를 참고하자.

# Get the name of the current file

- Register `%` contains the name of the current file
- Register `#` contains the name of the alternate file.

현재 작업 중인 buffer 의 file name 을 확인하려면 register `%` 를 확인하면 된다 : `:echo @%`

기타 file path 를 확인하기 위한 command :

- `:echo expand('%:t')` : `my.txt`, name of file ('tail')
- `:echo expand('%:p')` : `/abc/def/my.txt`, full path
- `:echo expand('%:p:h')` : `/abc/def`, directory containing file ('head')
- `:echo expand('%:p:h:t')` : `dev`, First get the full path with `:p` (`/abc/def/my.txt`), then get the head of that with `:h` (`/abc/def`), then get the tail of that with `:t` (`def`)
- `:echo expand('%:r')` : `my`, name of file less one extension ('root')
- `:echo expand('%:e')` : `txt` name of file's extension ('extension')

For more info run `:help expand`

If all that is wanted is to display the name of the current file, type `Ctrl-G` (or press `1 then Ctrl-G` for the full path).

When using `@%`, the name is displayed relative to the current directory.

