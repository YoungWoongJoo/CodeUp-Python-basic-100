"""
단어와 반복 횟수를 입력받아 여러 번 출력해보자.

입력
단어와 반복 횟수가 공백으로 구분되어 입력된다.

출력
입력된 단어를 입력된 횟수만큼 반복해 출력한다.
"""

value, cnt = input().split()

print(value*int(cnt)) #문자열 * 숫자 는 숫자만큼 문자열 반복 출력