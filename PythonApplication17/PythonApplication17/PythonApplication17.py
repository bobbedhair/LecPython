#coding: cp949
#Lec17-1116: 플라스크1

from flask import Flask, url_for, redirect

#the name of the application package
app = Flask(__name__) 

@app.route('/hello')     #아래 함수 실행
def hello_world(): 
    return redirect(url_for('login'))   #경로 변경

@app.route('/login')
def login():
    return 'log in'

if __name__ == '__main__': 
    #app.run() 

    #app.debug=True  #소스 변경과 디버거 제공. 배포할 때는 False로.
    app.run(host='192.168.56.1')
