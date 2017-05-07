Title: Linux 에서 파일 관리를 위한 명령어들
Date: 2017-01-01
Modified: 2017-05-08
Tags: linux, file
Slug: linux-command-for-file-management
Authors: imjang57
Summary: Linux 에서 파일 관리일 위한 명령어들(ls, lsof, chown, chmod, mv, cp, rm, rmdir, mkdir, fuser, ln, file, diff, patch, cat, tail, head, etc)

# Linux 에서 사용자 관리를 위한 명령어들

Linux 에서 파일 목록 확인, 파일 내용 확인, 사용 중인 파일 확인, 파일 정보 변경, 파일 비교, 패치 등을 위한 명령어들을 정리한 글이다.

리눅스에서는 모든 것이 파일로 관리된다. 일반적으로 알고 있는 파일 외에 console, socket, device 등도 모두 파일이다. 그래서 리눅스에서 모든 인터페이스는 File Descriptor 를 기반으로 하고 모든 입력과 출력은 File Descriptor 를 통해 이루어진다.

# 파일 목록 조회

일반적으로 파일 목록을 조회하는 명령어는 `ls` 이다. `ls -alh [path]` 와 같이 여러 옵션을 전달할 수 있다. `-a` 는 숨김파일(리눅스에서는 `.` 으로 시작하면 숨김파일로 처리한다)을 포함한 모든 파일을 보여준다. `-l` 옵션을 file name 외에 mode bits, owner, group, modification time 등의 추가적인 정보도 보여준다. `-h` 옵션을 파일의 크기를 사람이 쉽게 인식할 수 있도록 크기에 따라 KB, MB, GB 단위로 바꿔서 보여준다.

`lsof` 명령어는 사용 중인 파일, 즉 열려 있는 파일들을 확인할 수 있는 명령어이다. user name, process id, network protocol, network port, command name 등 여러 기준으로 사용 중인 파일들을 확인할 수 있다.

- `lsof -u <usrename>` : 특정 사용자가 열어서 사용중인 파일들을 검색
- `lsof <file path>` : 특정 파일을 사용하는 프로세스와 사용자 확인 가능
- `lsof +D <directory path>` : 특정 directory 밑에 있는 열려있는 파일들을 검색
- `lsof -p <process id>` : process id 가 사용 중인 파일들을 검색
- `lsof -i` : 모든 네트웍 포트 중 열려있는 포트를 검색
- `lsof -i TCP` : 모든 TCP 포트 중 열려있는 포트를 검색
- `lsof -i TCP:22` : 22번 TCP 포트를 사용중인 프로세스와 사용자 확인 가능
- `lsof -i TCP:22-80` : 22번에서 80번까지의 TCP 포트 중 열려있는 포트를 검색
- `lsof -c httpd` : httpd command 가 사용 중인 파일들을 검색

또한 `fuser` 명령어를 사용하면 파일을 사용 중인 process id 를 확인할 수 있다.

- `fuser -n tcp 22` : tcp 22 port 를 사용중인 process id 를 확인
- `fuser -n file <file path>` : 특정 파일을 사용중인 process id 를 확인

`file` 이라는 명령어를 사용하면 특정 파일의 type 을 확인할 수 있다. 일반적인 파일이 어떤 파일인지 확인할 때 사용되는데 Text file 인지, 실행 파일, Python code 인지, Shell script 인지를 알 수 있으며 Encoding(ASCII, UTF-8 등) 이 무엇인지도 확인가능하다.

# 파일 메타 정보 변경

Linux 에서 파일은 Owner 와 Group owner 가 있고, mode bits 가 있어서 여러 사용자들이 파일에 대해 어떤 권한까지 접근할 수 있는지를 지정할 수 있다. 이 정보들은 `ls -l` 을 실행하면 확인할 수 있다.

`chown` 은 파일의 owner 정보를 변경한다. `chown [-R] <username>:<groupname> <path>` 와 같이실행할 수 있고 `-R` 옵션이 있으면 하위 디렉터리들과 파일들도 모두 같이 변경한다.

`chmod` 는 파일의 mode bits 를 변경한다. `chown [-R] 755 <path>` 와 같이 실행할 수 있고 `-R` 옵션이 있으면 하위 디렉터리들과 파일들도 모두 같이 변경한다. 또한 sticky bit 를 설정하려면 `chown [-R] 1777 <path>` 와 같이 mode bits 를 1777 하면 된다.

# 파일 처리

파일은 복사, 이동, 삭제 등이 가능하다.

- `mv` : move (rename) files
- `cp` : copy files and directories
    * `cp -r <src> <dst>` : `-r` 옵션을 전달하면 recursive 하게 복사를 수행하여 하위 파일들과 디렉터리들도 모두 복사된다.
- `rm` : remove files or directories
    * `rm -r` : recursive 하게 삭제
    * `rm -f` : 삭제 여부를 묻는 prompting 없이 삭제한다. 그리고 삭제하는 파일이 없어도 에러로 처리하지 않고 그냥 넘어간다.

또한 directory 만을 위한 명령어도 있다.

- `rmdir` : remove empty directories
- `mkdir` : make directories
    * `mkdir -p <path>` : `-p` 옵션을 directory 를 생성할 때 parent directory 가 없을 경우 parent directory 들도 같이 생성한다.

# Link 생성

Linux 에서는 Symbolic link 와 Hard link 가 있다.

- `ln` : make links between files
    * `ln -s <target> <link name>` : Symbolic link 를 생성한다.

# 파일 내용 출력

텍스트 파일의 경우 내용을 확인할 수 있는 여러 명령어들이 있다.

`cat` 은 concatenate and print files 라고 man pages 에 나와있듯이 파일을 출력하고 내용을 추가하기 위해 사용된다.

`cat <filepath>` 를 실행하면 특정 파일의 냉용을 출력한다. 파일의 내용이 많을 경우 `cat <filepath> | less` 또는 `cat <filepath> | more` 와 같이 pipe 를 사용하여 파일의 내용을 pager utility 로 확인하면 된다. 그냥 `cat` 을 실행하면 Stdin (Standard in) 으로 한줄을 입력받고 바로 Stddout (Standard out) 으로 바로 출력한다. 만약 파일에 내용을 저장하려면 `cat > <filepath>` 를 실행하면 된다. 입력을 종료하려면 `C-D` (`ctrl + D`) 를 입력하여 End-of-file signal 을 전송하여 `cat` 을 종료한다.

`tail` 은 파일의 마지막 부분을 출력하는 명령어이다. `tail [-n <number>] <file path>` 와 같이 실행할 수 있다. default 로 마지막 10줄을 출력하며 `-n` 옵션을 사용하여 출력할 line 수를 지정할 수 있다. `tail -f <file path>` 를 실행하면 파일의 내용이 추가되는 것을 바로 확인할 수 있다.

`head` 는 `tail` 과 반대로 파일의 처음 부분을 출력하는 명령이다. `head [-n <number>] <file path>` 와 같이 실행할 수 있다. default 로 처음 10줄을 출력하며 `-n` 옵션을 사용하여 출력할 line 수를 지정할 수 있다.

# 파일 비교

`diff` 를 사용하여 두 파일의 내용을 비교할 수 있다.

`diff <file1> <file2>` 와 같이 실행되는데 대부분 `diff -uNr <file1> <file1>` 와 같이 옵션을 전달하여 사용된다.

- `-u` : diff output format 을 unified format 으로 지정한다. context format 등 다른 format 들도 있지만 보통 `-u` 옵션을 사용한다. format에 대한 자세한 내용은 따로 googling 해보자.
- `-r` : recursive 를 의미한다. 즉, sub-directory 까지 모두 포함하여 실행한다.
- `-N` : 새 파일도 포함하여 실행한다. 존재하지 않는 original file 을 empty file 로 취급한다.

# Make and apply patches using diff and patch command

패치(patch) 파일은 두 파일들간의 차이들을 출력해 주는 프로그램인 `diff` 에 의해 생성된 파일을 의미한다. 주로 쓰이는 때는 어떤 프로그램에서 기능향상이나 문제점을 해결하기 위해 소스파일들을 고치고 나서 고친 부분에 대한 정보만을 기록해 놓고 싶을때 쓰인다. 고친 소스파일 전체보다도 고친 부분에 대한 정보만을 갖고 있으면 저장해야 되는 양이 적고, 어떤 부분을 고쳤는지 파악하기도 쉽다는 장점이 있다. (특히 비공식적인 패치 적용시 프로그램이 버젼업이 되어 소스가 변경되었을때 유용하다.) 패치파일의 확장자는 사용자 임의이긴 하지만 알아보기 쉽도록 주로 `.diff` 또는 `.patch` 를 사용한다.

## diff example

아래와 같이 `hello.c` 라는 file 이 있다.:

```c
#include

int main(void) {
    printf("hello\n");
    return 0;
}
```

위에서 'hello' 라는 문구 대신 '안녕하세요'로 바꾸고 싶다고 하자. 먼저 다음과 같이 위의 `hello.c` 파일을 `hello.c.orig` 라는 파일로 백업해 둔다:

```
$ cp hello.c hello.c.orig
```

그리고 `hello.c` 파일을 다음과 같이 고친다:

```c
#include

int main(void) {
    printf("안녕하세요\n");
    return 0;
}
```

이 두 파일의 차이점을 패치 파일로 기록해 두기 위해 다음과 같이 `diff` 명령을 이용한다.:

```
$ diff -uNr hello.c.orig hello.c > hello-hangul.patch
```

생성된 `hello-hangul.patch` 라는 파일은 단순한 텍스트 파일이다. 그 내용을 보기 위해 다음과 같은 명령을 실행해 보자:

```
$ cat hello-hangul.patch
--- hello.c.orig      Sun Jan 16 16:54:32 2000
+++ hello.c   Sun Jan 16 16:53:04 2000
@@ -2,6 +2,6 @@

int main(void) {
- printf("hello\n");
+ printf("안녕하세요\n");
    return 0;
}
```

고친 파일의 이름, 고친 부분의 아래 위 세줄의 내용과 고친 부분이 -, + 로 표시되어 있는 것을 알 수 있다. 만약, 수정한 파일이 많다면 `diff` 를 file 단위가 아니라 directory 단위로 실행시킬 수 있다:

```
$ diff -uNr [from-directory] [to-directory] > directory_patch.diff
```

paatch file 을 만들기 전에 `make clean` 등을 이용하여 컴파일 과정의 결과로 생성되는 object file 들이나 기타 불필요한 파일들을 정리하고 실행하자.

## Apply patch file: Using patch command

다음은 패치 파일과 변형되지 않은 원래 프로그램 소스 파일을 가지고 있을 때 패치를 적용하는 방법이다. 일단 패치를 적용하기 위해서는 `patch` 라는 명령어를 이용하는데, 그 일반적인 형식은 다음과 같다:

```
$ patch [options] [originalfile [patchfile]]
```

일단 패치 파일을 살펴본다. 패치의 맨 윗줄을 보면 다음과 같이 파일에 관한 정보가 있는 부분이 있다:

```
--- xchat-1.2.0/src/serverlist.h.orig   Wed Aug 25 14:48:57 1999
+++ xchat-1.2.0/src/serverlist.h        Sun Oct 31 18:06:13 1999
```

변경되지 않은 프로그램의 소스 디렉토리로 이동한다음 다음과 같이 `patch` 라는 명령을 이용하여 패치를 한다:

```
$ cd xchat-1.2.0/
$ patch -p1 < ../xchat-1.2.0-serverlist.patch
```

`patch` command 는 입력을 stdin 으로 받을 수 있기 때문에 redirect 를 이용해서 patch file 내용을 전달한다.

`-p` 옵션은 patch file 의 정보에 있는 path 에서 몇 단계를 제외할 지를 나타낸다. 예를 들어 위에서 처럼 `-p1` 옵션을 주면 patch 적용 path 는 xchat-1.2.0 이 제외된 `src/serverlist.h` 가 되고, 현재 위치(directory, path) 를 기준으로 `src/serverlist.h` 파일에 패치를 적용한다. 만약 그 상위디렉토리에서 패치를 적용하기 원한다면 그냥 다음과 같이 하면 될 것이다:

```
$ patch -p0 < xchat-1.2.0-serverlist.patch
```
