"""
정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

while 조건식 :
  ...
  ...

반복 실행구조를 사용해 보자.

입력
정수 1개가 입력된다.
(1 ~ 100)

출력
1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력한다.

"""

num = input()
num=int(num)

while num>0:
	num=num-1
	print(num)