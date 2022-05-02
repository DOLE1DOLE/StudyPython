# for문 학습
# arr=[1,2,3,4,5,6,7,8,9,10]

# 한줄 주석 '''
# 여러줄 주석 """
result=0

for x in range(1,101):     ###100까지 합은 100+1
    result=result + x

print('배열의 합 =', result)

arr2= ('me', 'my', 'friend', 'jane')   ##()대신 [] 써도 상관없음

for item in arr2:
    print(f'{item:>10}')    ##:>10은 포맷팅(전부 10자리 들여쓰기)   *2 ->meme mymy

## 1~10까지 수에서 홀수/짝수 구분하기
'''
for num in range(1,11,2):  ###10+1
    if (num%2)==0:
        print(f'{num}는 짝수입니다.')
    else:
        print(f'{num}는 홀수입니다.')
        '''
# 내용 전체 주석처리:편집 줄주석/ 블록주석(다중문자열처리)

#for문 내에서 사용하는 continue, break
values=[1,3,5,7,9,11,13,15,17,19]

num=0
for item in values:
    num += 1    #num=num+1와 같음.   += 붙여서 쓸것
    if (num%2)==0:
        #break #반복문 탈출
        continue  # if 조건만 패스 다음값 진행
    else:
        print(f'{num}번 수는 {item}입니다.')
