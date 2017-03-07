Title: Windows 에서 apache zeppelin 사용 시 HiveContext 에러
Date: 2017-01-10
Modified: 2016-01-10
Tags: spark, zeppelin
Slug: hive-context-error-of-zeppelin-on-windows
Authors: imjang57
Summary: Windows 에서 apache zeppelin 사용 시 HiveContext 에러가 발생하는 경우

# Windows 에서 zeppelin 실행

[윈도우에서 spark-shell을 실행하는 방법]({filename}/issues/run-spark-shell-on-windows.md) 에서 윈도우에서 spark-shell 을 실행하는 방법에 대해 알아봤다. spark-shell 이 실행가능하니까 당연히 zeppelin 도 실행가능할거라고 생각된다. 그래서 실행해보니 에러가 발생했다..-_-..; 메시지가 매우 긴데.. 다음과 같은 메시지가 나오는 경우였다.

```
Caused by: java.lang.IllegalArgumentException: java.net.URISyntaxException: Relative path in absolute URI: file:C:/Users/imjan/Desktop/zeppelin-0.6.2/spark-warehouse
```

`%ZEPPELIN_HOME%\spark-warehouse` 를 hive 테이블들을 저장하기 위해 사용하는 것 같다. 그래서 `%ZEPPELIN_HOME%\spark-warehouse` 폴더를 생성하고 [윈도우에서 spark-shell을 실행하는 방법]({filename}/issues/run-spark-shell-on-windows.md) 포스트에서 했떤 것 처럼 winutils 를 사용해서 권한을 설정해줬다

그런데 같은 에러가 또 발생한다..!!!!..ㅆ....

그래서 찾다보니 [이 블로그 포스트](https://hernandezpaul.wordpress.com/2016/11/14/apache-zeppelin-installation-on-windows-10/) 에서 해결책을 찾았다.

결론은 `spark.sql.warehouse.dir` 이라는 설정값을 정확하게 설정해줘야 한다는 것이다. `%ZEPPELIN_HOME%\conf\interpreter.json` 을 열어서 spark interprefter 설정을 찾아서 아래와 같이 `spark.sql.warehouse.dir` 을 추가하자.

```json
{
  ...
  "2C5DV85NF": {
      "id": "2C5DV85NF",
      "name": "spark",
      "group": "spark",
      "properties": {
        "spark.sql.warehouse.dir": "file:///C:/Users/imjan/Desktop/zeppelin-0.6.2/spark-warehouse",
        "spark.executor.memory": "",
        "args": "",
        "zeppelin.spark.printREPLOutput": "true",
        "spark.cores.max": "",
        "zeppelin.dep.additionalRemoteRepository": "spark-packages,http://dl.bintray.com/spark-packages/maven,false;",
        "zeppelin.spark.sql.stacktrace": "false",
        "zeppelin.spark.importImplicit": "true",
        "zeppelin.spark.concurrentSQL": "false",
        "zeppelin.spark.useHiveContext": "true",
        "zeppelin.pyspark.python": "python",
        "zeppelin.dep.localrepo": "local-repo",
        "zeppelin.R.knitr": "true",
        "zeppelin.spark.maxResult": "1000",
        "master": "local[*]",
        "spark.app.name": "Zeppelin",
        "zeppelin.R.image.width": "100%",
        "zeppelin.R.render.options": "out.format \u003d \u0027html\u0027, comment \u003d NA, echo \u003d FALSE, results \u003d \u0027asis\u0027, message \u003d F, warning \u003d F",
        "zeppelin.R.cmd": "R"
      },
      ...
    }
  ...
}
```

그리고 아래 코드를 실행해서 테스트해보니 잘된다. `%ZEPPELIN_HOME`\spark-warehouse` 에 `tmptable` 이라는 폴더가 생성된 걸 확인할 수 있다.

```scala
val hiveCtx = new org.apache.spark.sql.hive.HiveContext(sc)
hiveCtx.sql("select 1, 2").write.saveAsTable("tmpTable")
```

--------------------------------------------------------------------------------

위의 내용은 zeppelin 내장 spark interpreter 를 사용한 경우라서 사용 형태라 다른 경우 맞지 않을 수도 있다.

# 참고

- [Apache Zeppelin installation on Windows 10](https://hernandezpaul.wordpress.com/2016/11/14/apache-zeppelin-installation-on-windows-10/)
