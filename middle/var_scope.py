a=1     #밖의 a는 global 광역변수
print(a)

def vartest():   #안의 a 는 local 지역변수
    global a    #<-밖의 광역변수a를 가져다 쓴다 : 밖의 a랑 충돌하면안됨
    print(a)
    a=a+10
    return a

a=vartest()
print(a)


if a==13:
    pass    #pass는 파이썬에만 있음. 실행은 시킴.
