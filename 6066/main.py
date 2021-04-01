"""
3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

입력
3개의 정수(a, b, c)가 공백을 두고 입력된다.
0 <= a,b,c <= 2147483647

출력
입력된 순서대로 짝(even)/홀(odd)을 줄을 바꿔 출력한다.
"""

a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if a%2==0:
	print('even')
else:
	print('odd')
if b%2==0:
	print('even')
else:
	print('odd')
if c%2==0:
	print('even')
else:
	print('odd')