"""
정수값이 입력될 때,
그 불 값을 반대로 출력하는 프로그램을 작성해보자.

입력
정수 1개가 입력된다.

출력
입력된 정수의 불 값이 False 이면 True, True 이면 False 를 출력한다.

"""
num = input()
num=bool(int(num))
print(not num)