Title: Vim Plugin
Date: 2017-05-05
Modified: 2017-05-05
Tags: vim
Slug: vim-plugin
Authors: imjang57
Summary: Vim Plugin

# Vim Plugin

Vim 은 _Vim script_ 라는 자체 스크립트 언어를 제공하여 Plugin 을 만들 수 있게 한다. 이 스크립트들은 `plugin-name.vim` 과 같이 vim 이라는 확장자(extension) 을 갖는다. _Vim script_ 는 [Vim script page](http://www.vim.org/scripts/index.php) 에 많이 업로드되어 있다.

환경 설정을 위해 사용되는 `.vimrc` 파일도 사실은 _Vim script_ 이다.

Vim plugin 은 2가지 종류가 있다.

- filetype plugin : 특정 file type 에 대해서 동작하는 plugin. Default 로 `$VIMRUNTIME/ftplugin` directory 에서 관리된다.
- global plugin : 모든 file type 에 대해서 동작하는 plugin. Default 로 `$VIMRUNTIME/plugin` directory 에서 관리된다.

각 plugin 의 위치가 `$VIMRUNTIME` 밑에 꼭 있어야 하는 것은 아니다. Vim plugin 을 관리하는 plugin 을 설치하면 각자가 Runtime path 를 관리하여 `~/.vim/bundle` 에 각 plugin 디렉터리를 생성하고 그 하위에 `ftplugin` 과 `plugin` 등 필요한 디렉터리들을 생성해서 사용하기도 한다.

# Vundle

Vim plugin 을 관리하기 위한 여러 plugin 들이 있는데 나는 [Vundle](https://github.com/VundleVim/Vundle.vim) 을 사용한다.

자세한 내용은 [Vundle](https://github.com/VundleVim/Vundle.vim) 에 가면 설치 방법부터 잘 나와있으니 참고하자.

설치는 매우 쉽다. git clone 하여 `~/.vim/bundle/Vundle.vim` 에 설치하겨 `~/.vimrc` 파일에 Vundle 을 위한 설정과 설치하여 사용할 Plugin 목록을 입력해주기만 하면 된다.

```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```

Vundle 은 인터넷을 통해 각 plugin 들을 받아서 `~/.vim/bundle` 에 설치한다.

## My `.vimrc` including Vundle

```
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
"set backup               "create backup file
"set backupdir=~/vim/backup "set directory where backup file is saved
set nocompatible         "be improved, required
colorscheme evening


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""belows are encoding configurations
"auto detected file encoding list which is used when vim opens file
set fencs=utf-8,euc-kr,cp949,cp932,euc-jp,shift-jis,big5,latin1,ucs-2le
"Use command :set fileencoding=utf-8 when you change current file's encoding


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""belows are key mappings
nnoremap <leader>q :bp<CR>
nnoremap <leader>w :bn<CR>

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""Belows are Vundle Plugin configurations
filetype off

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
"Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
"Plugin 'L9'
" Git plugin not hosted on GitHub
"Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
"Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
"Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
"Plugin 'ascenator/L9', {'name': 'newL9'}

Plugin 'The-NERD-tree'
Plugin 'AutoComplPop'
Plugin 'majutsushi/tagbar'
Plugin 'airblade/vim-gitgutter'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'kien/ctrlp.vim'
Plugin 'pathogen.vim'

let g:airline#extensions#tabline#enabled = 1

let NERDTreeWinPost = "left"

nmap <F7> :NERDTree<CR>
"nmap <F8> :TlistToggle<CR>
nmap <F8> :TagbarToggle<CR>
filetype on

let Tlist_Ctags_Cmd = "/usr/bin/ctags"
let Tlist_Inc_Winwidth = 0
let Tlist_Exit_OnlyWindow = 0
let Tlist_Auto_Open = 0
let Tlist_Use_Right_Window = 1

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just
" :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to
"auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

let g:ctrlp_custom_ignore = {
    \ 'dir': '\.git$\|vendor$',
    \ 'file': '\v\.(exe|so|dll)$'
        \ }
```