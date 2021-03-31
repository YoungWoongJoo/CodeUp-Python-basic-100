"""
두 정수(a, b)를 입력받아
a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False 를 출력하는 프로그램을 작성해보자.

입력
두 정수(a, b)가 공백을 두고 입력된다.
-2147483648 <= a, b <= +2147483647

출력
a가 b보다 작은 경우 True 를, 그렇지 않은 경우 False 를 출력한다.
"""

a,b=input().split()
a=int(a)
b=int(b)

print(a<b)