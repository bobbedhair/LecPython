#coding: cp949 
#Lec15-1104: �����ͺ��̽�1 

import sqlite3

#�����ͺ��̽� ����
con=sqlite3.connect("test.db")  
cur=con.cursor()

con.isolation_level=None    #�ڵ����� Ŀ�� ��� ����


####################################################phonebook ���̺�

##���̺� ���� �� ����
#dropsql='''drop table if exists phonebook;'''
#cur.execute(dropsql)

#sql='''create table if not exists phonebook(name text, phoneNum text);'''
#cur.execute(sql)


##���ڵ� ����1
#insertsql='''insert into phonebook values('REDjoa','010-1111-1111');'''
#cur.execute(insertsql)


##���ڵ� ����2 - ���� ���� ������ ����
#name='bluejoa'
#phoneNumber='010-2222-2222'
#insertsql='''insert into phonebook values(?,?);'''
#cur.execute(insertsql, (name, phoneNumber))


##���ڵ� ����3 - ���ڿ� �̸��� �ο�
#name='greenjoa'
#phoneNumber='010-3333-3333'
#insertsql='''insert into phonebook values(:inputName, :inputNum);'''
#cur.execute(insertsql, {"inputNum":phoneNumber, "inputName":name})


##con.commit()   #Ʈ�����. ����� ������ ����


##���ڵ� ��ȸ1
#cur.execute("select * from phonebook;")
#for row in cur:
#    print(row)
#    #print(row[0])
#print()


##���ڵ� ��ȸ2
#cur.execute("select * from phonebook order by name;")   #�ݴ�� desc
#print(cur.fetchall())
#print()


##���ڵ� ��ȸ3 - name�� �빮���϶� ���� �Լ� �߰�
#def OrderFunc(str1, str2):
#    s1 = str1.upper()
#    s2 = str2.upper()
#    return (s1 > s2) -(s1 < s2)     #��(����), ����(0), ��(���)

#con.create_collation('myordering', OrderFunc)
#cur.execute("select * from phonebook order by name collate myordering")
#print(cur.fetchall())



####################################################user ���̺�

#���̺� ���� �� ����
dropsql='''drop table if exists user;'''
cur.execute(dropsql)

sql='''create table if not exists user(name text, age int);'''
cur.execute(sql)


#���ڵ� ����4 - iterator ��ü�� ����
sql='''insert into user values(?,?);'''
datalist=(('user1', 15), ('user2', 25), ('user3', 35))
cur.executemany(sql, datalist)


#���ڵ� ��ȸ
cur.execute("select * from user;")
print(cur.fetchall())


#���� ���� �Լ� ���
cur.execute("select max(age) from user;")  #���� �ִ밪
print(cur.fetchone()[0])


#����� ���� �Լ� - ��� ���ϱ�
class Average:
    def __init__(self):
        self.sum= 0
        self.cnt= 0
    def step(self, value):
        self.sum+= value
        self.cnt+=1
    def finalize(self):
        return self.sum/self.cnt

con.create_aggregate("avg", 1, Average)     #DB�����
cur.execute("select avg(age) from user;")
print(cur.fetchone()[0])
