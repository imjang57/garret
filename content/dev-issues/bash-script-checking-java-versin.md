Title: Java version 을 체크하는 bash script
Date: 2016-12-30
Modified: 2016-12-30
Tags: bash
Slug: bash-script-checking-java-version
Authors: imjang57
Summary: Java version 을 체크하기 위한 bash script

# Check Java version from bash script

리눅스에서 자바 버전을 체크하기 위한 꼼수 스크립트를 간단하게 작성해서 저장하기 위한 글입니다.

java -version 명령의 결과:

```bash
$ java -version
java version "1.8.0_73"
Java(TM) SE Runtime Environment (build 1.8.0_73-b02)
Java HotSpot(TM) 64-Bit Server VM (build 25.73-b02, mixed mode)
```

환경변수 $JAVA_HOME을 찾아서 하는 bash script:

```bash
#!/bin/bash
if [ -n "$JAVA_HOME" ]
then
  JAVA_CMD="$JAVA_HOME/bin/java"
  JAVA_VERSION=$($JAVA_CMD -version 2>&1 | awk -F'"' '/version/ {print $2}' | awk -F'_' '{print $1}')
  echo "Run using java version $JAVA_VERSION (JAVA_HOME is $JAVA_HOME)"
  [[ $JAVA_VERSION > 1.8 ]]
  if [ $? -eq 0 ]
  then
    echo This java version is greater than 1.8.
  else
    echo This java version is not supported.
  fi
else
  echo "Java doesn't exists."
fi
```

자바 실행 파일 위치를 찾아서 하는 bash script:

```bash
#!/bin/bash
if [ $(which java) ]
then
  JAVA_PATH=$(whereis java)
  JAVA_VERSION=$(java -version 2>&1 | awk -F'"' '/version/ {print $2}' | awk -F'_' '{print $1}')
  echo "Run using java version $JAVA_VERSION ($JAVA_PATH)"
  [[ $JAVA_VERSION > 1.8 ]]
  if [ $? -eq 0 ]
  then
    echo This java version is greater than 1.8.
  else
    echo This java version is not supported.
  fi
else
  echo "Java doesn't exists."
fi
```

두 방법이 사실 거의 똑같다. 그냥 whereis 명령을 이용하느냐, JAVA_HOME 이라는 환경변수를 이용하느냐만 다르다.

다른 방법으로는 sort 명령을 이용해서 가장 앞에 위치하는 녀석을 비교하는 방법도 있다.

처음에는 bc 명령을 사용하려 했는데 버전은 보통 여러 개의 comma(.)로 되어있어서 bc 로 사용은 불가능했다. 사실 comma(.) 단위로 나눠서 각각 비교하는 로직 구현하면 되는데 귀찮음이 커서..

이 방법은 사실 완벽한 방법은 아니다. awk 로 추출한 문자열이 x.y.z 형태라는 걸 알고 있기 때문에 가능한 방법이다. 만약 1.8 로 버전이 추출되면 제대로 동작 안할 것이다. 제대로 하려면 comma(.) 단위로 나눠서 제대로 비교하는 함수를 만들어야 겠지..

