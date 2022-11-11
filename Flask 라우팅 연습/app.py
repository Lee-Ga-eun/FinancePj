from flask import Flask, jsonify,redirect,url_for,request, render_template
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "<h1>hello world</h1>"


@app.route('/profile/<username>')
def get_profile(username):
    return "profile:  "+ username

# /profile/나나나 --> view에 profile:나나나 출력됨

# 숫자를 뷰에 출력하기
@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id

#  rest api 구현하기.
# 특정 url을 요청하면, json 형식으로 데이터를 반환
# 웹주소 요청에 대한 응답을 json 형식으로 작성

@app.route('/json_test')
def hello_json():
    data={'name':'Aaron', 'family':'Byun'}
    return jsonify(data)

@app.route('/server_info')
def server_info():
    data={'server_name':'127.0.0.1', 'server_port':'5000'}
    return jsonify(data)


#  get/post 구현하기 (postman으로 확인)

@app.route('/success/<name>') #로그인 성공시 해당 페이지로 이동
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form['myName']
        return redirect(url_for('success',name=user)) # postman에서 key:myName, value:lucy하고 send하면 success 페이지로 redirect된 걸 확인할 수 있음
    else:
        user=request.args.get('myName')
        return redirect(url_for('success',name=user))

# html과 렌더링 (html파일은 templates 폴더에 있어야 한다)
@app.route('/html_test')
def hello_html():
    return render_template('practice.html')


#플라스크는 flask 프로그래밍 로직에 따라 HTML 태그를 만들거나 HTML 내용을 채우기 위해 Jinja2 템플릿 엔진을 사용할 수 있다
# jinja2 engine을 사용하여 템플릿을 만들고 템플릿 안의 값을 채워서 렌더링

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('variable.html', name=user)


# 반복문 연습
@app.route('/hello_loop')
def hello_names():
    value_list=['이름a','이름b','이름c']
    return render_template('variable.html',values=value_list)

# 조건문 연습
@app.route('/hello_if')
def hello_if():
    value=40
    return render_template('condition.html',data=value)




if __name__=="__main__":
    app.run(host="127.0.0.1",port="5000")


# 종료는 control+ c
