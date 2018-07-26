# -*- conding:utf-8 -*-

import json
import os
import shutil
import time
import uuid
import re
import yunconglib

from flask import Flask, render_template, request, url_for, flash, redirect, send_file, abort, jsonify






# *******************  Flask Configuration ******************#

app = Flask(__name__)
app.config['SECRET_KEY'] = str(uuid.uuid4())
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1 * 24 * 60 * 60







# *******************  View ******************#

@app.route('/', methods=['GET', 'POST'])
def index():


    # *******************  GET ******************#

    if request.method == 'GET':
        pass

    # *******************  POST ******************#

    if request.method == 'POST':
        pass

    return render_template('index.html', data=getdata())



# *******************  API ******************#

@app.route('/get_info', methods=['GET'])
def get_info():
    _id = request.args.get('id', "")
    print(_id)
    if _id == "":
        return jsonify({})
    _id = int(_id)

    data = getdata()
    for p in data['people']:
        if p['id'] == _id:
            return jsonify(p)
    return jsonify({})


@app.route('/set_info', methods=['POST'])
def set_info():
    p = json.loads(request.data, encoding='utf-8')

    if id is None:
        return jsonify({'result': False})

    data = getdata()
    for i in range(len(data['people'])):
        if data['people'][i]['id'] == p['id']:
            data['people'][i] = p
    setdata(data)

    return jsonify({'result': True})


@app.route('/track', methods=['GET'])
def track():
    _id = request.args.get('id', "")
    if _id == "":
        return jsonify([])
    _id = int(_id)
    data = getdata()
    for p in data['people']:
        if p['id'] == _id:
            return render_template('track.html', data=data, p=p)
    return jsonify([])


@app.route('/get_cost', methods=['GET'])
def get_cost():
    _id = request.args.get('id', "")
    if _id == "":
        return ''
    _id = int(_id)
    data = getdata()
    money = 0
    name = ''
    for p in data['people']:
        if p['id'] == _id:
            name = p['name']
            money = p['money']
    cost_list = []
    for i in data['eating']:
        if i['id'] == _id:
            cost_list.append(i['cost'])
        if len(cost_list) == 5:
            break
    s = '您好{}同学，你目前余额为{}元\n最近的五笔消费为：\n'.format(name, money)
    for i in range(len(cost_list)):
        s += '[{}]: {}元\n'.format(i+1, cost_list[i])
    return s


def format_time(date):
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date))
app.add_template_global(format_time)


def getdata():
    fd = open('data.json', encoding='utf-8')
    s = fd.read()
    fd.close()
    data = json.loads(s)
    return data


def setdata(data):
    fd = open('data.json', 'w', encoding='utf-8')
    s = json.dumps(data)
    fd.write(s)
    fd.flush()
    fd.close()

# ******************  Debug Run *******************#
# !!!!!!  Do NOT run in production environment !!!!#

if __name__ == '__main__':
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
    app.run(debug=True, port=5000)
