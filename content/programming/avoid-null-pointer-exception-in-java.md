Title: NPE (NullPointerException) 을 피하자
Date: 2017-01-18
Modified: 2017-01-18
Tags: java, NPE, NullPointerException, null
Slug: avoid-null-pointer-exception-in-java
Authors: imjang57
Summary: Java 에서 NPE (NullPointerException) 을 피하면서 코딩하기 위한 습관들

# NPE(NullPointerException) 을 피하자.

자바 개발을 하다보면 가장 많이 만나고 영향이 큰 예외 중 하나가 _NPE_ 이다. NPE 는 개발자의 습관이나 부주의 등이 대부분 원인이다. 이를 예방하는 가장 좋은 방법은 NPE 를 피하는 코딩 습관을 갖는 것이다.

## null 의 의미

자바에서 `null` 이란 아래와 같은 상태를 의미한다.

> 아직 object 가 생성되지 않은 상태, 즉 아직 memory 할당이 되지 않은 object 상태

NPE 는 null 상태인 object 를 참조하여 어떠한 행위(method 실행)를 하려할 때 발생하는 예외이다.

## NPE가 발생하는 상황

NPE 는 아래와 같은 상황에서 발생할 수 있다.

- null object 의 method 를 호출
- null object 의 instance member 에 접근

# Avoid NPE in source code

NPE 는 대부분 개발자의 부주의로 발생하므로, 개발할 때 조금만 신경쓰면 대부분의 NPE 를 예방할 수 있다.

## String 객체를 비교할 경우

`equals()`, `equalsIgnoreCase()` 등을 사용할 때 null 이 아닌 것이 확실한 객체가 있다면 해당 객체의 method 를 호출하자.

```java
if( "Compare String".equals(testStr) ) {
 // logic
}
```

## String.valueOf() 사용

로그 등을 남길 때 객체의 상태를 확인하기 위해 객체의 `toString()` 을 호출하는 경우가 있는데, 객체가 null 일 경우 NPE 가 발생한다. 로그를 위해 null 을 체크하는 로직을 추가하는 것은 불필요한 코드가 될 수 있다.

`toString()` method 보다는 `String.valueOf()` 를 사용하자.

## Primitive type 사용

꼭 필요한 경우가 아니라면 Primitive type data 를 사용하자. NPE 를 줄이고 memory 도 더 효율적으로 사용할 수 있다.

## return empty collection

List, Set, Map 등과 같은 Collection 을 return 하는 method 를 구현할 때, null 을 return 하지 말자. 대신 empty collection 을 return 하자. 그러면 함수를 사용하는 개발자는 불필요한 null 체크를 하지 않아도 된다.

## Use null-safe stuffs

null 에 안전한 자바 내장 함수나 commons-lang 과 같은 helper class 를 사용하자. Apache Commons 도 좋고, 요즘은 Googld guava 가 매우 유용한 라이브러리들을 많이 제공한다.

## Unit Test

Java assert, Unit test (JUnit) 등을 활용하여 사전 확인 및 다양한 상황에서의 테스트를 수행하자.

## 협업할 때는 기능 및 제약사항 등을 확실히 명시하자.

NPE 는 개발자의 부주의에 의해 대부분 발생하고, 개발자의 부주의는 정보가 없어서 발생하는 경우가 많다. 아래의 내용들은 명확하게 공유하자.

- Method parameter 와 return value 에 대한 명세
- Method 에서 수행하는 validation 으로 인해 발생가능한 Exception 들

[Google guava](https://github.com/google/guava) 의 _Preconditions_ 등을 사용하면 parameter 에 대한 validation 을 쉽게 처리할 수 있다.

또한 _Java Doc_ 등의 문서를 적절히 사용하자. 자동으로 Java doc 을 생성해주는 프로그램도 많다. 또는 [swagger](http://swagger.io) 등을 이용하여 RestAPI 서비스의 API 에 대한 명세를 공유할 수도 있다.

문서의 내용을 자세하게 채우지 않아도 된다. 위의 내용들에 대해서만이라도 명확하게 작성하자.

## Optional class

_Optional_ 을 사용하면 null check 를 위한 코드를 상당히 줄일 수 있으며 코드의 Readability 를 높일 수 있다.

Optional 은 원래 google guava 라이브러리에서 제공되었었는데 java 8 로 버전 업하면서 자바에서도 지원(`java.util.Optional<T>`)하게 되었다.

Optional object 생성:

```java
String nStr = null;
String str = "Test String";
Optional<String> eOp = Optional.empty(); // empty Optional 객체 생성
Optional<String> nullableOp = Optional.ofNullable(nStr); // null 을 허용하는 Optional 객체 생성
Optional<String> notNullableOp = Optional.of(str); // str 에 접근하는 시점이 아니라 Optional 객체를 생성하는 이 순간 parameter 의 null 여부를 체크하여 NPE 가 발생
if( notNullableOp.isPresent() ) {
 // Optional 객체에 값이 있는지 확인 후 아래 코드를 실행
 System.out.println(notNullableOp.get());
}
notNullableOp.ifPresent(System.out::println); // Optional 객체에 값이 있는지 확인 후 전달받은 function 을 실행
notNullableOp.ifPresent(s -> { System.out.println(s) });
nullableOp.ifPresent(System.out::println); // null 이므로 실행되지 않는다.
String emtpyStr = eOp.orElse("Empty String"); // Optional 객체가 empty 일 경우 (null 일 경우) "Empty String" 의 reference 를 return.
String exStr = eOp.orElseThrow(Exception::new); // Optional 객체가 empty 일 경우 (null 일 경우) 지정된 Exception 을 throw.
System.out.println(notNullableOp.filter(s->s.length() < 5).orElse("Too long string"));
```

Optional 과 map 을 이용하여 null check 없이 jsonNode 접근하기:

```java
Optional.of(rootNode)
 .map(node -> node.get("secondNode"))
 .map(node -> node.get("thirdNode"))
 .ifPresent(node -> {
 System.out.println(node.get("value"));
 })
```

if else 를 이용한 null 체크는 source code readability 를 떨어뜨린다. Optional 과 Java doc 을 이용한 직관적인 코드 작성을 하자.

