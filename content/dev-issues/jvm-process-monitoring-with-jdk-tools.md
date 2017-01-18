Title: JVM Process monitoring with JDK tools
Date: 2017-01-18
Modified: 2017-01-18
Tags: java, jvm, monitoring, jps, stat, stack
Slug: jvm-process-monitoring-with-jdk-tools
Authors: imjang57
Summary: JDK Tools 을 사용하여 JVM Process 를 모니터링하는 방법에 대한 소개

# JVM Process monitoring

요즘 일 때문에 오랜만에 자바를 사용하고 있고, 스칼라에 관심이 생겨 공부해보고 있다. 그런데 둘다 _JVM_ 기반 언어다 보니 JVM 에 대해 알아야 겠다는 생각이 들었다. (사실 일하다가 JVM 모니터링 할 일이 생긴 김에 간단하게 정리한다.) 어쨌든 둘 다 JVM 에서 동작하는 녀석들이라 JVM 모니터링에 대해 간단하게 남겨보고자 한다.

자바든 스칼라든 실행되면 JVM 프로세스이다. 자바나 스칼라로 쓰여진 코드는 Java Bytecode 로 컴파일되고, JVM 은 이 Bytecode 를 실행한다. 그러므로 컴파일 된 이후에는 자바로 작성했든 스칼라로 작성했든 JVM 입장에서는 그냥 똑같은 Bytecode 이다. 그러니 같은 방법(JVM Process monitoring)으로 모니터링할 수 있다.

# JVM Monitoring tools

_JDK (Java Development Kit)_ 를 설치하면 기본적으로 자바 코드를 컴파일하기 위한 `javac`, 컴파일된 bytecode 를 실행하는 `java` 를 제공한다. 그리고 개발자들을 위한 다양한 도구들을 기본적으로 제공한다. 모니터링을 위해서 아래 도구들을 사용가능하다.(물론 아래 도구들 외에 더 많다.)

- `jps` : JVM Process Status
- `jstat` : JVM Statistics
- `jhat` : Java Heap Analysis Tool
- `jstack` : Java thread Stack traces

_VisualVM_ 과 같은 GUI 도구도 있지만 어쨌든 기본은 CLI 도구들이고, GUI 도구들도 CLI 도구들을 이용하는 형태이다.

# JVM Monitoring

JVM 프로세스를 모니터링하려면 당연히 JVM 프로세스가 있어야 한다. 테스트 프로그램은 임시로 tomcat 을 사용하였다.

- `yum install -y tomcat`
- `passwd tomcat`
- `/etc/passwd` 파일에서 tomcat 계정의 login shell 을 bash 로 지정
- `sudo service tomcat start`
- tomcat 계정으로 전환(`su - tomcat`)

## jps : JVM Process Status

`jps` 를 실행하면 JVM Process 목록과 PID 를 확인할 수 있다.

```
$ jps
17285 Bootstrap
17322 Jps
$ jps -m
17285 Bootstrap start
17398 Jps -m
$ jps -ml
17285 org.apache.catalina.startup.Bootstrap start
17413 sun.tools.jps.Jps -ml
$
```

## jstat: JVM Statistics

`jps` 에서 확인한 PID 로 `jstat` 를 실행할 수 있다. 위에서 tomcat 을 실행하는 Bootstrap 의 PID 가 17285 이므로 이를 이용하여 `jstat` 을 실행하였다. 그리고 1000 밀리초 단위로 통계치를 수집하도록 하였다. 결과는 퍼센트(%)로 출력된다.

```
$ jstat -gcutil 17285 1000
  S0     S1     E      O      M     CCS    YGC     YGCT    FGC    FGCT     GCT   
  0.00  98.44  60.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005
  0.00  98.44  60.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005
  0.00  98.44  60.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005
  0.00  98.44  60.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005
  0.00  98.44  60.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005
$
```

위에서처럼 `-gcutil` 옵션을 사용하면 Java Heap 현황을 확인할 수 있다.

- _GCT_ : Garbage Collection Time (seconds, 누적)
- _FGCT_ : Full GCT (seconds, 누적)
- _FGC_ : Full Garbage Collection 발생 회수
- _M_ : Metaspace 영역의 사용률
- _S0_ : Survivor 0 영역의 사용률
- _S1_ : Survivor 1 영역의 사용률
- _E_ : Eden 영역의 사용률
- _O_ : Old 영역의 사용률
- _CCS_ : Compressed Class Space (part of metaspace)
- _YGC_ : Young GC 발생 회수
- _YGCT_ : Young GC Time (seconds, 누적)

FGCT 열의 값이 계속 증가하면 문제가 있는 것이다.

M 열은 Metadata 를 위한 힙 영역이다. 이 영역은 자바8부터 M(Metaspace)로 표시되기 시작했고 이전 버전까지는 P(Permgen, Permanent Generation) 영역이라고 불리었다. 클래스의 Metadata, JVM 내부 객체 등이 저장되는 중요한 곳이다. 매우 무조건 자바 프로그램의 경우 이 영역에서 `java.lang.OutOfMemoryError` 를 만날 수도 있다.

`-gcutil` 대신 `-gccause` 옵션을 사용하면 `-gcutil` 의 결과에 GC 의 원인까지 확인할 수 있다.

```
$ jstat -gccause 17285 1000
  S0     S1     E      O      M     CCS    YGC     YGCT    FGC    FGCT     GCT    LGCC                 GCC                 
  0.00  98.44  61.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005 Allocation Failure   No GC               
  0.00  98.44  61.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005 Allocation Failure   No GC               
  0.00  98.44  61.41   5.27  96.61  89.46      1    0.005     0    0.000    0.005 Allocation Failure   No GC               
$
```

- _LGCC_ : 지난 GC의 발생 이유
- _GCC_ : 현재 GC의 발생 이유

## jstack: Java thread Stack traces

`jstack` 을 이용하면 현재 Java 프로세스의 stack dump 를 얻을 수 있다. `jstack` 을 이용하면 현재 실행 중인 여러 thread 들의 stack 을 확인할 수 있다.

```
$ jstack 17285
2016-12-26 10:32:20
Full thread dump OpenJDK 64-Bit Server VM (25.111-b15 mixed mode):
"Attach Listener" #17 daemon prio=9 os_prio=0 tid=0x00007f48d0001000 nid=0x458b waiting on condition [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
"ajp-bio-8009-AsyncTimeout" #15 daemon prio=5 os_prio=0 tid=0x00007f491049c800 nid=0x43a9 waiting on condition [0x00007f48f8ba4000]
   java.lang.Thread.State: TIMED_WAITING (sleeping)
 at java.lang.Thread.sleep(Native Method)
 at org.apache.tomcat.util.net.JIoEndpoint$AsyncTimeout.run(JIoEndpoint.java:152)
 at java.lang.Thread.run(Thread.java:745)
"ajp-bio-8009-Acceptor-0" #14 daemon prio=5 os_prio=0 tid=0x00007f491049a000 nid=0x43a8 runnable [0x00007f48f8ca5000]
   java.lang.Thread.State: RUNNABLE
 at java.net.PlainSocketImpl.socketAccept(Native Method)
 at java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:409)
 at java.net.ServerSocket.implAccept(ServerSocket.java:545)
 at java.net.ServerSocket.accept(ServerSocket.java:513)
 at org.apache.tomcat.util.net.DefaultServerSocketFactory.acceptSocket(DefaultServerSocketFactory.java:60)
 at org.apache.tomcat.util.net.JIoEndpoint$Acceptor.run(JIoEndpoint.java:222)
 at java.lang.Thread.run(Thread.java:745)
"ContainerBackgroundProcessor[StandardEngine[Catalina]]" #13 daemon prio=5 os_prio=0 tid=0x00007f4910497000 nid=0x43a7 waiting on condition [0x00007f48f8da6000]
   java.lang.Thread.State: TIMED_WAITING (sleeping)
 at java.lang.Thread.sleep(Native Method)
 at org.apache.catalina.core.ContainerBase$ContainerBackgroundProcessor.run(ContainerBase.java:1510)
 at java.lang.Thread.run(Thread.java:745)
"GC Daemon" #11 daemon prio=2 os_prio=0 tid=0x00007f491040c800 nid=0x43a5 in Object.wait() [0x00007f48fa637000]
   java.lang.Thread.State: TIMED_WAITING (on object monitor)
 at java.lang.Object.wait(Native Method)
 - waiting on <0x00000000ecfdd7d0> (a sun.misc.GC$LatencyLock)
 at sun.misc.GC$Daemon.run(GC.java:117)
 - locked <0x00000000ecfdd7d0> (a sun.misc.GC$LatencyLock)
"Service Thread" #8 daemon prio=9 os_prio=0 tid=0x00007f49100e1000 nid=0x43a3 runnable [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
"C1 CompilerThread2" #7 daemon prio=9 os_prio=0 tid=0x00007f49100ce000 nid=0x43a2 waiting on condition [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
"C2 CompilerThread1" #6 daemon prio=9 os_prio=0 tid=0x00007f49100cc800 nid=0x43a1 waiting on condition [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
"C2 CompilerThread0" #5 daemon prio=9 os_prio=0 tid=0x00007f49100bf000 nid=0x43a0 waiting on condition [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
"Signal Dispatcher" #4 daemon prio=9 os_prio=0 tid=0x00007f49100bc800 nid=0x439f runnable [0x0000000000000000]
   java.lang.Thread.State: RUNNABLE
"Finalizer" #3 daemon prio=8 os_prio=0 tid=0x00007f4910093000 nid=0x439e in Object.wait() [0x00007f48fb5f4000]
   java.lang.Thread.State: WAITING (on object monitor)
 at java.lang.Object.wait(Native Method)
 - waiting on <0x00000000edd08988> (a java.lang.ref.ReferenceQueue$Lock)
 at java.lang.ref.ReferenceQueue.remove(ReferenceQueue.java:143)
 - locked <0x00000000edd08988> (a java.lang.ref.ReferenceQueue$Lock)
 at java.lang.ref.ReferenceQueue.remove(ReferenceQueue.java:164)
 at java.lang.ref.Finalizer$FinalizerThread.run(Finalizer.java:209)
"Reference Handler" #2 daemon prio=10 os_prio=0 tid=0x00007f491008e800 nid=0x439d in Object.wait() [0x00007f48fb6f5000]
   java.lang.Thread.State: WAITING (on object monitor)
 at java.lang.Object.wait(Native Method)
 - waiting on <0x00000000edd00970> (a java.lang.ref.Reference$Lock)
 at java.lang.Object.wait(Object.java:502)
 at java.lang.ref.Reference.tryHandlePending(Reference.java:191)
 - locked <0x00000000edd00970> (a java.lang.ref.Reference$Lock)
 at java.lang.ref.Reference$ReferenceHandler.run(Reference.java:153)
"main" #1 prio=5 os_prio=0 tid=0x00007f4910009000 nid=0x4397 runnable [0x00007f4919dbd000]
   java.lang.Thread.State: RUNNABLE
 at java.net.PlainSocketImpl.socketAccept(Native Method)
 at java.net.AbstractPlainSocketImpl.accept(AbstractPlainSocketImpl.java:409)
 at java.net.ServerSocket.implAccept(ServerSocket.java:545)
 at java.net.ServerSocket.accept(ServerSocket.java:513)
 at org.apache.catalina.core.StandardServer.await(StandardServer.java:470)
 at org.apache.catalina.startup.Catalina.await(Catalina.java:781)
 at org.apache.catalina.startup.Catalina.start(Catalina.java:727)
 at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
 at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
 at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
 at java.lang.reflect.Method.invoke(Method.java:498)
 at org.apache.catalina.startup.Bootstrap.start(Bootstrap.java:294)
 at org.apache.catalina.startup.Bootstrap.main(Bootstrap.java:428)
"VM Thread" os_prio=0 tid=0x00007f4910084800 nid=0x439c runnable
"GC task thread#0 (ParallelGC)" os_prio=0 tid=0x00007f491001e000 nid=0x4398 runnable
"GC task thread#1 (ParallelGC)" os_prio=0 tid=0x00007f491001f800 nid=0x4399 runnable
"GC task thread#2 (ParallelGC)" os_prio=0 tid=0x00007f4910021800 nid=0x439a runnable
"GC task thread#3 (ParallelGC)" os_prio=0 tid=0x00007f4910023800 nid=0x439b runnable
"VM Periodic Task Thread" os_prio=0 tid=0x00007f49100ef800 nid=0x43a4 waiting on condition
JNI global references: 44
$
```

# References

- [Monitoring the OpenJDK from the CLI](https://www.wolfe.id.au/2011/10/16/monitoring-the-openjdk-from-the-cli/)
- [Garbage Collection 모니터링 방법](http://d2.naver.com/helloworld/6043)

