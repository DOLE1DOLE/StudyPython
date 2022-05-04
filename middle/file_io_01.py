## 파일 입출력 1 - 쓰기

# mode=w 새로생성쓰기, a 추가쓰기, r 읽기
f= open(file='C:/STUDY/StudyPython/temp.txt', mode='a', encoding='utf-8')   ##앞의 file= 생략가능
f.write('안녕하세요. \n')
f.write('나는 죠르디다 \n')
f.write('죠르르맘마 \n')

f.close()   ##잊지말자 open열면 close!!!!!
print('파일 생성완료')