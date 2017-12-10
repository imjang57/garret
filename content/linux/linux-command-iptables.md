Title: iptables
Date: 2017-01-01
Modified: 2017-01-01
Tags: iptables
Slug: linux-command-iptables
Authors: imjang57
Summary: iptables 사용법

# iptables

_iptables_ 는 리눅스에서 네트웍 방화벽으로 사용되는 도구이다. Source, Destination, Protocol, State 등으로 다양한 조건을 설정할 수 있다. 리눅스 호스트에서 제공되는 가장 기초적인 방화벽 도구이며, C언어로 작성된 packet filtering framework 인 [netfilter](https://www.netfilter.org) 를 기반으로 동작한다. 사실은 iptables 가 netfilter 의 하위 프로젝트라고 볼 수도 있다. 보통 _netfilter/iptables_ 와 같이 함께 언급되기도 한다.

- [netfilter](http://www.netfilter.org)
- [iptables](https://www.netfilter.org/projects/iptables/index.html)
- [netfilter git repository](https://git.netfilter.org/)
- [iptables git repository](https://git.netfilter.org/iptables/)

대부분의 리눅스 배포판에서 _iptables_ 는 기본적으로 제공된다. `iptables` 명령으로 방화벽 정책 관련 작업을 수행할 수 있고 _iptables-service_ 패키지를 설치하면 Daemon 형태로 관리가 가능하다.

_iptables_ 에서 사용되는 정책(Rule)을 저장하기 위한 파일의 위치는 `/etc/sysconfig/iptables` 이다.

참고로, CentOS 7 부터는 _iptables_ 대신 [firewalld](http://www.firewalld.org) 가 사용된다. 클라우드 환경에서의 조금 더 유연한 방화벽 관리를 위해 python 으로 만든 도구인데, 내부적으로는 _netfilter/iptables_ 를 사용한 front-end for the iptables 이다. 사용자 입장에서는 그저 명령어를 `iptables` 대신에 `firewall-cmd` 나 `firewall-config` 를 사용하게 된 것이다. CentOS 7 에는 _iptables_ 자체는 있지만 _iptables-service_ 가 없어서 _firewalld_ 로 방화벽을 관리하도록 하는데, 사실 _filrewalld_ 를 끄고, _iptables-service_ 를 설치한 후 사용할 수도 있다(인터넷에 찾으면 많이 나온다). 하지만 이왕 바뀐거 나중에 다시 롤백되지 않을 가능성이 크니 익숙해지는게 좋을 테고 익숙해지면 _Redhat_ 이 _firewalld_ 를 선택한 이유도 알게 될 지도.. 어쨌든 이 글에선 _firewalld_ 에 대해선 다루지 않는다.

만약 iptables 가 설치되어 있지 않다면 아래와 같이 설치하자.

```bash
$ yum install iptables iptables-service
```

## tables

_iptables_ 는 4개의 _table_ 을 관리한다.

- _filter_
- _nat_
- _mangle_
- _raw_

보통 사용하는 _table_ 은 _filter_ 이다.

## chain

_filter table_ 에는 _INPUT_, _OUTPUT_, _FORWARD_ 3개의 _chain_ 이 있다. 각 _chain_ 들은 Network Traffic (IP Packet) 에 대하여 정해진 규칙들을 수행한다.

- _INPUT_ : Host 를 향해 들어오는 Packet
- _OUTPUT_ : Host 에서 나가는 Packet
- _FORWARD_ : Host 가 Destination 이 아닌 Packet

_INPUT chain_ 에 해당하는 Packet 을 허용(_ACCEPT_), 거부(_REJECT_), 또는 드랍(_DROP_) 할 지 결정할 수 있다.

## match

어떤 Packet 에 규칙을 적용할지 판단하기 위한 조건이다.

- `--source` (`-s`) : Source IP address 또는 Network
- `--destination` (`-d`) : Destination address 또는 Network
- `--protocol` (`-p`) : Protocol
- `--in-interface` (`-i`) : 입력 interface
- `--out-interface` (`-o`) : 출력 interface
- `--state` : 연결 상태
- `--string` : Application Layer Data 의 Byte 순서
- `--comment` : Kernel memory 내의 규칙과 연계되는 최대 256 bytes 주석
- `--syn` (`-y`) : SYN Packet 을 허용하지 않음
- `--fragment` (`-f`) : 두 번째 이후의 조각에 대해서 규칙을 명시
- `--table` (`-t`) : 처리될 table
- `--jump` (`-j`) : 규칙에 맞는 Packet 을 어떻게 처리할 것인가를 명시
- `--match` (`-m`) : 특정 module 과의 매치

## target

Packet 에 적용하려는 동작이다.

- _ACCEPT_ : Packet 을 받아들인다.
- _DROP_ : Packet 을 버린다. Packet 을 송신한 쪽은 아무런 응답도 받지 못한다.
- _REJECT_ : Packet 을 버리고 이와 동시에 적절한 응답 패킷(connection refused)을 전송한다.
- _LOG_ : Packet 을 syslog에 기록한다.
- _RETURN_ : 호출 체인 내에서 Packet 처리를 계속한다.

## 연결 추적(Connection Tracking)

_iptables_ 는 연결 추적(connection tracking)이라는 방법을 사용하여 내부 Network 상 서비스 연결 상태에 따라서 그 연결을 감시하고 제한할 수 있게 해준다. 연결 추적 방식은 연결 상태를 표에 저장하기 때문에, 다음과 같은 연결 상태에 따라서 시스템 관리자가 연결을 허용하거나 거부할 수 있다.

- _NEW_ : 새로운 Connection 을 요청하는 Packet, (예: _HTTP_ 요청)
- _ESTABLISHED_ : 기존 Connection 의 일부인 Packet
- _RELATED_ : 기존 Connection 에 속하지만 새로운 Connection 을 요청하는 Packet, 예를 들면 접속 port 가 20인 수동 FTP의 경우 전송 포트는 사용되지 않은 1024 이상의 어느 port 라도 사용 가능하다.
- _INVALID_ : 연결 추적표에서 어디 Connection 에도 속하지 않은 Packet

상태에 기반(stateful)한 _iptables_ 연결 추적 기능은 어느 Network Protocol 에서나 사용 가능하다. _UDP_ 와 같이 상태를 저장하지 않는 (stateless) Protocol 에서도 사용할 수 있다.

## 명령어(commond)

_iptables_ 에서 사용 가능한 명령들의 목록:

- `-A` (`--append`) : 새로운 규칙을 추가한다.
- `-D` (`--delete`) : 규칙을 삭제한다.
- `-C` (`--check`) : 패킷을 테스트한다.
- `-R` (`--replace`) : 새로운 규칙으로 교체한다.
- `-I` (`--insert`) : 새로운 규칙을 삽입한다.
- `-L` (`--list`) : 규칙을 출력한다.
- `-F` (`--flush`) : _chain_ 으로부터 규칙을 모두 삭제한다.
- `-Z` (`--zero`) : 모든 _chain_ 의 패킷과 바이트 카운터 값을 0으로 만든다.
- `-N` (`--new`) : 새로운 _chain_ 을 만든다.
- `-X` (`--delete-chain`) : _chain_ 을 삭제한다.
- `-P` (`--policy`) : 기본정책을 변경한다.

추가로 `-L` 옵션 이용시 `-n` (`--numeric`) 옵션을 추가하면 address 와 port 를 더 편하게 볼 수 있다. (`iptables -nL`)

내용을 확인할 때 `--line-numbers` 를 추가하면 각 Ruleset 들의 순서도 같이 확인할 수 있다.

`-v` (`--verbose`) 옵션을 사용하면 더 다양한 정보를 볼 수 있다.

추가 사용법은 `-h` (`--help`) 를 확인하자.

## 기본 동작

다음은 _iptables_ 의 기본 동작 과정이다.

패킷에 대한 동작은 위에서 부터 차례로 각 규칙에 대해 검사하고, 그 규칙과 일치하는 패킷에 대하여 타겟에 지정한 _ACCEPT_, _DROP_ 등을 수행한다.

규칙이 일치하고 작업이 수행되면, 그 패킷은 해당 규칙의 결과에 따리 처리하고 체인에서 추가 규칙을 무시한다.

패킷이 체인의 모든 규칙과 매치하지 않아 규칙의 바닥에 도달하면 정해진 기본정책(policy)이 수행된다.

기본 정책은 policy _ACCEPT_, policy _DROP_ 으로 설정할 수 있다.

일반적으로 기본정책은 모든 패킷에 대해 _DROP_ 을 설정하고 특별히 지정된 포트와 IP주소등에 대해 _ACCEPT_ 를 수행하게 만든다.

# iptables 사용하기

iptables 적용 예:

- `iptables -P INPUT ACCEPT` : _INPUT Chain_ 의 기본 정책을 _ACCEPT_ 로 설정
- `iptables -P INPUT DROP` : _INPUT Chain_ 의 기본정책을 _DROP_ 으로 설정
- `iptables -F` : _Chain_ 에 정의된 모든 규칙을 삭제
- `iptables -nL` : 현재 ruleset 설정 확인(address 와 port 는 숫자로 출력)
- `iptables -A INPUT -i lo -j ACCEPT` : _INPUT Chain_ 에 localhost interface 인 Packet 은 모두 _ACCEPT_
- `iptables -A INPUT -m state — state ESTABLISHED,RELATED -j ACCEPT` : _INPUT Chain_ 에 state module 의 state 가 _ESTABLISHED_, _RELATED_ 인 Packet 에 대해 _ACCEPT_
- `iptables -A INPUT -p tcp -m tcp — dport 22 -j ACCEPT` : _INPUT Chain_ 에 Protocol 의 _TCP_ 이며 destination port 가 22번인 Packet 에 대해 _ACCEPT_

`service iptables save` 명령을 실행하면 `/etc/sysconfig/iptables` 에 _iptables_ 현재 설정이 저장된다.

_iptables_ 규칙을 만들 때는 순서가 매우 중요하다. 예를 들어 만일 _chain_ 에서 local network 인 192.168.100.0/24 subnetwork 에서 들어오는 모든 packet 을 _DROP_ 하도록 지정한 후 (_DROP_ 하도록 지정된 subnetwork 에 포함되는) 192.168.100.13 에서 들어오는 packet 을 모두 허용하는 _chain_ (`-A`)을 그 후에 추가하면 뒤에 추가된 추가 규칙이 무시된다. 먼저 192.168.100.13 을 허용하는 규칙을 설정한 후 subnet 을 _DROP_ 하는 규칙을 설정해야한다.

HTTP Web Server 를 용할 경우:

```
iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
```

HTTPS:

```
iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
-A INPUT -m state --state NEW -m tcp -p tcp -m multiport --dports 80,443 -j ACCEPT
```

MySQL (port 3306):

```
iptables -A INPUT -p tcp --dport 3306 -j ACCEPT
```

FTP(passive mode):

```
iptables -A INPUT -p tcp --dport 21 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 21 -j ACCEPT
iptables -A INPUT -p tcp --dport 1024:65535 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 1024:65535 -j ACCEPT
```

NTP 시간동기화:

```
iptables -A INPUT -p udp --dport 123 -j ACCEPT
```

# 서버의 취약점을 차단하기 위한 iptables 설정 예

NULL 패킷 차단: `iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP`

NULL 패킷은 정찰 패킷으로 서버설정의 약한 곳을 찾기위한 방법으로 사용된다.

# 기타 사용법

기타 _iptables_ 사용법에 대해 알아보자.

## iptables 수정

등록된 _iptables_ 를 수정하는 방법은 `/etc/sysconfig/iptables` 에서 직접 vi로 수정하거나 `iptables` 명령어를 사용한다.

실행 순번을 확인하기: `iptables -nL --line-number`

순번 3의 행을 수정(replace, `-R`): `iptables -R INPUT 3 -p tcp --dport 2222 -j ACCEPT`

## 인터페이스 지정

Network interface 를 지정하여 _iptables_ 를 적용할 수도 있다.

루프백 인터페이스에 대해 모든 패킷을 허용: `iptables -A INPUT -i lo -j ACCEPT`

랜카드 지정에 대해 모든 패킷을 허용: `iptables -A INPUT -i eth0 -j ACCEPT`

## IP 주소 지정

IP address 를 지정하여 iptables 를 적용할 수도 있다.

신뢰할 만한 ip에 대해 모든 패킷을 허용: `iptables -A INPUT -s 192.168.0.3 -j ACCEPT`

신뢰할 만한 ip 대역에 대해 모든 패킷을 허용: `iptables -A INPUT -s 192.168.0.0/24 -j ACCEPT`

신뢰할 만한 ip 대역에 대해 모든 패킷을 허용: `iptables -A INPUT -s 192.168.0.0/255.255.255.0 -j ACCEPT`

신뢰할 만한 ip와 MAC주소에 대해 모든 패킷을 허용: `iptables -A INPUT -s 192.168.0.3 -m mac — mac-source 00:50:80:FD:E6:32 -j ACCEPT`

포트 범위지정: `iptables -A INPUT -p tcp --dport 6881:6890 -j ACCEPT`

# 자동화 스크립트

자주 방화벽 설정을 초기화하고 재설정해야 한다면 자동화 스크립트를 짜놓는게 좋다. 아래는 그에 대한 예이다.

```bash
#!/bin/bash
# iptables 설정 자동화 스크립트
# 입맛에 따라 수정해서 사용합시다.
iptables -F
# TCP 포트 22번을 SSH 접속을 위해 허용
# 원격 접속을 위해 먼저 설정합니다
iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT
# 기본 정책을 설정합니다
iptables -P INPUT DROP
iptables -P FORWARD DROP
 iptables -P OUTPUT ACCEPT
# localhost 접속 허용
iptables -A INPUT -i lo -j ACCEPT
# established and related 접속을 허용
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
# Apache 포트 80 허용
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
# 설정을 저장
/sbin/service iptables save
# 설정한 내용을 출력
iptables -L -v
위 내용을 입맛에 맞게 수정한 후에 저장(myfirewall)
권한부여: chmod +x myfirewall
실행: ./myfirewall
```

# References

- http://webdir.tistory.com/170

