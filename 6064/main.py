"""
입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 3항 연산을 사용한다.

입력
3개의 정수가 공백으로 구분되어 입력된다.
-2147483648 ~ +2147483648

출력
가장 작은 값을 출력한다.
"""

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

print((a if(a<b) else b) if(a if(a<b) else b)<c else c)