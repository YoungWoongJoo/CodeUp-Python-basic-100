"""
알파벳 문자와 숫자로 이루어진 단어 2개를 입력받아
순서대로 붙여 출력하는 프로그램을 작성해보자.

입력
알파벳과 숫자로 이루어진 2개의 단어가 공백으로 구분되어 입력된다.

출력
입력된 2개의 단어를 순서대로 붙여 출력한다.
"""

str1, str2 = input().split()

print(str1+str2)