# 주소록 프로그램 v1.5
# 작성일 : 2022-05-09
# 작성자 : 돌돌
# 설  명 : 파일DB에서 Oracle로 변경

import os
import cx_Oracle as ora


# 연락처 클래스
class Contact:
    name =''; phone_num=''; e_mail=''; addr=''

    def __init__(self, name, phone_num, e_mail, addr) -> None:
        self.name= name      ##그냥 같은 이름을 쓴다 새로안지음
        self.phone_num= phone_num
        self.e_mail=e_mail
        self.addr=addr

    def __str__(self) -> str:
        str_val = (f'이  름 : {self.name}\n'
                   f'핸드폰 : {self.phone_num}\n'
                   f'이메일 : {self.e_mail}\n'
                   f'주  소 : {self.addr}\n'
                   f'=======================================================')
        return str_val           

def initDB():
    dsn=ora.makedsn('localhost',1521,service_name='orcl')
    conn=ora.connect(user='scott',password='tiger',dsn=dsn,encoding='utf-8')
    return conn

def run():
    lst_contact=[]   # 빈 리스트 생성
    conn=initDB()

    #contact = Contact('홍길동', '010-0000-1111', 'gjfh@djd.fjf','서울')
    #print(contact)
    #set_contact()
   ###1 load_contact(lst_contact)  # 파일DB 읽어오기
    clearConsole()

    while True:
        sel_menu=get_menu()
        if sel_menu==1:
            clearConsole()
            isval=set_contact(conn)
            if isval:
                input('연락처 추가성공\n계속하려면 엔터를 누르세요')
            else:
                input('오류발생 개발자에게 문의바람')
        
            # if contact is None:  
            #     input('계속하려면 엔터를 누르세요')
            #     clearConsole()
            #     continue  #contact가 비어 있으면 리스트추가 불가
           #1 lst_contact.append(contact)
               # 아무값도 엔터 대기

            clearConsole()

        elif sel_menu==2:  # 연락처 출력
            clearConsole()
            get_contact(conn)
            input('계속하려면 엔터를 누르세요')   # 엔터를 기다령
            clearConsole()

        elif sel_menu==3:
            clearConsole()
            name=input('삭제할 이름 입력 > ')
            del_contact(conn, name)
            input('연락처 삭제성공\n계속하려면 엔터를 누르세요')
            clearConsole()


        elif sel_menu==4:   # 종료
            ### save_contact(lst_contact)  #파일 DB 저장
            conn.close()
            break
        else:
            clearConsole()

# 주소록 입력받는 함수
def set_contact(conn):
    contact=None
    isSucceed=False   #입력 성공여부
    try:  # 아무입력없이 엔터 혹은 갯수 틀리면 생기는 예외처리
        name, phone_num, e_mail, addr = \
        input('정보입력(이름, 핸드폰, 이메일, 주소(구분자 /))').split('/')
        contact=Contact(name, phone_num, e_mail, addr)

            #DB처리(0509)
        cur=conn.cursor()     #밑의 쿼리문 두줄일때, 위에꺼 끝에서 띄어쓰기 해야함(한 문장으로 인식해서 오류남)
        query=('insert into addressbook '  ##문장 끝에서 공백없으면 예외발생. and 문장 간 , 쓰면 튜플로 인지함
              'VALUES (SEQ_ADDRBOOK.nextval, :1, :2, :3, :4)')
        tup=(contact.name, contact.phone_num, contact.e_mail, contact.addr)
        cur.execute(query, tup)
        conn.commit()
        cur.close()
        isSucceed=True

    except Exception as e:
        print('입력갯수 확인(이름/핸드폰/이메일/주소')
        isSucceed=False
    finally:
        return isSucceed   #True면 입력성공, False면 DB입력실패


# 주소록 전체 출력
def get_contact(conn):
    cur=conn.cursor()
    query='SELECT name, phone_num, e_mail, addr FROM ADDRESSBOOK'

    for row in cur.execute(query):   # 괄호 안에 쿼리문 직접 넣어도됨(위 쿼리 없애고)
        contact=Contact(row[0],row[1],row[2],row[3])
        print(contact)
    cur.close()

# 주소록 삭제
def del_contact(conn,name):
    cur=conn.cursor()
    query= f"DELETE FROM addressbook where name = '{name}'"
    cur.execute(query)
    conn.commit()
    cur.close()

# 주소록 파일DB 저장
def save_contact(lst_contact:list):
    f = open('./advanced/db_contact.txt', mode='w',encoding='utf-8')
    for contact in lst_contact:    ##??????
        f.write(contact.name + '/')
        f.write(contact.phone_num + '/')
        f.write(contact.e_mail + '/')
        f.write(contact.addr + '\n')

    f.close()

# # 주소록 파일DB 로드
# def load_contact(lst_contact:list):
#     f = open('./advanced/db_contact.txt', mode='r',encoding='utf-8')
#     while True:
#         line=f.readline()
#         if not line: break

#         lines = line.rstrip('\n').split('/')   # \n 제거하고, /로 나누고 리스트로
#         if len(lines) != 4: continue    #220506 11:11 엔터공백으로 생기는 예외처리
#         contact = Contact(lines[0], lines[1], lines[2], lines[3])
#         lst_contact.append(contact)

#     f.close()


# 메뉴 출력 및 선택
def get_menu() :
    str_menu=('--주소록 프로그램 v1.1--\n'
               '1. 연락처 추가\n'
               '2. 연락처 출력\n'
               '3. 연락처 삭제\n'
               '4. 종료\n')
    print(str_menu)
#0~9 숫자 외에는 ValueError 발생
    menu=0   #초기화
    try:
        menu=int(input('메뉴입력 : '))
    except Exception as e:
        print(e)
    finally:
        return menu
 
def clearConsole():
     command='clear'   # mac,unix,linux에서 화면클리어 명령어
     if os.name in ('nt','dos'):
         command='cls'    # windows,dos에선 clsㄴ
     os.system(command)

if __name__=='__main__':
    try:
        run()
    except KeyboardInterrupt as e:
        print('Ctrl+c 종료')
    