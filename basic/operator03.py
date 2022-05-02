# 문자열 포맷팅
from dataclasses import replace


name='성명건'
login_str='{0}님 로그인중'.format(name)

print(login_str)
# 문자열 포맷팅 방법
print('{0},{1},{2}'.format('하나',2,login_str))
print(f"{'하나'},{2},{True}")


# 소수점 표현
PI=3.14159268
print('{0:0.2f}'.format(PI))
print(f'{PI:0.3f}')

full_name='Hugo MG Sung'
sp_names=full_name.split()  #문자열을 ' ' 잘라서 리스트로
print(sp_names)
print(sp_names[0])

greeting='Hello, World'
words=greeting.split(',')  # 문자열을 ,로 잘라서 리스트로
print(words)

hi ='       hello~    '
print(hi.lstrip())  #in oracle  LTRIM()
print(hi.rstrip())   # RTRIM
print(hi.strip())    #TRIM
print(words[1].strip())

# 문자열 특정 단어, 문자열 값 변경
print(full_name.replace('Hugo MG', 'Ashley'))

# 리스트 연산
arr=['1',2,3,'4',5]

print(arr[4] + arr[2])  #그냥 더하기 5+3= 8
print(arr[3] + arr[0])  #'4'글자와 '1'글자를 합쳐라 = concat과 같음
print(arr[3] * arr[2])  #'4'글자를 3번 반복 출력

#이중 리스트
arr2=[1,2,3.14,['Hi','My','Friends']]
print(arr2[2])
print(arr2[3][1])   # 3:리스트전체 에서 1 두번째꺼 My  --2차원
print(arr2[3][1][0])   # 3:리스트전체 에서 1 두번째꺼 My에서 첫번째꺼 M   --3차원

arr3=arr+arr2
print(arr3)
