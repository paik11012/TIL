# 파이썬 파일은 모듈이자 스크립트 / 실행시키는 방법 두 개 python name, 모듈을 호출하기
from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)

@app.route("/") #decorator, endpoint
def hello(): #def making new function
    return render_template('index.html')    #app.py와 같은 경로, 파일 이름이 templates여야 한다 / 사용자에게 어떤 html을 보여 줄 것인가?

@app.route('/minju')
def minju():
    return 'Hello Minju'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    nday = datetime.datetime(2019,12,14)    
    td = nday - today
    return f'{td.days} 일 남았습니다'

@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag</h1>'

@app.route('/html_lines')
def html_lines():
    return '''
        <h1> 여러 줄 보내기 </h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

@app.route('/greeting/<name>') #get name from user
def greeting(name):
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return render_template('cube.html', html_num=num, result=result)
   

# practice
@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['pork', 'fish', 'sheep', 'beer', 'soju']
    order = random.sample(menu, people)
    return str(order)


@app.route('/movie')
def movie():
    movies = ['toy story', 'farms', 'cats and cow', 'tomb rader', 'spider man']
    return render_template('movie.html', movies=movies)


if __name__=='__main__': #파이썬 실행 했을 때 name폴더 내에 main이 담긴다
    app.run(debug=True)
