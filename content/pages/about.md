Title: About
Slug: about
Authors: imjang57

# Hello

개인적으로 나중에 혹시나 쓸 일이 있을까 하는 것들을 적는 곳입니다. 사실 나중에 다시 찾기 귀찮아서.. 그러니까 글들이 불친절하게 작성되었습니다.

즉, 여기 글들은 게으른 개발자가 되기 위한 개인적인 목적으로 만들어 졌습니다.

# 개발자를 게으르게 만들어 줄 수 있는 것들

개발자는 게을러 지기 위한 고민을 항상 해야 한다. 어떻게 더 편하게, 더 쉽게 더 간단하게, 자동으로 처리할 수 있을지 고민하자. 그리고 남는 시간에 놀거나 문제 해결에 집중하자.

## 개발자가 최대한 키보드만 사용하면 좋은 이유

- 마우스는 매우 직관적인 인터페이스라 프로그램 사용자에게는 편하다. 하지만 추상적인 것을 찾아 구체화하는 일을하는 개발자에게는 맞지 않는다.
- 마우스는 몰입(flow)에 방해된다. 단축키나 매크로를 사용한 키보드보다 속도가 느리다. 손이 마우스와 키보드를 왔다 갔다 하는 것은 번거롭고 일을 느리게 만든다.

### Why Terminal? Why keyboard rather than mouse?

[A Byte of Vim](http://files.swaroopch.com/vim/byte_of_vim_v051.pdf) 이라는 책에 보면 다음과 같이 언급한다.

Because once a person becomes efficient at typing, using only the keyboard makes the person much faster and less error-prone, as opposed to using the mouse. This is because the hand movement required to switch between the keyboard and the mouse is slow and there is a context switch required in the mind of the person when shifting the hand between the keyboard and the mouse. If we make it a habit to use the keyboard as much as possible, you're saving valuable hand movement.

## 콘솔 환경에 익숙해져야 하는 이유 Command Line Interface

- 내가 원하는 작업을 자동화하여 반복 작업의 수행을 편하게 하고 문제 해결에 시간을 더 사용할 수 있게 해준다.
- 마우스 사용 억제 습관을 기를 수 있다.
- GUI 는 기능이 제한적이고 제공되는 기능만 사용할 수 있다. CLI 에서 Script 를 구현하면 얼마든지 내가 원하는 작업을 자유롭게 만들 수 있다.
- AWK, SED, GREP 등 좋은 툴들이 많고, Bash, Python 등 좋은 스크립트 도구도 많다. Pipe, Redirection 등의 interface 는 매우 유용하다. 적극적으로 사용하자.
- 대부분의 경우 프로그램은 개발자가 만들고, 개발자는 CLI 에 익숙하고, 다른 개발자를 위해 CLI 명령을 잘 만들어 놓는다.

## 정규표현식 Regular Expression

- 텍스트를 다루는데 엄청난 편의성을 제공한다.
- 개발은 소스코드를 작성하면서 진행되고, 소스코드는 텍스트다. 검색, 치환 등에 매우 좋다.
- 특히 vi, sed 등은 정규표현식을 알면 매우 큰 생산성 향상을 경험할 수 있다.

## 터미널 기반 텍스트 에디터

- 운영에서 사용되는 리눅스나 유닉스는 GUI Desktop Environment 가 없는 경우가 많다. 보편적으로 사용되는 SSH 로 접속한 경우에는 어떤 에디터를 사용할 것인가? 적어도 기본 에디터인 nano 나 vi 는 알아 놓는게 좋다. cat, sed, awk 까지 알면 더할 나위 없다.
- Eclipse, IntelliJ 등 IDE 나 GUI 에디터도 좋다. 이들은 뛰어난 Analysis 기능과 Assistant 기능을 제공하고 코드 작성과 디버깅에 편의성을 제공한다. 하지만 키보드만 이용한 작업에는 vi 가 아직은 가장 좋고 언어나 환경 등에 상관없이 범용적으로 유용하게 사용할 수 있다. 둘 다 사용할 줄 알아야 한다는 말이다.

## 구글 파워 서칭

- 구글이 짱이다.

