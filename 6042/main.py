"""
실수 1개를 입력받아
소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력해보자.


입력
실수 1개가 입력된다.
 

출력
소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력한다. 이 때 소숫점 둘째자리 이하 불필요한 0이 있는 경우 출력되지 않는다.
"""

f1 = input()

print(round(float(f1),2))