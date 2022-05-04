# csv파일 읽기
import csv

file_name='busanbus_211231.csv'

f=open('./'+file_name, mode='r', encoding='cp949')
reader=csv.reader(f, delimiter=',')   #구분자가 , 일 경우  delimiter

next(reader)   #첫줄 제목줄 있을때!!-제목줄 안긁어옴

for line in reader:
    print(line)

f.close()     #잊지말자close