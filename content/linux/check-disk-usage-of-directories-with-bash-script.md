Title: Bash script 로 각 디렉터리들의 실제 사용량 조회하기
Date: 2017-01-18
Modified: 2017-01-18
Tags: bash, linux, du, disk
Slug: check-disk-usage-of-directories-with-bash-script
Authors: imjang57
Summary: Bash script 로 각 디렉터리들이 실제 사용하고 있는 디스크 크기를 알아보는 방법

# Linux 에서 각 디렉터리 별 디스크 사용량 확인하기

리눅스에서 각 디렉터리마다 디스크를 얼마나 사용하고 있는지 확인하기 위한 bash script 이다.

스크립트:

```bash
# make newlines the only seperator (IFS : Internal Field Separator)
IFS=$'\n'; for d in $(ls -l | grep '^d' | awk '{ print substr($0, index($0, $9)) }'); do du -hs $d; done
```

처음에 `IFS` 를 지정해주지 않으면 디렉터리 이름에 공백이 들어간 경우 디렉터리 이름이 공백을 기준으로 split 되어 별도의 디렉터리처럼 동작하게 된다.

나머지들은 워낙 기본적인 것들이니 간단하게 언급만 하면, 현재 디렉터리의 파일 목록을 조회하고, `grep` 으로 디렉터리만 뽑아내고, `awk` 로 파일 이름만 뽑아내고, `for` statement 를 사용해서 각 디렉터리마다 `du` 명령을 사용한다.

