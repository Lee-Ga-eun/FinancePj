from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "<h1>hello world</h1>"

if __name__=="__main__":
    app.run(host="127.0.0.1",port="5000")


# 종료는 control+ c
