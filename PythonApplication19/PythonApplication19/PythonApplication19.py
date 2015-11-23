#coding: cp949
#Lec19-1123: 플라스크2(DB 연동 및 로그인)

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


#변수 설정
DATABASE='flask.db'
DEBUG=True
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD='default'


#응용 프로그램 생성
app=Flask(__name__)
app.config.from_object(__name__)


#DB 관련 작업
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    db = connect_db()
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
    db.commit()
        

#DB 커넥션 요청
@app.before_request
def before_request():
    g.db=connect_db()   #g=flask의 global 인스턴스

@app.teardown_request
def teardown_request(exception):
    g.db.close()


#작성된 글 보여주기
@app.route('/')
def show_entries():     #cursor 객체 생성 후, 질의 수행
    cur=g.db.execute('select title, text from entries order by id desc')
    entries=[dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    #print(entries)
    
    return render_template('show_entries.html', entries=entries)


#로그인 하기
@app.route('/login', methods=['GET', 'POST'])
def login():
    error=None
    
    if request.method=='POST':
        if request.form['username']!=app.config['USERNAME']:
            error='Invalid usernmae'
        elif request.form['password']!=app.config['PASSWORD']:
            error='Invalid password'
        else:
            session['logged_in']=True
            flash('You were logged in')     #다음 request에 메시지 전달↔get_flashed_messages()
            return redirect(url_for('show_entries'))
    
    return render_template('login.html', error=error)


#새로운 글 추가하기
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)      #HTTP Exception 발생
    
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')

    return redirect(url_for('show_entries'))


#로그아웃 하기
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')

    return redirect(url_for('show_entries'))


#앱 실행
if __name__=='__main__':
     init_db()
     app.run()

