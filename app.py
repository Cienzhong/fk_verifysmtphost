from flask import Flask, request, make_response
from verify_email import VerifyEmail
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

'''
Http请求方式 POST
Content-Type application/json
传参格式（Http流传输）：
[
	"zhzhi2008@126.com",
	"529781013@qq.com",
	"2121kk@toytoystimple.net"
]
'''

@app.route('/verify/email', methods=['POST'])
def verify_email():
    data = request.stream.read()
    v = VerifyEmail(json.loads(data))
    list = v.verify()
    resp = make_response(json.dumps(list))
    resp.headers['content-type'] = 'application/json'
    return resp

@app.route('/verify/wrongemail', methods=['POST'])
def wrong_demain():
    data = request.stream.read()
    v = VerifyEmail(json.loads(data))
    list = v.wrong_demain()
    resp = make_response(json.dumps(list))
    resp.headers['content-type'] = 'application/json'
    return resp

if __name__ == '__main__':
    app.run()
