Title: Integer types header file (stdint.h)
Date: 2016-01-02
Modified: 2016-01-02
Tags: c programming language, stdint.h
Slug: integer-types-header-file-stdint
Authors: imjang57
Summary: C 언어의 Integer data type 의 크기를 정의한 stdint.h 헤더파일

# uintXX_t data types in stdint.h

`_t` 는 구조체에 붙이는 것이라기 보다는 user-defined type 에 붙이는 것이다. `uint8_t`, `uint32_t` 등은 `stdint.h` 헤더파일에 정의되어 있으며 C99 표준에서 도입되었다.

`stdint.h` : This header defines a set of integral type aliases with specific width requirements, along with macros specifying their limits and macro functions to create values of these types.

C 언어 표준에는 `char`, `short`, `int`, `long`, `float`, `double` 등과 같은 Primitive data type 을 지원한다. 하지만 표준에서 이런 type 들이 몇 bytes 를 필요로 하는지 정확한 정의를 하지 않았다. 때문에 Machine (CPU) 의 종류에 따라 `int` 나 `long` 등의 크기가 달라지게 되었다. (대부분은 `char` 1 byte, `short` 2 bytes, `int` 4 bytes 로 알고 가르치지만 대부분의 machine 에서 이렇게 사용할 뿐이지 다 똑같은 건 아니다. 표준은 `short`, `int`, `long` 에 대해 `short` 은 최소 `int` 보다 같거나 작아야 한다고 정의되어 있으며, `long` 은 `int` 보다 같거나 커야 한다고 정의되어 있을 뿐이다.) 이는 C 언어로 작성된 프로그램의 호환성(Portability) 에 매우 큰 악영향을 미칠 수 있는 요소였다.

이러한 machine 에 따른 호환성 문제를 해결하기 위해 C99 표준에서는 `int8_t`, `uint8_t`, `int16_t`, `uint16_t`, `int32_t`, `uint32_t`, `int64_t`, `uint64_t` 등을 도입하였다.

C99 에서 도입된 `stdint.h` 는 이전에 존재하던 `limits.h` 와는 성격이 다르다. 기존의 `limits.h` 가 machine-dependent data type 의 크기를 서술한 것이라면, `stdint.h` 는 data type 의 size 를 명확하게 정의한다. `limits.h` 는 기계마다 다르게 정의되는 각 data type 의 크기만 알려줄 뿐이며, 원하는 크기의 자료형을 선언하는데는 크게 도움이 되지 않는다. 반면 `stdint.h` 는 기존의 `short`, `int`, `long` 과 같은 자료형을 보다 명확하게 수치로 나타낸다.

32 비트 기계에서 16 비트 크기를 가지는 정수 자료형을 명확하게 선언하고 싶다면, `int16_t` 를 사용하고, 32 비트 정수 자료형이라면 `int32_t` 를 사용하여 선언한다. 기본 자료형을 다시 재정의하는 것은 쓸데없이 혼란을 가중시킬거라 생각할지도 모르지만, 이런 식으로 보다 명확하게 자료형을 재정의하는 것은 훨씬 명확한 코드를 작성하는데 도움이 된다. 부동소수점 자료형을 제외한 정수 자료형들은 모두 이런 `intN_t` 스타일로 정의할 수 있는데, `char` 도 `int8_t` 와 같이 선언할 수 있다. C 에서 `char` 타입은 정수형으로도 간주될 수 있기 때문이다. 자료형의 크기를 명확하게 밝혀준다는 장점 외에도, `unsigned int` 와 같은 긴 문장을 간단하게 `uint32_t` 로 표현할 수 있다는 장점도 있다. 호환성을 염두에 둔 코드를 작성한다면, `stdint.h` 는 매우 편리한 존재가 아닐 수 없다. C99 에서 새롭게 도입된 `stdint.h` 는 C++ 에도 `cstdint` 헤더 파일로 포함되어 있다.

