#coding=utf-8

from flask import Flask, make_response,jsonify,request
from ai import sample_sync_call

app = Flask(__name__)
app.json.ensure_ascii = False

@app.route('/meal/<string:name>', methods=['GET'])  # 获取一个用户的信息
def get_fun(name):
    data={"name":name,"menu":"土豆炖牛肉"}
    response = make_response(jsonify(data))
    response.headers["Content-Type"] = "application/json;charset=UTF-8"
    return response

@app.route('/meal/getMenu', methods=['POST'])  # 创建一个新的用户
def get_menu():
    print(request.json)
    ask = request.json.get('ask')
    res = sample_sync_call(ask)
    data={"ask":ask,"menu":res}
    response = make_response(jsonify(data))
    response.headers["Content-Type"] = "application/json;charset=UTF-8"
    return response

if __name__ == '__main__': 
    app.run(host='0.0.0.0',debug=True)