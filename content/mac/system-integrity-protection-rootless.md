Title: System Integrity Protection (Rootless)
Date: 2016-12-31
Modified: 2016-12-31
Tags: mac, os x, rootless 
Slug: system-integrity-protection-rootless
Authors: imjang57
Summary: Mac 의 Rootless 기능을 enable 및 disable 하기

# System Integrity Protection (Rootless)

예전에 (2015년 인가..??) OS X 가 _El Capitan_ 으로 업데이트되면서 새롭게 생겨난 시스템 보안 관련 기능이다. _Rootless_ 라고도 하는 기능이다.

보통 Linux/Unix 시스템은 root 사용자가 모든 파일을 읽고 쓸 수 있는데, 이 기능은 _Kernel_ 자체가 System file 들에 대한 쓰기 작업을 아예 막아 버리는 기능이다. 따라서, 이전에는 sudo 등으로 시스템 파일들을 수정할 수 있었지만 이제는 불가능하다.

Rootless 에 의해 보호되는 파일 목록:

- `/System`
- `/bin`
- `/usr`
- `/sbin`

`sudo touch /bin/rootlesstest` 를 실행하면 _Operation not permitted_ 메시지를 볼 수 있다.

_Rootless_ 에 의해 보호되는 파일 목록들은 `/System/Library/Sandbox/rootless.conf` 에 모두 저장되어 있다.

예전에 HomeBrew 때문에 Rootless 를 disable 한 적이 있었는데 이번에 또 필요해져서 다시 찾아봤다. 그리고 이왕 찾아본 김에 기록으로 남긴다.

## Disable Rootless

현재 _Rootless_ 기능의 상태는 아래와 같이 확인할 수 있다.

```bash
$ csrutil status
System Integrity Protection status: enabled.
```

_Rootless_ 기능을 끄려면 _Recovery Mode_ 로 부팅해야 한다.

1. 맥 restart
2. 부팅시작되자마자 `option` 키를 누른 후 `Recovery HD` 를 선택하여 부팅한다. 아니면 `Command` + `R` 을 길게 누르면 파티션 선택 화면을 생략하고 바로 _Recovery Mode_ 로 부팅한다.
3. _Recovery Mode_ 에서 상단 Menu bar 에서 유틸리티(Utilities)메뉴의 터미널(terminal)을 실행한다.
4. `csrutil disable [--without debug]` 실행한다.
5. restart 해서 일반 모드로 부팅한 후 필요한 작업 수행한다.
6. 필요한 작업 끝난 후 다시 재부팅하여 복구 모드로 들어온 뒤 `csrutil enable` 을 실행한다.

# References

- [How to Disable System Integrity Protection on a Mac (and Why You Shouldn’t)](http://www.howtogeek.com/230424/how-to-disable-system-integrity-protection-on-a-mac-and-why-you-shouldnt/)

