#coding: cp949
#Lec17-1116: �ö�ũ1

from flask import Flask, url_for, redirect

#the name of the application package
app = Flask(__name__) 

@app.route('/hello')     #�Ʒ� �Լ� ����
def hello_world(): 
    return redirect(url_for('login'))   #��� ����

@app.route('/login')
def login():
    return 'log in'

if __name__ == '__main__': 
    #app.run() 

    #app.debug=True  #�ҽ� ����� ����� ����. ������ ���� False��.
    app.run(host='192.168.56.1')
