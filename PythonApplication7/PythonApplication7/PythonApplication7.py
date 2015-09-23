#Lec7_0923
#클래스 상속, 다중상속, 추상화, 연산자 오버로딩

#from abc import ABCMeta, abstractmethod

#class Terran(metaclass=ABCMeta):
#    def __init__(self, name):
#        self.name=name

#    @abstractmethod
#    def attack(self):
#        pass
    
#class Tank(Terran):
#    def __init__(self, name, damage):
#        super().__init__(name)
#        self.damage=damage

#    def attack(self):
#        print("탱크를 쏩니다.")

#class Marine(Terran):
#    def __init__(self, name, hp):
#        super().__init__(name)
#        self.hp=hp

#    def attack(self):
#        print("총을 쏩니다.")


#def Attack(terran):   #전역함수
#    terran.attack()

#t1=Tank("tank", 0)
#t2=Marine("marine", 100)

#tlist=[Tank("tank1", 0), Tank("tank2", 0), Marine("marine1", 100), Marine("marine2", 100)]
#for item in tlist:
#    Attack(item)


class MyList(list):
    name=""
    def __init__(self, name):
        super().__init__([])    #빈 리스트로 초기화
        self.name=name

    def __str__(self):          #재정의
        return self.name+": "+super().__str__()

list1=MyList("greenjoa")
list1.append(10)
list1.append(30)
list1.append(60)
list1.append(70)
list1.append(100)
print(list1)        #리스트 출력
#print(dir(list1))   #리스트에 있는 기능들