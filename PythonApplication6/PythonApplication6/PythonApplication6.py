#Lec0921

class movie:
    '''영화 클래스입니다.'''
    
    count=0
    
    title="암살"
    director="최동훈"
    
    def __init__(self, title, director):
        self.title=title
        self.director=director
        #self.count += 1
        movie.count += 1
        print(self.title+" 생성자 호출")

    def __del__(self):
        print(self.title+" 소멸자 호출")

    def showinfo(self):
        print(self.title+" "+self.director)

    @staticmethod
    def showcount1():
        print(movie.count)

    @classmethod
    def showcount2(cls):
        print(cls.count)


#m0=movie("암살", "최동훈")
#print(m0.title)
#print()

#m3=movie("베테랑3", "류승완3")
#m4=movie("베테랑4", "류승완4")
#print(type(m4))

#m4=m3   #모든 대입연산은 얕은 복사
#print(id(m4))
#print(id(m3))   #주소가 같다. 같은곳을 참조
#m4.showinfo()

m1=movie("베테랑1", "류승완1")
m2=movie("베테랑2", "류승완2")
m3=movie("베테랑3", "류승완3")
m4=movie("베테랑4", "류승완4")
#print(m1.count)
#print(m2.count)
movie.showcount1()
movie.showcount2()