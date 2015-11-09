#coding: cp949
#Lec16-1109: �����ͺ��̽�2: �α���  

import sqlite3

#��й�ȣ ��ȣȭ ��ġ: python ?m pip install werkzeug 
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
    print("**** ȸ�� ���� ****")
    print("���̵�: ", end='')
    userid=input()
    
    #���̵� �ߺ� üũ
    db=get_db()
    cur=db.cursor()
    cur.execute("select * from user where userid=?", [userid])
    if not cur.fetchone()==None:
        print("�̹� �����ϴ� ���̵��Դϴ�.")
        return

    print("��й�ȣ: ", end='')
    userpw=input()
    print("�̸�: ", end='')
    username=input()

    #���ڵ� ����
    sql="insert into user(userid, username, userpw) values(?,?,?)"
    cur.execute(sql, [userid, username, generate_password_hash(userpw)])
    db.commit()
    print("ȸ�������� �Ϸ�Ǿ����ϴ�.\n")
    
    #���ڵ� ��ȸ
    print("**** ȸ�� ����Ʈ ****")
    sql='''select * from user'''
    cur.execute(sql)
    print(cur.fetchall())

    print()
    db.close()


def login():
    print("**** �α��� ****")
    print("���̵�: ", end='')
    userid=input()
    print("��й�ȣ: ", end='')
    userpw=input()
    
    #���̵�, ��й�ȣ üũ
    db=get_db()
    cur=db.cursor()
    cur.execute("select * from user where userid=?", [userid])
    temp=cur.fetchone()
    
    if temp==None:
        print("���̵� �������� �ʽ��ϴ�.")
    elif check_password_hash(temp[3], userpw):
        print("�α��� ����")
    else: 
        print("�߸��� ��й�ȣ�Դϴ�.")
    
    print()
    db.close()


init_db()
register()
while 1:
    login()