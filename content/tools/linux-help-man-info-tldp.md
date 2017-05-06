Title: Linux help, man, info, TLDP
Date: 2017-05-07
Modified: 2017-05-07
Tags: linux, help, man, info
Slug: linux-help-man-info-tldp
Authors: imjang57
Summary: Linux 를 사용함에 있어서 가장 큰 도움이 되고 필수로 알아야 할 도움말이나 문서들에 대해서 간단한게 정리한 글

# Linux _help_, _man pages_, GNU _info_, TLDP

Linux 를 사용함에 있어서 가장 큰 도움이 되고 필수로 알아야 할 도움말이나 문서들에 대해서 간단한게 정리한 글이다.

Linux 를 사용하다보면 Console 등의 CLI (Command-Line Interface) 에서 여러 명령어들을 사용하게 된다. 그런데 매우 많은 명령어들이 있고 각 명령어마다 다양한 옵션과 Argument 를 사용할 수 있기 때문에 이들의 사용법을 모두 외우는 것은 거의 불가능하고 비효율적이다.

그래서 어떤 명령어에 대해 익히면 이후에는 `--help` 옵션, _man pages_ utility, GNU _info_ utility 등을 참고하며 사용하게 된다.

명령어들을 만든 개발자들은 왠만하면 `--help` 정도는 최소한 제공하며, Linux 에서 사용되는 대부분의 명령들은 잘 작성된 `--help` 와 _man pages_  매뉴얼을 제공한다. 사실 이들을 제공하지 않으면 Linux 를 사용하는게 매우 힘들어 진다.

또한, 자발적인 기여자들이 모여 TLDP()

# `--help` 옵션

`--help` 옵션을 거의 필수적인 요소이다. 이게 없다면 프로그램을 사용하는 사람은 한 명도 없을 수도 있다. 최소한 사용방법을 알아야 할 것 아닌가.

_man pages_ 나 _info_ 의 경우는 그 자체로 하나의 프로그램이라 (정말 극소수이지만) 어떤 시스템에는 없을 수도 있다. 따라서 `--help` 옵션을 개발자가 사용자에게 제공해줄 수 있는 최소한의 문서이다.

예를 들어, `man` 명령은 다음과 같은 `--help` 를 출력한다.
```
man --help
man, version 1.6c

usage: man [-adfhktwW] [section] [-M path] [-P pager] [-S list]
	[-m system] [-p string] name ...

  a : find all matching entries
  c : do not use cat file
  d : print gobs of debugging information
  D : as for -d, but also display the pages
  f : same as whatis(1)
  h : print this help message
  k : same as apropos(1)
  K : search for a string in all pages
  t : use troff to format pages for printing
  w : print location of man page(s) that would be displayed
      (if no name given: print directories that would be searched)
  W : as for -w, but display filenames only

  C file   : use `file' as configuration file
  M path   : set search path for manual pages to `path'
  P pager  : use program `pager' to display pages
  S list   : colon separated section list
  m system : search for alternate system's man pages
  p string : string tells which preprocessors to run
               e - [n]eqn(1)   p - pic(1)    t - tbl(1)
               g - grap(1)     r - refer(1)  v - vgrind(1)
```

# _man pages_

_man pages_ 는 Unix 와 Linux 에서 대부분 기본 제공되는 도구이다. _man pages_ 라는 프로그램 이름은 _manual pages_ 를 의미한다.

`man <page name>` 과 같이 실행 할 수 있다. 예를 들어 `man man` 을 실행하면 아래와 같이 `man` 명령어에 대한 도움말을 볼 수 있다.

```
man(1)                                                                                                                           man(1)



NAME
       man - format and display the on-line manual pages

SYNOPSIS
       man  [-acdfFhkKtwW]  [--path]  [-m system] [-p string] [-C config_file] [-M pathlist] [-P pager] [-B browser] [-H htmlpager] [-S
       section_list] [section] name ...


DESCRIPTION
       man formats and displays the on-line manual pages.  If you specify section, man only looks in that section of the manual.   name
       is normally the name of the manual page, which is typically the name of a command, function, or file.  However, if name contains
       a slash (/) then man interprets it as a file specification, so that you can do man ./foo.5 or even man /cd/foo/bar.1.gz.

       See below for a description of where man looks for the manual page files.


OPTIONS
       -C  config_file
              Specify the configuration file to use; the default is /private/etc/man.conf.  (See man.conf(5).)

       -M  path
              Specify the list of directories to search for man pages.  Separate the directories with colons.  An  empty  list  is  the
              same as not specifying -M at all.  See SEARCH PATH FOR MANUAL PAGES.

       -P  pager
              Specify  which  pager to use.  This option overrides the MANPAGER environment variable, which in turn overrides the PAGER
              variable.  By default, man uses /usr/bin/less -is.

       -B     Specify which browser to use on HTML files.  This option overrides the BROWSER environment variable. By default, man uses
              /usr/bin/less-is,

       -H     Specify a command that renders HTML files as text.  This option overrides the HTMLPAGER environment variable. By default,
              man uses /bin/cat,

       -S  section_list
              List is a colon separated list of manual sections to search.  This option overrides the MANSECT environment variable.

...........
```

`man` 을 실행한 결과는 `less` 나 `more` 같은 pager utility 를 사용하여 출력된다. `q` 를 입력하면 종료되고, `/` 를 입력하면 문자열 검색을 수행할 수 있다.

_man pages_ 는 주제에 따라 여러가지 secton 으로 나누어서 제공된다:

- 1 : User commands
- 2 : System calls
- 3 : Subroutines (Libraries)
- 4 : Devices (files in `/dev` directory)
- 5 : File formats (example : format of `/etc/passwd` file)
- 6 : Games
- 7 : Miscellaneous (Macro, naming rules, etc)
- 8 : System administration
- 9 : Local
- 10 : New

`man write` 라고 실행하면 _write_ 라는 사용자 명령어에 대한 내용을 출력하고 `man 2 write` 라고 실행하면 _write_ 라는 linux kernel system call 에 대한 내용을 출력한다.

`man passwd` 라고 실행하면 _passwd_ 라는 사용자 명령어에 대한 내용을 출력하고 `man 5 passwd` 라고 실행하면 관련된 파일(`/etc/passwd`)들에 대한 내용을 출력한다

`man -k passwd` 를 실행하면 passwd 라는 키워드와 관련있는 매뉴얼들의 목록을 출력한다. `-k` 옵션을 키워드를 의미한다.

```
$ man -k passwd
chkpasswd(8)             - verifies user password against various systems
firmwarepasswd(8)        - tool for setting and removing firmware passwords on a system
htpasswd(1)              - Manage user files for basic authentication
kpasswd(1)               - Kerberos 5 password changing program
kpasswdd(8)              - Kerberos 5 password changing server
ldappasswd(1)            - change the password of an LDAP entry
passwd(1)                - modify a user's password
passwd(1ssl)             - compute password hashes
passwd(5), master.passwd(5) - format of the password file
slapd-passwd(5)          - /etc/passwd backend to slapd
slappasswd(8)            - OpenLDAP password utility
```

_man pages_ 가 화면에 출력하기 위한 문서들은 `/usr/share/doc` 에 저장되며 최초에는 압축파일 형태로 있다가 최초에 출력될 때 압축 해제된다.

참고로, [Linux man pages](https://linux.die.net/man/)와 같이 온라인에서 man pages 를 확인할 수 있는 여러 사이트들도 있다.

# GNU _info_

_man pages_ 는 Unix 에서 시작되어 오랜 시간 사용되고 있는 도구이다. GNU 에서는 조금 더 문서를 잘 표현할 수 있는 잘 정의된 포맷을 제안했고 이를 Redhat 에서 개발 및 배포했는데 이것이 _info_ 라는 프로그램이다.

`info [menu item]` 의 형태로 실행되며 실행된 상태에서 여러 명령들을 입력하여 다양한 작업을 수행할 수 있다. `info` 가 실행된 상태에서 `?` 를 입력하면 사용 가능한 명령들을 확인할 수 있으며 각 키보드 입력을 위한 표기법은 다음과 같다.

- `C-key` : _CONTROL_ + key (example : `C-h` 는 _CONTROL_ + h key 를 의미)
- `M-key` : _META_(_ALT_) + key (example : `M-x` 는 _META_ + x key 를 의미)

그런데 사실, GNU 에서 만든 프로그램들은 GNU _info_ 에 더 자세히 문서화가 되고 최신으로 업데이트 되어 있다고는 하지만 대부분의 경우 _man pages_ 프로그램만으로도 충분했기에 잘 사용하지 않는다. 인터페이스도 익숙하지 않아서 더 사용하지 않는다.

# TLDP

[TLDP (The Linux Documentation Project)](http://www.tldp.org/)는 자발적으로 참여하는 봉사자들에 의해 진행되는 프로젝트로, 리눅스에 대한 내용을 문서화하기 위한 프로젝트이다. [Github repository](https://github.com/tLDP/LDP)도 있다.

[wikipedia 의 설명](https://ko.wikipedia.org/wiki/%EB%A6%AC%EB%88%85%EC%8A%A4_%EB%AC%B8%EC%84%9C%ED%99%94_%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8)에 다음과 같이 언급되어 있다.

> 리눅스 문서화 프로젝트 (The Linux Documentation Project, TLDP)는 전적으로 자발적인 참여로 진행되는 프로젝트로 리눅스 관련 문서를 만드는 데 목표가 있다.
> 이 프로젝트는 처음엔 리눅스 해커들끼리 각자가 만들어 놓은 문서를 공유하기 위한 목적으로 시작되었다. 따라서 문서의 수준은 직업 시스템 어드민(admin) 등 숙달된 사용자들의 눈높이에 맞춰져 있었다. 그러나 현재에는 초보자들이 따라할 수 있는 강좌도 많이 포함하고 있다.
> 현재 LDP는 475개 이상의 문서를 제공하고 있다. 이 중 십여개는 일반 책의 분량이고, 이들 대부분은 오라일리 등의 컴퓨터 전문 출판사에 의해 출판되어 책으로 구입할 수 있다. LDP는 또한 사용자가 단계적으로 따라해서 목적을 이룰 수 있는 다수의 HowTo 문서 또한 제공한다. 문서의 목적은 매우 다양해서 특정 모뎀의 설정 같은 매우 구체적인 것일 수도 있고, 네트워크 관리와 같은 광대하고 추상적인 것일 수 있다.

또한, 설명에 따르면 TLDP 는 리눅스 관련된 최초에 웹 사이트이다.

KLDP 에서도 매우 많은 TLDP 문서의 번역을 제공하고 있다. 예를 들면 [The Linux System Administrators' Guide 번역](https://wiki.kldp.org/Translations/html/SysAdminGuide-KLDP/book1.html)과 같은 것들이 있다. KLDP 의 더 많은 번역 문서들은 [여기](https://wiki.kldp.org/Translations/html/)에서 확인할 수 있다.

# 기타

IT는 매우 많은 분야가 있고 매우 많은 요소들이 결합되어 유기적으로 동작한다. 한 명이 모든 내용을 알기는 불가능하다. 그래서 웹을 통한 지식 공유가 매우 중요하다. 내 분야에서의 기초 지식과 핵심 원리에 집중하고 나머지는 위임하거나 협력해야 한다.

TLDP 외에도 [google](https://www.google.com/) 검색을 습관화하고 [stack overflow](http://stackoverflow.com/) 등을 적극 활용하면 좋다. 단, 잘못된 지식이나 오래된 지식은 거를 수도 있어야 하니 무조건적으로 맹신하는 것은 좋지 않다.
