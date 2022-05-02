# 문자열 연산
first='Hello'
second='World!'

print(first+second)  #문자연산 +(합치기)
print(first, second)  #concat과 동일(합치기 사이 자동 띄우기)

print(first*3) # 문자열연산은 +,*밖에 없음

# 문자열 길이 내장함수
print(len('한글'))
print(len(first))

# 리스트 연산
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
#print(first[-6])    #IndexError!!-큰문제(프로그램비정상종료..)

## 현재 일시
current_date='2022-05-02 14:23:45'
year=current_date[0:4]   ##0자리(2)부터 3자리(2)  +1 !!!!(4)  :앞의 0은 생략 가능
month=current_date[5:7]
day=current_date[8:10]
hour=current_date[11:13]
min=current_date[14:16]
sec=current_date[17:19]

print(year,'년', month,'월',day,'일')
print(hour,'시',min,'분',sec,'초')

print(current_date[-5:-3])

l=[1,2,3,4,5]
l[0]=10
print(1)

p= 'python'
print(p)
#p[0] = 'P'  #Python(원하는 결과) TypeError
print('P'+p[1:])
p2='P'+p[1:]
print(p2)

print(p.upper())
print(p2.lower())

