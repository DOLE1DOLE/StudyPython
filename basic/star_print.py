# *찍기
for x in range(1,8):
    for y in range(x,6):
        print('*',end='')
    print('')


for x in range(1,6):
    for y in range(x,5):
        print(' ')
    for y in range(1,x):
        print('*', end='')


print('Hello',end='')   ##end는 줄 안바꾸고싶을떄. ' ' 공백넣으면 띄어쓰기
print('World')



for x in range(3,7):
    for y in range(x,6):
        print('*',end='')
    print('')

print('쿠쿠쿠쿠')

for x in range(1,6):
    for y in range(6,x):
        print('*',end='')
    print('')