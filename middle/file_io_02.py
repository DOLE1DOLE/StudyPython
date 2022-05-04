# 파일 입출력 2 - 파일 읽기

f=open(file='./temp.txt',mode='r',encoding='utf-8')

#t=f.read()
while True:
    line=f.readline()  # 
    if not line: break   # break까지 한줄로많이씀.  not line:더이상 line에서 읽어올게 없으면

    print(line, end='') 



f.close()   ##잊지마 러~~~
print('파일 읽기 완료')