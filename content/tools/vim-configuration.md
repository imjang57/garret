Title: Vim Configuration
Date: 2017-05-05
Modified: 2017-05-05
Tags: vim
Slug: vim-configuration
Authors: imjang57
Summary: Vim 설정

# Vim Configuration

Vim 은 실행 중에 여러 설정들을 필요에따라 바꿔서 사용할 수 있다. 그리고 설정 파일을 생성하여 원하는 설정을 적용할 수도 있다.

Vim 설정 파일은 보통 `.vimrc` 라는 이름으로 생성되는데, 사용자의 Home 밑에 `~/.vimrc` 로 생성하면 Vim 이 자동으로 이 파일을 찾아서 파일이 있으면 파일의 내용을 확인하여 설정을 적용한다.

## Key mapping

Vim 에서 Key mapping 할 때 `map` 또는 `noremap` 을 사용하게 된다.

Vim 에서 `:map j gg` 를 실행하면 `j` 가 `gg` 로 mapping 되어서 _Normal mode_ 에서 `j` 를 입력하면 `gg` 가 실행된다.

만약 `:map j gg`, `:map Q j` 를 실행하면 `j` 를 눌러도, `Q` 를 눌러도 `gg` 가 실행된다. `Q` 가 `j` 로 mapping 되고, 다시 `j` 가 `gg` 로 mapping 되는 것이다.

`:map j gg`, `:map Q j`, `:map gg Q` 와 같이 무한으로 재귀적으로 참조하게 되면 오류가 발생한다. `map` 은 recursive key mapping 을 하기 때문이다.

`:map` 과 반대로 `:noremap` 은 non-recursive key mapping 이다. `:map j gg`, `:map Q j`, `:map gg Q` 를 해도 오류가 발생하지 않는다. `Q` 를 누르면 `j` 를 누른 것과 같다. 한 번 key mapping 하여 변환되면 끝이다.

Vim 은 또한 각 mode 별로 key mapping 을 설정할 수 있다.

- `nmap` : display normal mode maps
- `imap` : display insert mode maps
- `vmap` : display visual and select mode maps
- `smap` : display select mode maps
- `xmap` : display visual mode maps
- `cmap` : display command-line mode maps
- `omap` : display operator pending mode maps

예를 들어, `:nnoremap g gg` 를 실행하면 _Normal mode_ 에서 `g` 를 누르면 `gg` 로 non-recursive mapping 을 한다.

key mapping 을 할 때 특수 기능 키에 대해 mapping 을 하려면 아래 내용을 참고하여 mapping 하자.

- `<BS>` : Backspace
- `<Tab>` : Tab
- `<CR>` : Enter
- `<Enter>` : Enter
- `<Return>` : Enter
- `<Esc>` : Escape
- `<Space>` : Space
- `<Up>` : Up arrow
- `<Down>` : Down arrow
- `<Left>` : Left arrow
- `<Right>` : Right arrow
- `<F1>` - `<F12>` : Function keys 1 to 12
- `#1`, `#2` .. `#9`, `#0` : Function keys F1 to F9, F10
- `<Insert>` : Insert
- `<Del>` : Delete
- `<Home>` : Home
- `<End>` : End
- `<PageUp>` : Page-Up
- `<PageDown>` : Page-Down

만약 `:imap ,<Space> <Space><Space><Space><Space>` 와 같이 key mapping 을 하면, `,<Space>` 를 입력할 때마다 4개의 Space 가 입력된다.

key mapping 에 대한 자세한 내용은 `:help key-mapping` 또는 [Mapping keys in Vim - Tutorial (Part 1)](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_%28Part_1%29) 을 참고하자.

## <leader> key

Vim 에는 leader key 가 있다. Default 로 `\` 가 leader key 로 되어 있는데, 설정에서 이 leader key 를 이용하여 많은 작업들에 대한 단축키를 생성할 수 있다.

예를 들어, `:map <leader>A g` 를 실행하면  `\A` 를 입력했을 때 `g` 를 실행한 것과 같은 결과를 얻을 수 있게 된다. 이때 leader key 를 누른 후 1초 내에 다음 key 를 입력해야 한다.

leader key 를 `,` 로 변경하려면 `:let mapleader=","` 를 실행한다.

# My `.vimrc` file

```vim
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""Belows are basic vim configurations
""""""""""Refer `:help quickref` (quickref.txt)
syntax on
set nu                   "line numbers
set tabstop=4            "tab stop
set softtabstop=4        "soft tabstop
"set expandtab            "soft tab: fill tab with blank characters(space)
set shiftwidth=4         "tab stop for '>' command
set autoindent           "Auto indentation
set cindent              "The C programming language indentation
set smartindent          "smart autoindenting for C programs
set history=100          "remember work history
set hlsearch             "hilighting search word
set showmatch            "hilighting matched parentheses : (),{}
set ruler                "show current cursor's location at lower right side
set showmode             "To be able to see what mode you are in.
set laststatus=2         "always show status bar
set nobackup             "don't create backup file
set relativenumber
""set backup               "create backup file
"set backupdir=~/vim/backup "set directory where backup file is saved
set nocompatible         "be improved, required
colorscheme evening


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""belows are settings for gvim running on high resolution
set guifont=Consolas:h11:cANSI
"set guifontwide=Dotumche:h11:cDEFAULT


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""belows are encoding configurations
"auto detected file encoding list which is used when vim opens file
set fencs=utf-8,euc-kr,cp949,cp932,euc-jp,shift-jis,big5,latin1,ucs-2le
"Use command :set fileencoding=utf-8 when you change current file's encoding


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""belows are key mappings
nnoremap <leader>q :bp<CR>
nnoremap <leader>w :bn<CR>
nnoremap <silent> <Leader>+ :exe "resize " . (winheight(0) * 3/2)<CR>
nnoremap <silent> <Leader>- :exe "resize " . (winheight(0) * 2/3)<CR>
```

Vim 일반 설정 :

- `set nocompatible` : vi 호환성을 위한 기능을 사용하지 않는다.
- `syntax on` : syntax highlighing 을 사용한다.
- `set nu` : 왼쪽에 line number 를 보여준다.
- `set tabstop=4` : tab size 를 4로 지정한다.
- `set softtabstop=4` : tab size 를 4로 지정한다.
- `set shiftwidth=4` : tab size 를 4로 지정한다.
- `set expandtab` : tag 을 space 로 사용하도록 한다.
- `set relativenumber` : line number 를 현재 위치한 line 에서 상대적인 값으로 보여준다.
- `set hlsearch` : `/` 로 검색할 때 검색된 문자열에 highlight 를 해준다.
- `set ignorecase` : `/` 로 검색할 때 대소문자를 구분하지 않는다.
- `set autoindent` : 새로운 line 을 입력할 때 자동으로 indent 를 적용한다.
- `set cindent` : 새로운 line 을 입력할 때 C style 의 indent 를 적용한다.
- `set smartindent` : 
- `set showmode` : 현재 어떤 mode 인지를 status bar 에 보여준다.(NORMAL, INSERT, VISUAL, etc)
- `set nobackup` : 파일을 열어서 buffer 를 생성할 때 backup 파일을 만들지 않는다.
- `set ruler` : 현재 cursor 의 위치를 하단에 있는 status bar 의 오른쪽에 보여준다.
- `set history=100` : 100 개의 work history 를 저장한다.
- `set showmatch` : `(` 와 `)`, `{` 와 `}` 등 matched parentheses 에 hlghlight 적용한다.
- `set colorscheme evening` : evening color theme 를 사용한다.
- `set fences=utf-8,euc-kr,cp949,latin1` : vim 이 파일을 열 때 자동으로 인식할 file encoding 목록을 지정한다.

Vim key 설정 :

- `let mapleader = ","` : leader key 를 '\' 에서 ',' 로 변경한다.
- `nnoremap <leader>q :bp<CR>` : `<leader key> + q` 를 누르면 previous buffer 로 이동한다. `:bp` 명령과 같은 일을 한다.
- `nnoremap <leader>w :bn<CR>` : `<leader key> + w` 를 누르면 next buffer 로 이동한다. `:bn` 명령과 같은 일을 한다.

# References

- [vim 설정파일 알아보기](http://jaeheeship.github.io/console/2013/11/15/vimrc-configuration.html)
- [Mapping keys in Vim - Tutorial (Part 1)](http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_%28Part_1%29)
