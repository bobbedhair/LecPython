#coding: cp949
#Lec16-1109: 데이터베이스2: 로그인  

import sqlite3

#비밀번호 암호화 설치: python ?m pip install werkzeug 
from werkzeug import check_password_hash, generate_password_hash    


def init_db():
    db=sqlite3.connect("test.db")
    
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit()


def get_db():
    db=sqlite3.connect("test.db")
    return db


def register():
    print("**** 회원 가입 ****")
    print("아이디: ", end='')
    userid=input()
    
    #아이디 중복 체크
    db=get_db()
    cur=db.cursor()
    cur.execute("select * from user where userid=?", [userid])
    if not cur.fetchone()==None:
        print("이미 존재하는 아이디입니다.")
        return

    print("비밀번호: ", end='')
    userpw=input()
    print("이름: ", end='')
    username=input()

    #레코드 삽입
    sql="insert into user(userid, username, userpw) values(?,?,?)"
    cur.execute(sql, [userid, username, generate_password_hash(userpw)])
    db.commit()
    print("회원가입이 완료되었습니다.\n")
    
    #레코드 조회
    print("**** 회원 리스트 ****")
    sql='''select * from user'''
    cur.execute(sql)
    print(cur.fetchall())

    print()
    db.close()


def login():
    print("**** 로그인 ****")
    print("아이디: ", end='')
    userid=input()
    print("비밀번호: ", end='')
    userpw=input()
    
    #아이디, 비밀번호 체크
    db=get_db()
    cur=db.cursor()
    cur.execute("select * from user where userid=?", [userid])
    temp=cur.fetchone()
    
    if temp==None:
        print("아이디가 존재하지 않습니다.")
    elif check_password_hash(temp[3], userpw):
        print("로그인 성공")
    else: 
        print("잘못된 비밀번호입니다.")
    
    print()
    db.close()


init_db()
register()
while 1:
    login()