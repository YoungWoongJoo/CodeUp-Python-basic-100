"""
정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

입력
2개의 정수(a, b)가 공백으로 구분되어 입력된다.

출력
a를 b로 나눈 몫을 출력한다.
"""

a, b = input().split()

print(int(int(a)/int(b))) # 또는 print(int(a)//int(b))