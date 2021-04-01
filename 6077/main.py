"""
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

입력
정수 1개가 입력된다.
(0 ~ 100)

출력
1부터 그 수까지 짝수만 합해 출력한다.
"""

num=int(input())
result=0
for i in range(num+1) :
	if i%2==0:
		result=result+i
print(result)