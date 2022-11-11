from flask import Flask, jsonify
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



if __name__=="__main__":
    app.run(host="127.0.0.1",port="5000")


# 종료는 control+ c
