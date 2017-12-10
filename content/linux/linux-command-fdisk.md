Title: Linux Partition 관리 : fdisk
Date: 2017-01-18
Modified: 2017-01-18
Tags: linux, disk, partition, fdisk
Slug: linux-command-fdisk
Authors: imjang57
Summary: 리눅스에서 fdisk 명령을 사용하여 파티션(Partition)을 관리하는 방법

# fdisk

`fdisk` 명령은 partition table 을 관리하는 명령이다. 즉, linux 의 disk partition 을 생성, 수정, 삭제할 수 있는 도구이다.

`fdisk` 실행파일의 위치는 `/sbin/fdisk` 이다:

```
# which fdisk
/sbin/fdisk
```

fdisk help:

```
# fdisk -h
Usage:
fdisk [options] <disk> change partition table
fdisk [options] -l <disk> list partition table(s)
fdisk -s <partition> give partition size(s) in blocks
Options:
-b <size> sector size (512, 1024, 2048 or 4096)
-c switch off DOS-compatible mode
-h print help
-u <size> give sizes in sectors instead of cylinders
-v print version
-C <number> specify the number of cylinders
-H <number> specify the number of heads
-S <number> specify the number of sectors per track
#
```

## Disk device name

리눅스에서 디스크장치명은 IDE Disk 인지 SCSI Disk 인지에 따라서 장치명이 주어진다.

IDE Disk 인 경우:

- `/dev/hda` : 첫번째(a) IDE Disk (hd)
- `/dev/hdb` : 두번째(b) IDE Disk (hd)
- `/dev/hdc` : 세번째(c) IDE Disk (hd)

SCSI Disk 인 경우:

- `/dev/sda` : 첫번째(a) SCSI Disk (sd)
- `/dev/sdb` : 두번째(b) SCSI Disk (sd)
- `/dev/sdc` : 세번째(c) SCSI Disk (sd)

그리고 디스크 내에서 파티션이 여러개 나누어진 경우 숫자가 붙어서 장치명이 주어진다:

- `/dev/hda` : 첫번째(a) IDE디스크 전체를 의미
- `/dev/hda1` : 첫번째(a) IDE디스크 내의 첫번째 파티션
- `/dev/hda2` : 첫번째(a) IDE디스크 내의 두번째 파티션

요약하면 다음과 같다.

1. hd 로 시작하면 IDE Disk, sd 로 시작하면 SCSI Disk
2. 뒤에 알파벳이 붙으면 Disk 자체를 의미하고 Disk 는 a 부터 순서대로 Naming 이 이루어짐
3. 뒤에 숫자가 붙으면 Disk 내의 partition 번호를 의미하고 Partition 은 1 부터 순서대로 Naming 이 이루어짐

`fdisk` 를 사용하여 현재 시스템의 디스크와 파티션을 확인하고 새로운 파티션을 추가해보자.

## 디스크 및 파티션 확인하기

`fisk -l` 을 실행하면 현재 시스템의 모든 디스크 및 파티션 정보를 확인할 수 있다.

```
# fdisk -l
Disk /dev/vda: 85.9 GB, 85899345920 bytes
255 heads, 63 sectors/track, 10443 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x0005360e
   Device Boot      Start         End      Blocks   Id  System
/dev/vda1   *           1        1045     8387584   83  Linux
#
```

위의 결과에서 Disk device name 이 `/dev/vda` 로 되어 있는데 오픈스택 가상머신에서 테스트하여 virtual disk 로 디스크가 인식되어 있기 때문이다. 현재 하나의 디스크를 사용하고 있고, 디스크에 하나의 파티션이 사용되고 있음을 알 수 있다. 디스크 용량은 총 85.9 GB 인데, 현재 파티션이 생성된 것은 8225280 bytes 즉 약 8 GB 이다.

## 새로운 파티션 추가하기

특정 디스크에 대해 `fdisk` 명령을 실행하여 파티션 설정을 하려면 `fdisk <device name>` 을 실행한다.

```
# fdisk /dev/vda
WARNING: DOS-compatible mode is deprecated. It’s strongly recommended to
switch off the mode (command ‘c’) and change display units to
sectors (command ‘u’).
Command (m for help):
```

`m` 을 입력하면 어떤 명령을 사용할 수 있는지 도움말을 확인할 수 있다.

```
Command (m for help): m
Command action
a toggle a bootable flag
b edit bsd disklabel
c toggle the dos compatibility flag
d delete a partition
l list known partition types
m print this menu
n add a new partition
o create a new empty DOS partition table
p print the partition table
q quit without saving changes
s create a new empty Sun disklabel
t change a partition’s system id
u change display/entry units
v verify the partition table
w write table to disk and exit
x extra functionality (experts only)
Command (m for help):
```

`p` 를 입력하면 현재 디스크 파티션 상태를 확인할 수 있다. fdisk -l 을 실행한 결과가 같은 내용을 확인할 수 있다.

```
Command (m for help): p
Disk /dev/vda: 85.9 GB, 85899345920 bytes
255 heads, 63 sectors/track, 10443 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x0005360e
   Device Boot      Start         End      Blocks   Id  System
/dev/vda1   *           1        1045     8387584   83  Linux
Command (m for help):
```

이제 `n` 을 입력하여 새로운 파티션을 생성한다. primary partition 으로 생성하기 위해 `p` 를 입력하고, 새로 생성되는 partition 은 2번째 partition 이므로 2 를 입력한다. 그리고 partition 의 크기를 지정하기 위해 First cylinder 와 Last cylinder 를 입력하는데 둘 모두 그냥 Enter 를 입력하여 default 로 설정한다. 그리고 마지막으로 파티션 생성 후 `p` 를 입력하여 새로운 partition 정보를 확인한다.

```
Command (m for help): n
Command action
e extended
p primary partition (1–4)
p
Partition number (1–4): 2
First cylinder (1045–10443, default 1045):
Using default value 1045
Last cylinder, +cylinders or +size{K,M,G} (1045–10443, default 10443):
Using default value 10443
Command (m for help): p
Disk /dev/vda: 85.9 GB, 85899345920 bytes
255 heads, 63 sectors/track, 10443 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x0005360e
   Device Boot      Start         End      Blocks   Id  System
/dev/vda1   *           1        1045     8387584   83  Linux
/dev/vda2            1045       10443    75494789+  83  Linux
Command (m for help):
```

정상적으로 파티션 정보가 생성된 것을 확인한 후 `fdisk` 를 나오기 위해 `w` 를 입력한다. `fdisk` 를 종료할 때 `w` 와 `q` 2가지 명령을 사용할 수 있는데 `w` 는 변경된 내용을 실제 시스템에 적용한 후 종료하는 것이고 `q` 는 작업한 내용을 적용하지 않고 종료하는 것이다.

```
Command (m for help): w
The partition table has been altered!
Calling ioctl() to re-read partition table.
Syncing disks.
#
```

## Partition Type

fdisk prompt 에서 `l` 을 입력하면 Partition type 들의 목록과 Partition Type 의 ID 를 확인할 수 있다.

Swap partition 은 82, Linux partition 은 83, FAT 는 b 또는 c, FreeBSD partition 은 a5 를 ID 로 사용한다.

```
Command (m for help): l
0  Empty           24  NEC DOS         81  Minix / old Lin bf  Solaris        
1  FAT12           39  Plan 9          82  Linux swap / So c1  DRDOS/sec (FAT-
2  XENIX root      3c  PartitionMagic  83  Linux           c4  DRDOS/sec (FAT-
3  XENIX usr       40  Venix 80286     84  OS/2 hidden C:  c6  DRDOS/sec (FAT-
4  FAT16 <32M      41  PPC PReP Boot   85  Linux extended  c7  Syrinx         
5  Extended        42  SFS             86  NTFS volume set da  Non-FS data    
6  FAT16           4d  QNX4.x          87  NTFS volume set db  CP/M / CTOS / .
7  HPFS/NTFS       4e  QNX4.x 2nd part 88  Linux plaintext de  Dell Utility   
8  AIX             4f  QNX4.x 3rd part 8e  Linux LVM       df  BootIt         
9  AIX bootable    50  OnTrack DM      93  Amoeba          e1  DOS access     
a  OS/2 Boot Manag 51  OnTrack DM6 Aux 94  Amoeba BBT      e3  DOS R/O        
b  W95 FAT32       52  CP/M            9f  BSD/OS          e4  SpeedStor      
c  W95 FAT32 (LBA) 53  OnTrack DM6 Aux a0  IBM Thinkpad hi eb  BeOS fs        
e  W95 FAT16 (LBA) 54  OnTrackDM6      a5  FreeBSD         ee  GPT            
f  W95 Ext'd (LBA) 55  EZ-Drive        a6  OpenBSD         ef  EFI (FAT-12/16/
10  OPUS            56  Golden Bow      a7  NeXTSTEP        f0  Linux/PA-RISC b
11  Hidden FAT12    5c  Priam Edisk     a8  Darwin UFS      f1  SpeedStor      
12  Compaq diagnost 61  SpeedStor       a9  NetBSD          f4  SpeedStor      
14  Hidden FAT16 <3 63  GNU HURD or Sys ab  Darwin boot     f2  DOS secondary  
16  Hidden FAT16    64  Novell Netware  af  HFS / HFS+      fb  VMware VMFS    
17  Hidden HPFS/NTF 65  Novell Netware  b7  BSDI fs         fc  VMware VMKCORE
18  AST SmartSleep  70  DiskSecure Mult b8  BSDI swap       fd  Linux raid auto
1b  Hidden W95 FAT3 75  PC/IX           bb  Boot Wizard hid fe  LANstep        
1c  Hidden W95 FAT3 80  Old Minix       be  Solaris boot    ff  BBT            
1e  Hidden W95 FAT1
Command (m for help):
```

특정 파티션을 Swap 용으로 사용하고 싶다면 해당 파티션의 타입을 82 로 지정해준다. 만약 3번 파티션을 Swap 으로 사용하고 싶다면 아래와 같이 차례대로 입력한다.

```
Command (m for help): t
Partition number (1–4): 3
Hex code (type L to list codes): 82
Changed system type of partition 3 to 82 (Linux swap)
Command (m for help):
```

## Boot partition 지정하기

Boot flag 를 설정하여 booting 가능한 파티션을 지정할 수 있다.

```
Command (m for help): a
Partition number (1–4): 1
Command (m for help):
```

파티션 정보를 확인하면 아래와 같이 1번 파티션에 Boot 항목이 설정되어 있음을 확인할 수 있다.

```
Command (m for help): p
Disk /dev/vda: 85.9 GB, 85899345920 bytes
255 heads, 63 sectors/track, 10443 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk identifier: 0x0005360e
   Device Boot      Start         End      Blocks   Id  System
/dev/vda1   *           1        1045     8387584   83  Linux
/dev/vda2            1045       10443    75494789+  83  Linux
Command (m for help):
```

## 파티션 삭제하기

파티션을 삭제하려면 `d` 를 입력한다.

```
Command (m for help): d
Partition number (1–4): 2
Command (m for help): w
The partition table has been altered!
Calling ioctl() to re-read partition table.
Syncing disks.
#
```
