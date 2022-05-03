# 사람객체를 위한 클래스 Person

class Person:
    __name=''   #이름속성
    age=''    #나이속성
    height=100  #키
    weight=30   #몸무게

    # 생성자 재정의
    def __init__(self, name = None) -> None:   #안됨
        if name == None:
            self.__name = '홍길동'
        else:
            self.__name = name
    
        print(f'{self.__name}탄생!!')

# 매직메서드 __str__ 사용 재정의
    def __str__(self) -> str:        
        value=f'''객체 : {self.__name}
나이 : {self.age}
  키 : {self.height}'''
        return value

    def walk(self, speed):    #잊지말자 self
        print(f'{self.__name}이(가) {speed}km/h로 걷는다.')
        return

    def run(self, speed):
        print(f'{self.__name}이(가) {speed}km/h로 뛴다.')
        return

p=Person()   #객체 생성
 #p.__name='성명건'
p.age=46
p.height=178
p.weight=70

p.walk(2)
p.run(10)

print(p)
#print(p.__name)
print(p.age)

