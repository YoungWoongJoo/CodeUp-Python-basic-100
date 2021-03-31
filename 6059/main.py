"""
입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

** 비트단위(bitwise) 연산자는,
~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
<<(bitwise left shift), >>(bitwise right shift)
가 있다.

입력
정수 1개가 입력된다.
-2147483648 ~ +2147483647

출력
비트 단위로 1 -> 0, 0 -> 1로 바꾼 후 그 값을 10진수로 출력한다.
"""

num = int(input())
print(~num)