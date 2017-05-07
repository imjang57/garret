Title: Linux 에서 사용자 관리를 위한 명령어들
Date: 2017-01-01
Modified: 2017-05-08
Tags: linux, user
Slug: linux-command-for-user-management
Authors: imjang57
Summary: Linux 에서 사용자 관리를 위한 명령어들(useradd, userdel, usermod, groupadd, groupdel, passwd, who, w, whoami, last, lastlog)

# Linux 에서 사용자 관리를 위한 명령어들

Linux 에서 사용자 추가, 사용자 정보 변경, 사용자 삭제, 그룹 추가, 그룹 삭제, 로그인한 사용자 정보 확인, 로그인 내역 확인 등을 위한 명령어들을 정리한 글이다.

# Login message

각 명령어들에 대해 알아보기 전에 리눅스에 로그인 하면 여러 메시지들이 출력되는 시스템들이 있다. 시스템마다 내용이 다르게 출력되는데 이는 아래의 2가지 파일을 이용해서 만든 것이다. 참고용으로 알고 가자.

- `/etc/motd`
- `/etc/issue`

참고로, motd 는 message of the day 를 의미한다.

# Add new user

`useradd` 와 `adduser` 2개의 명령어가 존재하는데 같은 거다. `adduser` 는 사실 `useradd` 의 symbolic link 이기 때문에 같은 명령어이다.

`useradd` 는 새로운 사용자를 추가하는 명령이다.

`useradd` 는 실행될 때 `/etc/default/useradd` 파일과 `/etc/login.defs` 파일을 참고하여 실행되기 때문에 두 파일의 내용에 따라 결과가 다르게 나타날 수 있다.

`/etc/default/useradd` 파일:

```
# useradd defaults file
GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/bash
SKEL=/etc/skel
CREATE_MAIL_SPOOL=yes
```

예를 들면 `/etc/default/useradd` 파일에 `SKEL` 의 값으로 새로운 사용자의 Home directory 에 생성될 기본 파일들을 지정할 수 있다.

`/etc/login.defs` 파일:

```
#
# Please note that the parameters in this configuration file control the
# behavior of the tools from the shadow-utils component. None of these
# tools uses the PAM mechanism, and the utilities that use PAM (such as the
# passwd command) should therefore be configured elsewhere. Refer to
# /etc/pam.d/system-auth for more information.
#

# *REQUIRED*
#   Directory where mailboxes reside, _or_ name of file, relative to the
#   home directory.  If you _do_ define both, MAIL_DIR takes precedence.
#   QMAIL_DIR is for Qmail
#
#QMAIL_DIR	Maildir
MAIL_DIR	/var/spool/mail
#MAIL_FILE	.mail

# Password aging controls:
#
#	PASS_MAX_DAYS	Maximum number of days a password may be used.
#	PASS_MIN_DAYS	Minimum number of days allowed between password changes.
#	PASS_MIN_LEN	Minimum acceptable password length.
#	PASS_WARN_AGE	Number of days warning given before a password expires.
#
PASS_MAX_DAYS	99999
PASS_MIN_DAYS	0
PASS_MIN_LEN	5
PASS_WARN_AGE	7

#
# Min/max values for automatic uid selection in useradd
#
UID_MIN                  1000
UID_MAX                 60000
# System accounts
SYS_UID_MIN               201
SYS_UID_MAX               999

#
# Min/max values for automatic gid selection in groupadd
#
GID_MIN                  1000
GID_MAX                 60000
# System accounts
SYS_GID_MIN               201
SYS_GID_MAX               999

#
# If defined, this command is run when removing a user.
# It should remove any at/cron/print jobs etc. owned by
# the user to be removed (passed as the first argument).
#
#USERDEL_CMD	/usr/sbin/userdel_local

#
# If useradd should create home directories for users by default
# On RH systems, we do. This option is overridden with the -m flag on
# useradd command line.
#
CREATE_HOME	yes

# The permission mask is initialized to this value. If not specified, 
# the permission mask will be initialized to 022.
UMASK           077

# This enables userdel to remove user groups if no members exist.
#
USERGROUPS_ENAB yes

# Use SHA512 to encrypt password.
ENCRYPT_METHOD SHA512
```

`/etc/login.defs` 파일에도 여러 가지 값들이 있는데 `CREATE_HOME` 값에 따라 `useradd` 가 사용자 Home directory 를 생성할지 여부를 결정하게 된다. 만약 이 값이 `yes` 면 자동으로 생성하고 `no` 면 자동으로 생성하지 않도록 되어 `useradd -d <home path> <username> && mkdir <home path>` 와 같이 `-d` 옵션을 주어 home directory 를 설정하고 home directory 를 직접 생성해주어야 한다.

# Delete user

사용자를 삭제하려면 `userdel` 명령을 사용하면 된다.

`userdel <username>` 을 실행하면 사용자를 삭제한다. 하지만 사용자의 home directory 는 삭제하지 않는다. home directory 도 같이 삭제하려면 `userdel -r <username>` 과 같이 `-r` 옵션을 전달하여 실행한다.

# Change user account

사용자 정보를 변경하는 명령어는 `usermod` 이다.

사용자의 home directory 를 변경하려면 `usermod -d <path> <user>` 를 실행한다.

사용자의 group 을 변경하려면 `usermod -G <groupname>` 을 실행한다. groupname 은 `,` 로 구분되는 여러 group 들이 올 수 있다.

만약 사용자의 group 을 기존 group 에 추가하려 하면 `usermod -aG <groupname>` 을 실행한다.

사용자의 prior group (initial login group) 을 변경하려면 `usermod -g <groupname>` 을 실행한다. `-g` 옵션을 사용하면 home directory 이하의 모든 파일들의 group 도 같이 변경된다. home directory 외부에 있는 파일들을 직접 변경해주어야 한다.

# Change user password

사용자의 login password 를 변경하려면 `passwd` 명령을 사용한다.

`passwd <username>` 을 실행하면 된다.

# Group

새로운 group 을 추가하려면 `groupadd` 명령어를 사용한다. `groupadd <groupname>` 을 하면 새로운 group 이 생성된다.

`groups` 명령어를 사용하면 사용자의 group 목록을 알 수 있다. 그냥 `groups` 를 실행하면 현재 로그인된 사용자의 group 목록을 확인할 수 있으며, 특정 사용자의 group 목록을 확인하려면 `groups <username>` 을 실행한다.

group 을 삭제하려면 `groupdel` 명령을 사용한다.

# Show user informations

사용자 정보와 관련된 여러 내용을 확인하는 명령어들이 있다.

`whoami`, `who am i` 2가지 명령들은 다 같은 명령들인데 현재 로그인 중인 사용자를 보여준다.

`lastlog` 는 각 사용자들 또는 특정 사용자가 최근에 언제 어디에서 로그인했는지 정보를 알려준다.

`last` 는 특정 사용자가 로그인 한 history 를 보여준다. `/var/log/wtmp` 파일의 내용을 보여주는 명령이다. `/var/log/wtmp` 파일은 Text 가 아니라 binary 이기 때문에 last 명령으로만 확인할 수 있다. `last [username]` 과 같이 실행할 수 있는데, 만약 `last reboot` 를 실행하면 시스템이 리부트된 내역을 보여준다.

`who`, 는 현재 누가 로그인한 상태인지를 보여준다. `who -H` 와 같이 `-H` 옵션을 주면 결과에 헤더도 붙일 수 있다.

`w` 는 현재 누가 로그인한 상태이고 어떤 작업을 하고 있는지를 보여준다. Terminal Type, FROM (remote host 의 IP address 또는 domain name), LOGIN@ (접속 시간), IDLE (최종 명령 후 대기 시간), WHAT (현재 사용 중인 Shell 이나 작업 등) 등을 출력한다.

# Related files

Linux 에서 사용자 정보와 관련된 여러가지 파일들이 있다.

- `/etc/passwd` : User account information
- `/etc/shadow` : Secure user account information
- `/etc/group` : Group account information
- `/etc/gshadow` : Secure group account information
- `/etc/login.defs` : Shadow password suite configuration
- `/etc/skel` : Directory containing default files.
