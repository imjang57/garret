Title: SSH Brute force 막기
Date: 2017-01-12
Modified: 2017-01-12
Tags: ssh, iptables, brute force
Slug: defence-ssh-brute-force
Authors: imjang57
Summary: SSH Brute force 공격 시도를 막는 설정

# ssh brute force 막기

AWS EC2 를 사용하고 있었는데 갑자기 인스턴스가 엄청나게 느려졌다. 확인해보니 SSH 연결 시도가 엄청나게 쌓이고 있었다. 인터넷에서 Source 주소를 입력해서 찾아보니 중국이라고 나오는데 그거는 뭐 알 수 없는 거고.. 어쨌든 Security Group 을 22번 포트에 대해 그냥 다 열어놨더니 이런 일이 발생했나보다. 그래도 진짜 공격 받아보긴 처음이네 ㅎㅎ..

어쨌뜬 그래서 이 글에 brute force 방식으로 SSH 비밀번호를 해킹하려는 시도를 차단하기 위한 설정을 남긴다. (물론 AWS 인스턴스는 Security Group 을 내 주소로만 SSH 허용하도록 바꿔서 문제없지만 나중에 필요하게 될지 모르니....)

brute force 공격이 들어오면 매번 로그인 시도때마다 SSH 서버의 Resource 가 소모되기 때문에 보안성이 좋은 비밀번호나 키를 사용하더라도 이를 방지해주는 것이 좋다.

ssh port 로 20초간 5회 이상 접속을 시도하면 10분간 접속을 차단하는 iptables rule 을 만들어 보자.

blacklist 와 ssh chain 생성:

```
# iptables -N blacklist
# iptables -N ssh
```

INPUT chain 에서 state module 로 ssh port 에 접속이 시작되면 ssh chain 으로 보낸다.

```
# iptables -A INPUT -m state --state NEW -p tcp --dport ssh -j ssh
```

blacklist chain 에서는 recent module 로 "blacklist" 라는 목록에 접속 주소를 기록하고 접속을 거부한다.

```
# iptables -A blacklist -m recent --set --name blacklist
# iptables -A blacklist -j REJECT
```

ssh chain 은 다음과 같다.

```
# iptables -A ssh -m recent --update --seconds 600 --hitcount 1 --name blacklist -j REJECT
# iptables -A ssh -m recent --set --name ssh
# iptables -A ssh -m recent --update --seconds 20 --hitcount 5 --name ssh -j blacklist
# iptables -A ssh -j ACCEPT
```

이 ssh chain 은 다음과 같이 동작한다.

1. 접속 주소가 이미 blacklist 에 들어 있고 지난 10분간 1회 이상 접속이 있었으면 접속을 거부한다.
2. 접속 주소를 "ssh" 목록이 기록한다.
3. 접속 주소가 이미 "ssh" 목록에 있으면, 지난 20초간 5회 이상 접속이 있었으면 blacklist chain 으로 보낸다.
4. 위의 3개가 다 통과하면 ssh 접속을 허락한다.

