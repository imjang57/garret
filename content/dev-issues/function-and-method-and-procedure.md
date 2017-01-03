Title: Function, Method, Procedure
Date: 2017-01-03
Modified: 2017-01-03
Tags: function, method, procedure, sub-routine
Slug: function-and-method
Authors: imjang57
Summary: Function, Method, Procedure 의 차이점

# Function and Method

보통 function 과 method 를 구분 없이 사용한다. 하지만 이들은 엄연히 다른 개념이다. 서브루틴, 함수, 메서드, 프로시저 모두 비슷하지만 각자 의미가 있다.

- Sub-routine : A sub-routne is A repeatable piece of procedural code you can call by name.
- Function : A function is a sub-routine that returns one or more values. A function should calculate its return value based on its input.
- Procedure : A procedure is a sub-routine that doesn not return a value, but does have side-effects. (such as writing to a file, printing to the screen, or modifying the value of its input)
- Method : A method is a function or procedure that is executed in the context of an object. A Method calculates a new value or trigger side-effect based on the values of its inputs and/or the scope of the object instance

보통 개발자들은 이들 단어에 대해 별 다른 구분없이 비슷한 의미로 사용한다. 하지만 Programming Language Theory 에서는 확실히 다르다.

이런 단어들의 의미를 무시해도 상관없을까? 사실 대부분의 경우 무시해도 큰 상관은 없다고 생각된다. 하지만 어떤 로직을 모듈화하여 서브루틴으로 만들 때 이것들을 고려하면 더 좋다고 생각한다. 이 서브루틴은 어떤 타입의 서브루틴으로 구현해야 하는지 고민하면 그 서브루틴의 역할이나 목적을 더 명확해질 것이다. 서브루틴의 역할이나 목적이 명확해지면, 하나의 서브루틴이 과도하게 많은 역할을 하게 되는 현상을 방지할 수 있을 것이다. 프로그래밍에서 중요한 중복 제거, 모듈화에 대한 자연스러운 의식의 흐름이 생기게 되고 결과적으로 코드가 단순하지고 관리하기 좋아질 것이다. 어쨌든 좋은 함수를 만들기 위한 고민은 항상 필요하다고 생각한다.

물론, 실제 개발할 때 시간에 쫓겨 항상 이런 고민을 하지 못한다..ㅠㅠ.. 그래도 항상 고민하려고 노력하자. 개발은 사람이 하는 일이라 의식의 흐름에 영향을 받으니, 의식의 흐름을 항상 올바로 하려고 노력하자.

