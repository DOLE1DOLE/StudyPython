# 예외처리 2 - 여러 개의 예외 발생

x,y=map(int, input('두 수를 입력하세요 > ').split(' '))
z=0

print(f'x={x}')
print(f'y={y}')


try:
    z= x/y
    print(f'{x}/{y}={z}')
# except TypeError as e:
#     print('형변환하세요')
# except ZeroDivisionError as e:
#     print('두번째수에 0 넣지마라')
except Exception as e:            #뭐때문인진몰라도 에러 생기면 다.....바쁠때
    print(f'예외발생 {e}')

print('나누기 종료')