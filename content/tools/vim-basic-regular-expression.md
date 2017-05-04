Title: Vim Basic Regular Expression
Date: 2017-05-04
Modified: 2017-05-04
Tags: vim
Slug: vim-basic-regular-expression
Authors: imjang57
Summary: Vim 에서 사용가능한 정규표현식의 기본 사용법에 대한 글이다.

# 정규 표현식 (regular expression)

정규표현식이란 주로 문자열 내에서 검색이나 조작에 사용되는 표현식으로써 특정한 패턴을 가지고 그 패턴에 부합되는 문자열을 찾아내 원하는 일을 수행 할 수가 있다.

정규표현식은 vim, sed, grep, emacs, perl 등 프로그램이나 프로그래밍 언어 등에서 문자열을 다루는 용도로 사용되고 있다.

정규표현식이 쓰이는 모든 프로그램에서 동일한 문법으로 정규표현식을 규정하고 있지는 않는다. 기본적인 내용은 모두 같지만 약간의 표현 형식이 다르다. 즉, 이 글에 작성한 내용은 다른 프로그램이나 언어에서 사용하는 정규표현식과 다를 수 있다.

Vim 의 `:help pattern` 을 참고하자.

# Character

`[ ]` 안에는 알파벳이나 숫자가 올 수 있고 이 안에 나열되어 있는 문자 중 한 문자를 가리킨다. 즉 [abc] 는 검색에서 한 문자처럼 취급을 받는다.

- `[abc]` : a, b, c 문자 중 한 문자
- `b[abc]ll` : ball, bbll, bcll 중 하나

`[ ]` 안에는 문자의 범위가 들어 갈 수도 있다. 대소문자를 구분하니 주의해야 한다.

- `[a-z]` : 소문자 a 부터 z 중 한 문자
- `[0-9]` : 숫자 0 부터 9 중 한 문자
- `[A-Z0-9]` : 대문자 A 부터 Z 와 숫자 0 부터 9 중 한 문자

정규표현식에서 `.` 은 new line 을 제외한 모든 문자를 가리킨다. 즉 알파벳, 공백과 같은 특수문자, 숫자 모두 `.` 로 표현할 수 있다.

`^` 가 `[ ]` 안에 들어오면 안에 나열되어 있는 문자를 제외한 다른 모든 문자를 나타낸다.

- `[^a-z]` : 알파벳 소문자를 제외한 모든 문자

특수문자는 항상 `\` 와 같이 쓰여야 문자 그대로의 의미를 나타낸다. 공백(Space)는 `\ ` 로 Space 앞에 `\` 를 붙여주면 된다.

- `[A-Z][0-9][0-9]` : 첫문자는 무조건 대문자로 시작하고 곧바로 숫자가 2자리 오는 패턴

`^` 는 문자열의 가장 처음을 의미한다. Vim 에서 `/^The` 로 검색을 하게 되면 줄의 맨 처음에 위치한 The 만 찾게 된다. `[ ]` 내에 있던 `^` 과 다른 의미이다.

`$` 는 문자열의 가장 마지막을 의미한다. `/today$` 로 검색하면 줄의 마지막에 위치한 today 만 찾게 된다.

# Iteration

반복을 지정하는 표현식은 문자 뒤에 적어 앞에 있는 문자가 몇 개까지 반복되는 지를 지정한다.

- `*` : 0 번 이상
- `+` : 1 번 이상
- `-` : 0번 혹은 1번

`+` 와 `-` 는 전통적인 Vi 에서는 제공되지 않고 Vim 에서만 사용할 수 있다. 물론 리눅스에 설치되어 있는 Vi 는 Vim 이기 때문에 사용 가능하다.

- `ab*` : b 라는 문자가 없을 수도 있고 한번 이상 올 수도 있다. `a`, `ab`, `abb`, `abbb`, `abbbb`, etc.
- `ab+` : 반드시 b 라는 문자가 한번 이상 와야 한다. `ab`, `abb`, `abbb`, `abbbb`, etc.
- `ab-` : a 뒤에 b가 올 수도 오지 않을 수 도 있다. `a`, `ab`.

`( )` 를 사용하여 문자열을 반복시킬 수도 있다.

- `(abc)*` : abc 문자열이 0번 이상 반복
- `(abc)+` : abc 문자열이 1번 이상 반복

Vim 에서 `/(abc)*` 로 검색 명령을 내리면 Vim 은 모든 문자가 검색결과로 지정된다. `*` 은 0 번도 포함하기 때문이다.

`< >` 를 사용하여 문자열의 범위를 한정할 수도 있다.

- `\<abc\>` : 정확하게 abc 인 것만 찾는다.

정리하면 반드시 줄의 시작은 알파벳 하나 이상으로 시작하고 중간에 하나 이상의 공백 문자 다음에 2개 이상의 숫자가 오는 패턴은 정규표현식으로 다음과 같이 표현된다 : `^[A-Za-z]+ +[0-9][0-9]+`

# Replace

Vim 은 검색과 동시에 치환도 가능하다 : `:<시작줄 번호>,<끝 번호> s/검색어/바꿀단어/옵션`

- `:1,10 s/The/the/gc` : 1번째 줄에서 10번째 줄 사이에 있는 "The" 라는 단어를 "the"로 치환

`g` 라는 옵션은 모든 검색어에 대해 변경을 실시하게 해준다. 만약 `g` 옵션이 없을 경우 한 줄에 2 개 이상의 The 가 있을 경우 첫 번째 `The` 만 `the` 로 변경을 하게 된다.

`c` 라는 옵션은 치환이 발생할 때마다 정말 치환할 것인지를 묻는 prompt 를 출력한다.

이외에 줄 번호를 가리키는 특별한 문자가 있다.

- `.` : 현재 커서가 놓여 있는 줄의 번호 
- `$` : 마지막 줄
- `:.,$ s/The/the/g` : 현재에서 마지막 줄까지 모든 `The` 를 `the` 로 치환
- `:1,$ s/\<be\>/BE/g` : 모든 줄에서 다른 단어에 포함되지 않은 `be` 라는 단어를 검색하여 대문자 `BE` 로 변경

또는 아래와 같이 한번에 전체 문서에 대해서 치환을 수행할 수도 있다.

- `:%s/The/the/g` : 현재에서 마지막 줄까지 모든 `The` 를 `the` 로 치환. `:1,$ s/The/the/g` 와 같다.

# 정규표현식과 변수

`( )` 는 문자열을 하나의 단위로 보게 하는 역할을 하였다. 하지만 치환에 사용 될 경우 변수 역할도 하게 된다.

정규표현식 `([a-z]+) ([0-9]+)` 를 만족하는 문자열 `abcd 100` 가 있을 때, 정규표현식에서는 각 `( )` 을 하나의 단위로 묶으면서 `1`, `2` 와 같은 변수에 대응을 시킨다. 즉, 첫 번째 `( )` 는 `1` 이라는 변수에, 두 번째 `( )` 는 `2` 라는 변수에 저장된다.

정규표현식의 변수와 Vim 의 치환을 사용하여 앞 뒤 순서를 바꿀 수 있다 : `:1,$ s/([a-z]+)( +)([0-9]+)/321/g`

`s/.../.../g` 와 같은 치환 형식에서 찾을 문자열 부분은 세 개의 `( )` 로 이루어져 있어서 각각 변수 `1`, `2`, `3` 에 저장된다. 그리고 치환할 문자열 부분에서 `321` 과 같이 반대 순서로 변수를 나열하여 각 문자열들의 순서를 변경할 수 있게 된다.