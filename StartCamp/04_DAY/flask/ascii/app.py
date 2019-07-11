from flask import Flask, render_template, request #사용자 요청 확인 가능
app = Flask(__name__)


@app.route('/ascii_input')
def ascii_input():
    return render_template('ascii_input.html')


@app.route('/ascii_result')
def ascii_result():
    text = request.args.get('text')  #아까 html에서 text로 보냄
    #ascii art api활용해 사용자의 input값을 변경
    return text


if __name__=='__main__': #파이썬 실행 했을 때 name폴더 내에 main이 담긴다
    app.run(debug=True)