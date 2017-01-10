Title: Windows 에서 spark-shell 을 실행하는 방법
Date: 2017-01-10
Modified: 2016-01-10
Tags: spark
Slug: run-spark-shell-on-windows
Authors: imjang57
Summary: Windows 에서 spark-shell 을 실행하는 방법

# Windows 에서 spark-shell 실행

윈도우에서 spark-shell 실행 시 NullPointerException 발생할 경우 문제 해결하는 방법에 대한 글이다.

# 윈도우에서 Spark 실행 시 RuntimeException(NullPointerException) 발생

Spark 은 보통 리눅스에서 사용되지만 Local mode 로 실행하면 윈도우에서도 실행할 수 있다. 그런데 리눅스에서는 단순히 spark-shell 스크립트를 실행하면 되는데 윈도우에서는 아래와 같은 에러가 발생하는 경우가 있다.

```
java.lang.RuntimeException: java.lang.NullPointerException
        at org.apache.hadoop.hive.ql.session.SessionState.start(SessionState.java:522)
at org.apache.spark.sql.hive.client.ClientWrapper.<init>(ClientWrapper.scala:194)
at org.apache.spark.sql.hive.client.IsolatedClientLoader.createClient(IsolatedClientLoader.scala:238)
at org.apache.spark.sql.hive.HiveContext.executionHive$lzycompute(HiveContext.scala:218)
at org.apache.spark.sql.hive.HiveContext.executionHive(HiveContext.scala:208)
at org.apache.spark.sql.hive.HiveContext.functionRegistry$lzycompute(HiveContext.scala:462)
at org.apache.spark.sql.hive.HiveContext.functionRegistry(HiveContext.scala:461)
at org.apache.spark.sql.UDFRegistration.<init>(UDFRegistration.scala:40)
................
................
```

그냥 NullPointerException 이고 아무런 메시지가 없다…-_-…

내 기억에 작년에 분명 spark-shell 을 윈도우에서 잘 썼었는데 갑자기 에러가 나서 당황했는데, HiveContext 가 원인이었다.

[MSDN 블로그의 한 글](https://blogs.msdn.microsoft.com/arsen/2016/02/09/resolving-spark-1-6-0-java-lang-nullpointerexception-not-found-value-sqlcontext-error-when-running-spark-shell-on-windows-10-64-bit/)에 따르면 윈도우에서 Spark 이 HiveContext 를 초기화하기 위해서는 `winutils.exe` 이라는 파일이 필요하다. 블로그에 따르면 HiveContext 를 초기화하는데 Hadoop 의 Native libraries 를 필요로 하기 때문이라는 듯 하다.

이번에 사용하려고 했던 spark 빌드는 hive 를 포함한 빌드이기 때문에 spark-shell 이 실행될 때 무조건 HiveContext 를 초기화하게 되어 있었다. 생각해보니 작년에 사용했던 건 hive 를 제외하고 소스를 빌드해서 사용했던 것 같다.ㅠㅠ

어쨌든 이 문제를 해결하기 위해서는 아래와 같은 것들이 필요하다.

1. winutils.exe 다운로드 및 %HADOOP_HOME%\bin 에 복사
2. HADOOP_HOME 환경 변수 설정

자세한 내용은 블로그에 쉽게 나와있으니 읽어보면 되고, 아래 명령들만 기억하자.

```bash
%HADOOP_HOME%\bin\winutils.exe ls \tmp\hive
%HADOOP_HOME%\bin\winutils.exe chmod 777 \tmp\hive
%HADOOP_HOME%\bin\winutils.exe ls \tmp\hive
```

hadoop 은 설치하고 파일 옮기고 귀찮으니까 그냥 [winutils github](https://github.com/steveloughran/winutils) 에서 다운로드 하자. 윈도우에서 hadoop 을 잘 쓸 수 있게 `winutils.exe` 파일까지 포함시켜서 구성되어 있다. 다운로드 해서 `%HADOOP_HOME%` 만 잘 잡아주면 된다.

# 추가로 발생한 문제

나의 경우에 위 내용을 다 했는데도 에러가 발생했다.

```
java.lang.RuntimeException: java.lang.RuntimeException: The root scratch dir: /tmp/hive on HDFS should be writable. Current permissions are: rwx------
  at org.apache.hadoop.hive.ql.session.SessionState.start(SessionState.java:522)
  at org.apache.spark.sql.hive.client.ClientWrapper.<init>(ClientWrapper.scala:204)
  at org.apache.spark.sql.hive.client.IsolatedClientLoader.createClient(IsolatedClientLoader.scala:238)
  at org.apache.spark.sql.hive.HiveContext.executionHive$lzycompute(HiveContext.scala:218)
  at org.apache.spark.sql.hive.HiveContext.executionHive(HiveContext.scala:208)
  at org.apache.spark.sql.hive.HiveContext.functionRegistry$lzycompute(HiveContext.scala:462)
  at org.apache.spark.sql.hive.HiveContext.functionRegistry(HiveContext.scala:461)
  at org.apache.spark.sql.UDFRegistration.<init>(UDFRegistration.scala:40)
  at org.apache.spark.sql.SQLContext.<init>(SQLContext.scala:330)
  at org.apache.spark.sql.hive.HiveContext.<init>(HiveContext.scala:97)
  at org.apache.spark.sql.hive.HiveContext.<init>(HiveContext.scala:101)
  at sun.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
  at sun.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
  at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
  at java.lang.reflect.Constructor.newInstance(Constructor.java:422)
  at org.apache.spark.repl.Main$.createSQLContext(Main.scala:89)
  ... 47 elided
Caused by: java.lang.RuntimeException: The root scratch dir: /tmp/hive on HDFS should be writable. Current permissions are: rwx------
  at org.apache.hadoop.hive.ql.session.SessionState.createRootHDFSDir(SessionState.java:612)
  at org.apache.hadoop.hive.ql.session.SessionState.createSessionDirs(SessionState.java:554)
  at org.apache.hadoop.hive.ql.session.SessionState.start(SessionState.java:508)
  ... 62 more
<console>:13: error: not found: value sqlContext
       import sqlContext.implicits._
              ^
<console>:13: error: not found: value sqlContext
       import sqlContext.sql
              ^
```

이번에는 그래도 쉽게 이유를 알 수 있었다. 에러 메시지를 보면 다음과 같다.

```
The root scratch dir: /tmp/hive on HDFS should be writable. Current permissions are: rwx------
```

즉, 권한 문제다. 그런데 원래 위의 내용대로 하면 위 문제가 해결되어야 한다. 뭐가 문제인가.

문제는 내가 C 드라이브가 아니라 E 드라이브에서 spark-shell 을 실행해서 였다. 위의 내용대로 해서 `C:\tmp\hive` 를 생성하고 권한 설정했는데, spark-shell 은 E 드라이브에서 실행해서 실제로는 `E:\tmp\hive` 에 접근했던 거였다. 그래서 `E:\tmp\hive` 로 다시 권한을 설정하고 실행하니 잘 되었다.

--------------------------------------------------------------------------------

`HADOOP_HOME` 을 환경변수로 해주기 귀찮아서 더 해보니까 conf/spark-env.cmd 파일에 아래처럼 추가해줘도 동작한다.

set HADOOP_HOME=C:\hadoop\hadoop-2.6.4

# 참고

- [Resolving Spark 1.6.0 "java.lang.NullPointerException, not found: value sqlContext" error when running spark-shell on Windows 10 (64-bit)](https://blogs.msdn.microsoft.com/arsen/2016/02/09/resolving-spark-1-6-0-java-lang-nullpointerexception-not-found-value-sqlcontext-error-when-running-spark-shell-on-windows-10-64-bit/)
- [hadoop 2.6.4 winutils github](https://github.com/steveloughran/winutils/tree/master/hadoop-2.6.4/bin)

