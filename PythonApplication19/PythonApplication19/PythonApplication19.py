#coding: cp949
#Lec19-1123: �ö�ũ2(DB ���� �� �α���)

import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


#���� ����
DATABASE='flask.db'
DEBUG=True
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD='default'


#���� ���α׷� ����
app=Flask(__name__)
app.config.from_object(__name__)


#DB ���� �۾�
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    db = connect_db()
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
    db.commit()
        

#DB Ŀ�ؼ� ��û
@app.before_request
def before_request():
    g.db=connect_db()   #g=flask�� global �ν��Ͻ�

@app.teardown_request
def teardown_request(exception):
    g.db.close()


#�ۼ��� �� �����ֱ�
@app.route('/')
def show_entries():     #cursor ��ü ���� ��, ���� ����
    cur=g.db.execute('select title, text from entries order by id desc')
    entries=[dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    #print(entries)
    
    return render_template('show_entries.html', entries=entries)


#�α��� �ϱ�
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
            flash('You were logged in')     #���� request�� �޽��� ���ޡ�get_flashed_messages()
            return redirect(url_for('show_entries'))
    
    return render_template('login.html', error=error)


#���ο� �� �߰��ϱ�
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)      #HTTP Exception �߻�
    
    g.db.execute('insert into entries (title, text) values (?, ?)', [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')

    return redirect(url_for('show_entries'))


#�α׾ƿ� �ϱ�
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')

    return redirect(url_for('show_entries'))


#�� ����
if __name__=='__main__':
     init_db()
     app.run()

