#coding: cp949 
#Lec15-1104: 데이터베이스1 

import sqlite3

#데이터베이스 연결
con=sqlite3.connect("test.db")  
cur=con.cursor()

con.isolation_level=None    #자동으로 커밋 모드 설정


####################################################phonebook 테이블

##테이블 삭제 및 생성
#dropsql='''drop table if exists phonebook;'''
#cur.execute(dropsql)

#sql='''create table if not exists phonebook(name text, phoneNum text);'''
#cur.execute(sql)


##레코드 삽입1
#insertsql='''insert into phonebook values('REDjoa','010-1111-1111');'''
#cur.execute(insertsql)


##레코드 삽입2 - 인자 전달 순서에 맞춰
#name='bluejoa'
#phoneNumber='010-2222-2222'
#insertsql='''insert into phonebook values(?,?);'''
#cur.execute(insertsql, (name, phoneNumber))


##레코드 삽입3 - 인자에 이름을 부여
#name='greenjoa'
#phoneNumber='010-3333-3333'
#insertsql='''insert into phonebook values(:inputName, :inputNum);'''
#cur.execute(insertsql, {"inputNum":phoneNumber, "inputName":name})


##con.commit()   #트랜잭션. 종료시 데이터 저장


##레코드 조회1
#cur.execute("select * from phonebook;")
#for row in cur:
#    print(row)
#    #print(row[0])
#print()


##레코드 조회2
#cur.execute("select * from phonebook order by name;")   #반대는 desc
#print(cur.fetchall())
#print()


##레코드 조회3 - name이 대문자일때 정렬 함수 추가
#def OrderFunc(str1, str2):
#    s1 = str1.upper()
#    s2 = str2.upper()
#    return (s1 > s2) -(s1 < s2)     #앞(음수), 같음(0), 뒤(양수)

#con.create_collation('myordering', OrderFunc)
#cur.execute("select * from phonebook order by name collate myordering")
#print(cur.fetchall())



####################################################user 테이블

#테이블 삭제 및 생성
dropsql='''drop table if exists user;'''
cur.execute(dropsql)

sql='''create table if not exists user(name text, age int);'''
cur.execute(sql)


#레코드 삽입4 - iterator 객체를 통해
sql='''insert into user values(?,?);'''
datalist=(('user1', 15), ('user2', 25), ('user3', 35))
cur.executemany(sql, datalist)


#레코드 조회
cur.execute("select * from user;")
print(cur.fetchall())


#내장 집계 함수 사용
cur.execute("select max(age) from user;")  #나이 최대값
print(cur.fetchone()[0])


#사용자 집계 함수 - 평균 구하기
class Average:
    def __init__(self):
        self.sum= 0
        self.cnt= 0
    def step(self, value):
        self.sum+= value
        self.cnt+=1
    def finalize(self):
        return self.sum/self.cnt

con.create_aggregate("avg", 1, Average)     #DB에등록
cur.execute("select avg(age) from user;")
print(cur.fetchone()[0])
