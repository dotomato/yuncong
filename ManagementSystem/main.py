# -*- conding:utf-8 -*-

import json
import os
import shutil
import time
import uuid
import re
import random
import yuncongserverlib

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

    return render_template('index.html', data=_getdata())


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    # *******************  GET ******************#
    if request.method == 'GET':
        return render_template('add_user.html')

    # *******************  POST ******************#

    if request.method == 'POST':

        img = request.files['img']

        p = {
            'name': request.form.get('name', ""),
            'student_id': request.form.get('student_id', ""),
            'major': request.form.get('major', ""),
            'age': request.form.get('age', ""),
            'money': request.form.get('money', ""),
            'img': img.filename,
        }

        img.save('temp.jpg')

        img_file = open('temp.jpg', 'rb')

        img_bin = img_file.read()

        img_file.close()

        result = yuncongserverlib.face_create('cj', img_bin)

        os.remove('temp.jpg')

        data = _getdata()

        if result[0]:

            yuncong_id = result[1]
            p['yuncong_id'] = yuncong_id

            data['people'].append(p)

            _setdata(data)

            flash('新增用户成功')

        else:

            flash('新增用户失败')

        return redirect('/')


@app.route('/delete_user', methods=['GET'])
def delete_user():
    student_id = request.args.get('student_id', "")
    data = _getdata()
    for i in range(len(data['people'])):
        if data['people'][i]['student_id'] == student_id:
            data['people'].pop(i)

            _setdata(data)

            flash('删除用户成功')

            return redirect('/')

    flash('删除用户失败')

    return redirect('/')


@app.route('/add_food', methods=['GET', 'POST'])
def add_food():
    # *******************  GET ******************#
    if request.method == 'GET':
        return render_template('add_food.html')

    # *******************  POST ******************#

    data = _getdata()

    food_id = 0
    for i in range(len(data['food'])):
        if int(data['food'][i]['food_id']) >= food_id:
            food_id = int(data['food'][i]['food_id']) + 1

    if request.method == 'POST':

        p = {
            'food_id': str(food_id),
            'name': request.form.get('name', ""),
            'hall': request.form.get('hall', ""),
            'cost': request.form.get('cost', ""),
            'materials': request.form.get('materials', ""),
            'vegetarian': request.form.get('vegetarian', ""),
            'taste': request.form.get('taste', ""),
            'times': 0,
        }

        data = _getdata()

        data['food'].append(p)

        _setdata(data)

        flash('新增菜品成功')

        return redirect('/')


@app.route('/delete_food', methods=['GET'])
def delete_food():
    food_id = request.args.get('food_id', "")
    data = _getdata()
    for i in range(len(data['food'])):
        if data['food'][i]['food_id'] == food_id:
            data['food'].pop(i)

            _setdata(data)

            flash('删除菜品成功')

            return redirect('/')

    flash('删除菜品失败')

    return redirect('/')



# *******************  API ******************#

@app.route('/get_info_by_student_id', methods=['GET'])
def get_info_by_student_id():
    student_id = request.args.get('student_id', "")

    data = _getdata()
    for p in data['people']:
        if p['student_id'] == student_id:
            return jsonify(p)
    return jsonify({})


@app.route('/get_info_by_yuncong_id', methods=['GET'])
def get_info_by_yuncong_id():
    yuncong_id = request.args.get('yuncong_id', "")
    yuncong_id = int(yuncong_id)

    data = _getdata()
    for p in data['people']:
        if p['yuncong_id'] == yuncong_id:
            return jsonify(p)
    return jsonify({})


@app.route('/add_cost', methods=['GET'])
def add_cost():
    new_cost = {'time': time.time(),
                'student_id': request.args.get('student_id', ""),
                'machine': request.args.get('machine', ""),
                'food': request.args.get('food', ""),
                'cost': request.args.get('cost', ""),
                'hall': request.args.get('hall', ""),
                'jiko': request.args.get('jiko', "")
                }

    data = _getdata()
    data['eating'].append(new_cost)
    _setdata(data)
    return jsonify({'result': True})


@app.route('/get_cost', methods=['GET'])
def get_cost():
    student_id = request.args.get('student_id', "")

    data = _getdata()
    money = 0
    name = ''
    for p in data['people']:
        if p['student_id'] == student_id:
            name = p['name']
            money = p['money']
    cost_list = []
    for i in data['eating']:
        if i['student_id'] == student_id:
            cost_list.append(i['cost'])
        if len(cost_list) == 5:
            break

    s = '您好{}同学，你目前余额为{}元\n最近的五笔消费为：\n'.format(name, money)
    for i in range(len(cost_list)):
        s += '[{}]: {}元\n'.format(i + 1, cost_list[i])
    return s


@app.route('/kv_add', methods=['POST'])
def kv_add():
    payload = request.get_data()
    p = json.load(payload)
    data = _getdata()
    data['kv'].append({'key': p['key'], 'value': p['value']})
    _setdata(data)
    return jsonify({'result': True})


@app.route('/kv_get', methods=['GET'])
def kv_get():
    p_key = request.args.get('key', '')

    data = _getdata()
    for p in data['kv']:
        if p['key'] == p_key:
            return p['value']
    return ''



# *******************  Inner Function ******************#

def _format_time(date):
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date))
app.add_template_global(_format_time)


def _getdata():
    fd = open('data.json', encoding='utf-8')
    s = fd.read()
    fd.close()
    data = json.loads(s)
    return data


def _setdata(data):
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
