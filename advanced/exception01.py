# 예외처리 1 - 예외발생
def multi(a,b):
    res=a*b
    return res

def divide(a,b):
    res=0

    try:
        res=a/b
    except Exception as e:
        print(f'예외발생 {e}')
    finally:
        return res


if __name__=='__main__':
    value=7
print('곱셈/나눗셈')
print(divide(6,0))
print('b에다가 0 넣지 마세요 친절함')

print(multi(6,6))
print('종료')