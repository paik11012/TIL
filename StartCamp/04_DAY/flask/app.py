from flask import Flask, render_template, request #사용자 요청 확인 가능, flask
import requests  #파이썬 함수
app = Flask(__name__)


@app.route('/')   #/ is root, 사용자가 요청 보내기
def index():    #어떻게 응답을 해 줄지
    return "Hello Anonymous User"


@app.route('/hi/<name>')  
def hi(name):
    return render_template('hi.html', html_name=name) #꼭 ''넣기


@app.route('/ping')
def ping():
    return render_template('ping.html')


@app.route('/pong')
def pong():
    age = request.args.get('age')
    return f'pong! age: {age}'
# /pong?ages=typora


@app.route('/google')
def google():
    return render_template('google.html')


@app.route('/daum')
def daum():
    return render_template('daum.html')


# @app.route('/artii')
# def daum():
#     return render_template('artii.html')


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')  #아까 html에서 text로 보냄
    #ascii art api활용해 사용자의 input값을 변경
    response = requests.get(f'http://artii.herokuapp.com/make?text={text}')
    result = response.text
    return render_template('ascii_result.html', result=result)




if __name__=='__main__': #파이썬 실행 했을 때 name폴더 내에 main이 담긴다
    app.run(debug=True)


    
