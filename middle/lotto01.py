# 첫번째 간단한 로또
import random as rnd

numbers=[i for i in range(1,46)]
lotto=[]  #로또번호 저장할 곳

for i in range(6):   #6번 반복
    lotto.append(rnd.choice(numbers))

lotto.sort()
print(lotto)