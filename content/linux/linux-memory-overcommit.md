Title: Linux Memory overcommit
Date: 2017-01-23
Modified: 2017-01-23
Tags: linux, memory, overcommit
Slug: linux-memory-overcommit
Authors: imjang57
Summary: 리눅스에서 새로운 프로세스가 실행될 때 메모리 할당하는 과정과 overcommit 설정에 대한 설명

# Linux Memory and Over commit

개발한 자바 프로그램을 리눅스에서 실행시키려고 하는데 특정 서버에서만 계속 아래와 같은 메시지를 출력하면서 실행이 되지 않았다.

```
There is insufficient memory for the Java Runtime Environment to continue.
Native memory allocation (malloc) failed to allocate 4088 bytes for AllocateHeap
An error report file with more information is saved as:
/home/imjang57/hs_err_pid1234.log
```

잠시동안 삽질하다 보니 Linux 의 overcommit 설정때문이라는 것을 알았다.

## Linux Memory

자세히 알아보기 전에 먼저 리눅스에서 프로세스가 실행될 때 어떻게 메모리가 할당되는지 얘기해보자.

리눅스 시스템은 가상 메모리(Virtual Memory)라는 오래된 개념으로 물리 메모리(Physical Memory)보다 많은 메모리를 사용할 수 있다. (물론 윈도우도 똑같다.) 프로세스는 각각 독립적인 주소 공간을 가지고 있고, 메모리는 Page 라는 최소 단위로 할당된다. 이들 독립적인 주소 공간들은 가상 메모리에 할당된다. 그리고 실제로 프로세스가 필요한 부분만 물리 메모리에 할당하는 Demand-Paging 이라는 방법으로 메모리를 사용한다.

물리 메모리를 넘어가는 메모리 공간을 저장하기 위해 Disk 의 특정 영역을 사용하게 되는데 이를 Swap 이라고 한다. 그리고 물리 메모리를 넘어가는 메모리 영역을 사용하기 위해 Disk 에 Page file 을 쓰고, 다시 메모리로 load 하는 작업들을 하게 된다. 이 작업들을 swap-in, swap-out 이라고 하고 Page 단위로 발생한다.

자세히 들어가면 Page Table, Page, Page-in/Page-out, Copy on Write, Page replacement algorithm 등등 알아야 할게 많으니 넘어가자. 나도 오래되서 정확하게 기억 안난다. ^^;; 궁금한 내용은 Operating System 공부를 하자.

참고로, 리눅스에서 Swap 을 사용하는 빈도를 확인할 수 있다.

```
$ cat /proc/sys/vm/swappiness
60
$ sysctl vm.swappiness
vm.swappiness = 60
```

일반적으로 위의 내용처럼 60이 기본값으로 되어 있다. `vm.swappiness` 는 swap 영역을 얼마나 사용할 지를 나타내는 값이다. 0으로 설정하면 swap 을 최대한 사용하지 않는다는 뜻이고 100이면 swap 을 최대한 사용한다는 뜻이다.

`vm.swappiness` 값 변경은 아래 명령을 실행하면 된다.

```
$ sysctl vm.swappiness=0
$ echo 0 > /proc/sys/vm/swappiness
```

또는 `/etc/sysctl.conf` 에 `vm.swappiness=0` 을 추가하면 된다.

현재 사용되고 있는 swap 현황을 알고 싶으면 다음과 같이 하면 된다.

```
$ cat /proc/meminfo | grep Swap
SwapCached: 0 kB
SwapTotal: 0 kB
SwapFree: 0 kB
```

## Linux Memory Commit

리눅스에서 프로세스가 실행될 때 Memory Commit 이라는 작업이 수행된다. `malloc()` 등과 같은 시스템 콜(System call)을 사용하여 메모리 할당 요청을 할 때, 시스템 콜은 메모리 영역을 할당해서 주소를 리턴한다. 이때, 실제로 물리 메모리에 할당되는 것은 아니다. 단지 메모리 영역만 만들고 실제 사용될 때가 되어야 물리 메모리에 올라가게 된다.

`fork()` 등의 시스템 콜로 새로운 자식 프로세스를 생성할 때, 자식 프로세스는 부모 프로세스의 메모리 영역을 그대로 복사한다. 그래서 메모리를 많이 쓰는 프로세스에서 `fork()` System call 을 사용하면 매우 많은 메모리가 필요하게 된다. 즉, `fork` 한 후에 `exec` 가 수행되기 전까지 실제로는 자식 프로세스에서 사용되지 않는 메모리들을 commit 하게 된다.(참고로, `fork` 는 새로운 프로세스를 시작할 때 메모리 공간을 복사하지만 `exec` 는 새로운 프로세스를 실행할 때 현재 메모리 공간을 덮어쓴다. 하지만 `exec` 는 `exec` 가 실행된 이후의 로직들은 실행되지 않고 사라지게 된다.)

## Linux overcommit

리눅스에서는 가상 메모리로 인해 물리 메모리보다 많은 메모리를 사용할 수 있다. 그리고 overcommit 이라는 개념을 적용하여 이를 제어할 수 있게 한다. 리눅스는 새로운 프로세스가 실행될 때 overcommit 설정에 따라서 다음과 같은 행동들 중 하나를 선택한다.

- 메모리가 부족하면 임의의 프로세스를 종료시켜서 메모리를 확보
- 메모리가 부족해도 일단 프로세스 실행
- 프로세스 실행을 중지하고 에러 발생

리눅스가 임의로 프로세스를 종료시킬 때 사용되는 모듈을 __OOM Killer(Out Of Memory Killer)__ 라고 한다. OOM Killer 의 동작은 `vm.overcommit_memory`, `vm.overcommit_ratio` 설정에 의존적이다. `overcommit_memory` 가 0이면 Heuristic method, 1 이면 overcommit 사용, 2는 overcommit_ratio 에 따라 제한하게 된다.

- 0: 휴리스틱하게 overcommit 여부를 결정한다. 보통 기본설정이다. 메모리에 대한 요구가 발생했을 때 메모리 공간이 부족하면 실행 중인 프로세스를 강제로 종료시켜 메모리를 확보한다. Page Cache + Swap Memory + Slab Reclaimable 값을 기준으로 결정한다. kernel 의 소스에서 `mm/mmap.c` 를 참고하자.
- 1: 항상 overcommit 을 허용한다. 메모리가 실제로 부족해도 충분한 메모리가 있는 것처럼 동작하게 된다.
- 2: overcommit 허용하지 않는다. 메모리가 부족할 경우 메모리 할당 요청한 프로세스를 실행하는게 아니라 에러를 발생시킨다. Swap size + (Ram size * `vm.overcommit_ratio`/100) 의 공식에 따라 결정된다.

OOM Killer 에 의해 죽으면 아래와 같은 에러가 발생한다.

```
May 8 11:18:50 mimul01 kernel: Out of memory: Kill process 3121
(malloc_test) score 884 or sacrifice child
```

프로세스가 Commit 요청 가능한 크기는 `/proc/meminfo` 의 내용으로 확인할 수 있다. CommitLimit 은 요청 가능한 크기의 최대값, Committed_AS 는 사용량을 나타낸다.

```
$ cat /proc/meminfo | grep Commit
CommitLimit: 4030664 kB
Committed_AS: 67748 kB
```

Overcommit 설정은 제한된 메모리에서 보다 많은 프로세스를 띄우고 불필요한 메모리로 인한 공간 낭비를 줄일 수 있다는 장점이 있지만 OS 가 프로세스를 임의로 종료시켜 버릴 수 있다는 위험도 있다. 실제 운영에 사용되는 서버라면 매우 조심해야 할 상황이 발생할 수 있다.

현재 overcommit 설정 혹인은 다음과 같이 하면 된다.

```
$ sysctl -a | grep overcommit
vm.overcommit_memory = 0
vm.overcommit_ratio = 50
vm.overcommit_kbytes = 0
vm.nr_overcommit_hugepages = 0
```

또는

```
cat /proc/sys/vm/overcommit_memory
0
cat /proc/sys/vm/overcommit_ratio
50
cat /proc/sys/vm/oom_kill_allocating_task
0
```

overcommit 설정을 변경하려면 다음과 같이 하면 된다.

```
$ sysctl vm.overcommit_memory=1
```

또는 `/etc/sysctl.conf` 에 아래 내용을 추가

```
vm.overcommit_memory=1
```

## Linux overcommit test

참고로 overcommit 동작에 대해 테스트해보자.

다음 코드는 `malloc()`만 하고 메모리에 쓰는 작업은 하지 않는 코드다.

```
while(1) {
  block = (void *) malloc((double) GIGABYTE);
  printf("Allocated memory.\n");
  sleep(1);
}
```

그리고 다음 코드는 메모리에 쓰는 작업까지 한다.

```
while(1) {
  block = (void *) malloc((double) GIGABYTE);
  memset(block, 1, GIGABYTE);
  printf("Allocated memory.\n");
  sleep(1);
}
```

적절하게 할당하는 메모리 값을 변경해가며 테스트해보자.

# References

* Linux overcommit handling modes 에 대한 문서: https://www.kernel.org/doc/Documentation/vm/overcommit-accounting
* vm.overcommit에 대한 짧은 이야기: https://brunch.co.kr/@alden/16
