# 계산기 프로그램
'''
함수선언 구조
def 함수명(매개변수):
    처리로직1
    처리로직2
'''

def plus(a,b):
    res = a+b
    return res   #return은 함수 종료. 뒤에 주어지는 값 없어도 종료됨

def minus(a,b):
    res=a-b     ##return 뒤 res 적기 전에는 res가 옅은 색(변수 아직 사용하지 않았다는뜻)
    return res

def multiple(a,b):
    res=a*b
    return res

def divide(a,b):
    #if b==0:
      #  return 0   #안하면 division by zero 오류뜸+프로그램종료!!!!됨 실행오류(exception)

    res=a/b
    return res

def adds(*args):  #parameter, arguments
    res=0
    for i in args:
        res += i
    return res

print(adds(1,2,3,4,5,6,7,8,9,10))
print(adds(1,2,3))
print(adds(5,7,9,11,455))

def mul_and_div(a,b):
    return (a*b, a/b)   # 튜플

def add_and_minus_and_mul_and_div(a,b):
    return(a+b, a-b, a*b, a/b)

print(adds(1,2,3,4,5,6,7,8,9,10))
print(adds(1,2,3))
print(adds(5,7,9,11,455))

(mul_val, div_val)=mul_and_div(16,2)
print(mul_val)
print(div_val)
print(mul_and_div(16,2))

print(add_and_minus_and_mul_and_div(17,5))

# num=0     #이건뭘까
# x=0
# y=0
# val=0

# while True:
#     print('''메뉴
# 1. 덧셈
# 2. 뺄셈
# 3. 곱셈
# 4. 나눗셈
# 5. 종료
# 숫자입력 : ''', end='')
#     num=int(input())

#     if num==1:
#         print('덧셈')
#         print('첫번째 값 : ', end=' ')
#         x=int(input())
#         print('두번째 값 : ', end=' ')
#         y=int(input())
#         val=plus(x,y)
#         print(f'{x}+{y}={val}')

#     elif num==2:
#         print('뺄셈')
#         print('첫번째 값 : ', end=' ')
#         x=int(input())
#         print('두번째 값 : ', end=' ')
#         y=int(input())
#         val=minus(x,y)
#         print(f'{x}-{y}={val}')
    
#     elif num==3:
#         print('곱셈')
#         print('첫번째 값 : ', end=' ')
#         x=int(input())
#         print('두번째 값 : ', end=' ')
#         y=int(input())
#         val=multiple(x,y)
#         print(f'{x}*{y}={val}')

#     elif num==4:
#         print('나눗셈')
#         print('첫번째 값 : ', end=' ')
#         x=int(input())
#         print('두번째 값 : ', end=' ')
#         y=int(input())
#         val=divide(x,y)
#         print(f'{x}÷{y}={val}')

#     elif num==5:
#         break
#     else:
#         continue