from flask import Flask, jsonify,redirect,url_for,request
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



if __name__=="__main__":
    app.run(host="127.0.0.1",port="5000")


# 종료는 control+ c
