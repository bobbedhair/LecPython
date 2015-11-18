#coding: cp949
#Lec18-1118: 플라스크1(정적 파일)

from flask import Flask, render_template

app = Flask(__name__) 

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    data1=[dict(href="http://www.naver.com", caption="네이버"), dict(href="http://www.google.com", caption="구글")]
    
    data2={
        'title': "YEEUN's homepage",
        'name_d': 'greenjoa'
    }

    #return render_template('hello.html', name=name, items=data1, **data2)
    return render_template('main.html', name=name, items=data1, **data2)


if __name__=='__main__':
    app.run()
    app.debug=True
