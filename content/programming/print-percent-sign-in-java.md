Title: 자바에서 % 출력하기
Date: 2016-12-30
Modified: 2016-12-30
Slug: print-percent-sign-in-java
Authors: imjang57
Summary: 자바에서 % 문자 출력하기

# Java String 에서 % 문자 출력하기

오늘 개발하다가 `%` 문자가 들어가는 문자열을 처리할 일이 있었다. 처음에 아무 생각없이 아래처럼 작성했다.

```java
String str1 = "test";
String str2 = String.format("string is \"%%s%\".", str1);
```

원하는 결과는 아래와 같이 나오는 것이었다.

```
string is "%test%".
```

당연히 String.format 에서 에러가 발생했다.

```
Exception in thread "main" java.util.UnknownFormatConversionException: Conversion = '"'
 at java.util.Formatter.checkText(Formatter.java:2579)
 at java.util.Formatter.parse(Formatter.java:2565)
 at java.util.Formatter.format(Formatter.java:2501)
 at java.util.Formatter.format(Formatter.java:2455)
 at java.lang.String.format(String.java:2940)
 at StringTest.main(StringTest.java:7)
 at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
 at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
 at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
 at java.lang.reflect.Method.invoke(Method.java:497)
 at com.intellij.rt.execution.application.AppMain.main(AppMain.java:144)
```

`\` 는 특정 _espace character_ 로 이미 약속된 문자들과 사용돼야 한다. 그런데 그 문자들 중에 `%` 는 없다.

`%` 는 _Formatting_ 을 위한 문자로, `String.format("%d", 123);` 과 같이 사용된다. 이 때 `%` 자체를 출력하기 위해서도 `%` 를 prefix 로 사용하여 `%%` 와 같이 처리해야 한다.

```java
String str1 = "test";
String str2 = String.format("string is %%%s%%.", str1);
```

`%` 는 그냥 문자가 아니라 포맷을 지정하기 위한 포맷 지시자 (format specifier 또는 format string) 역할을 하는 특수한 문자이기 때문이다.

알고 있던 거였는데.. 역시 오래동안 안쓰면 머리에서 삭제되어 버린다. ㅠㅠ
