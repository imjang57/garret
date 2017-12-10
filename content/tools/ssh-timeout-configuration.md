Title: SSH Timeout Configuration
Date: 2017-01-02
Modified: 2017-01-02
Tags: ssh, timeout
Slug: ssh-timeout-configuration
Authors: imjang57
Summary: SSH 접속 시 Timeout 설정하는 방법

# SSH Timeout 관련 설정

`/etc/ssh/sshd_config`:

```
TCPKeepAlive yes
ClientAliveInterval 30
ClientAliveCountMax 99999
```

restart sshd:

```
$ systemctl restart sshd
```
