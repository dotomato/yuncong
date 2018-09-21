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

# *******************  YunCong Configuration ******************#
group = 'cj'


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


@app.route('/all_eating', methods=['GET', 'POST'])
def all_eating():
    return render_template('all_eating.html', data=_getdata())


@app.route('/add_user_0', methods=['GET'])
def add_user_0():
    # *******************  GET ******************#
    if request.method == 'GET':
        return render_template('add_user_0.html')


@app.route('/add_user_1', methods=['POST'])
def add_user_1():
    # *******************  POST ******************#

    if request.method == 'POST':

        img = request.files['img']

        img.save('temp.jpg')

        img_file = open('temp.jpg', 'rb')

        img_bin = img_file.read()

        img_file.close()

        result = yuncongserverlib.face_attribute(img_bin)

        if result[0]:

            age = result[1]
            gender = result[2]

            if gender == '-1':
                gender = '女'
            else:
                gender = '男'

            flash('人脸属性提取成功')

            return render_template('add_user_1.html', age=age, gender=gender)

        else:

            flash('人脸属性提取失败')

            return render_template('add_user_1.html', age='', gender='')

@app.route('/add_user_2', methods=['POST'])
def add_user_2():

    # *******************  POST ******************#
    if request.method == 'POST':

        p = {
            'name': request.form.get('name', ""),
            'gender': request.form.get('gender', ""),
            'student_id': request.form.get('student_id', "000"),
            'major': request.form.get('major', ""),
            'age': request.form.get('age', "18"),
            'money': request.form.get('money', "0.00"),
            'phone': request.form.get('phone', "00000000000"),
        }

        img_file = open('temp.jpg', 'rb')

        img_bin = img_file.read()

        img_file.close()

        result = yuncongserverlib.face_create(group, img_bin)

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


@app.route('/mod_user', methods=['GET', 'POST'])
def mod_user():
    student_id = request.args.get('student_id', "")
    data = _getdata()

    # *******************  GET ******************#
    if request.method == 'GET':
        for p in data['people']:
            if p['student_id'] == student_id:
                return render_template('mod_user.html', cur_user=p)
        return redirect('/')

    # *******************  POST ******************#

    if request.method == 'POST':

        img = request.files['img']

        new_p = {
            'name': request.form.get('name', ""),
            'gender': request.form.get('gender', ""),
            'student_id': request.form.get('student_id', "000"),
            'major': request.form.get('major', ""),
            'age': request.form.get('age', "18"),
            'money': request.form.get('money', "0.00"),
            'phone': request.form.get('phone', "00000000000"),
            'img': img.filename,
        }

        for p in data['people']:
            if p['student_id'] == new_p['student_id']:

                if new_p['img'] != '':
                    img.save('temp.jpg')

                    img_file = open('temp.jpg', 'rb')

                    img_bin = img_file.read()

                    img_file.close()

                    result = yuncongserverlib.face_edit(group, p['yuncong_id'], img_bin)

                    os.remove('temp.jpg')

                    p['img'] = new_p['img']

                p['name'] = new_p['name']
                p['gender'] = new_p['gender']
                p['major'] = new_p['major']
                p['age'] = new_p['age']
                p['phone'] = new_p['phone']

                _setdata(data)

                flash('修改用户信息成功')

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


@app.route('/start_train', methods=['GET'])
def start_train():
    flash('训练模型成功')

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


@app.route('/add_book', methods=['GET'])
def add_book():
    new_cost = {'time': _format_time(time.time()),
                'student_id': request.args.get('student_id', ""),
                'machine': request.args.get('machine', ""),
                'food': request.args.get('food', ""),
                # 'cost': request.args.get('cost', ""),
                'hall': request.args.get('hall', ""),
                'jiko': request.args.get('jiko', ""),
                'uuid': _generate_uuid(),
                'number': _generate_number()
                }

    data = _getdata()

    for p in data['food']:
        if p['name'] == new_cost['food']:
            new_cost['cost'] = p['cost']

            data['book'].append(new_cost)
            data['eating'].insert(0, new_cost)

            cost = new_cost['cost']
            student_id = new_cost['student_id']
            for p1 in data['people']:
                if p1['student_id'] == student_id:
                    p1['money'] = '%0.2f' % (float(p1['money']) - float(cost))
                    break

            _setdata(data)
            return jsonify({'result': True})

    return jsonify({'result': False})


@app.route('/add_book_instant', methods=['GET'])
def add_book_instant():
    new_cost = {'time': _format_time(time.time()),
                'student_id': request.args.get('student_id', ""),
                'machine': request.args.get('machine', ""),
                'food': request.args.get('food', ""),
                # 'cost': request.args.get('cost', ""),
                'hall': request.args.get('hall', ""),
                'jiko': request.args.get('jiko', ""),
                'uuid': _generate_uuid(),
                'number': _generate_number_instant()
                }

    data = _getdata()

    for p in data['food']:
        if p['name'] == new_cost['food']:
            new_cost['cost'] = p['cost']

            data['book'].append(new_cost)
            data['eating'].insert(0, new_cost)

            cost = new_cost['cost']
            student_id = new_cost['student_id']
            for p1 in data['people']:
                if p1['student_id'] == student_id:
                    p1['money'] = '%0.2f' % (float(p1['money']) - float(cost))
                    break

            _setdata(data)
            return jsonify({'result': True})

    return jsonify({'result': False})


# 删除book记录，并对学生的余额进行扣费
@app.route('/finish_book', methods=['GET'])
def finish_book():
    _uuid = request.args.get('uuid', "")
    data = _getdata()
    for p in data['book']:
        if p['uuid'] == _uuid:
            data['book'].remove(p)
            _setdata(data)
            return jsonify({'result': True})

    return jsonify({'result': False})


@app.route('/get_book_list', methods=['GET'])
def get_book_list():
    data = _getdata()
    return jsonify(data['book'])


@app.route('/get_number', methods=['GET'])
def get_number():
    student_id = request.args.get('student_id', "")

    data = _getdata()
    for p in data['eating']:
        if p['student_id'] == student_id and 0 < p['number'] < 1000:
            payload = jsonify(p)
            p['number'] = -p['number']
            _setdata(data)
            return payload
    return jsonify({})


@app.route('/get_food_list', methods=['GET'])
def get_food_list():
    data = _getdata()
    return jsonify(data['food'])


@app.route('/get_food', methods=['GET'])
def get_food():
    name = request.args.get('name', "")
    data = _getdata()
    for p in data['food']:
        if p['name'] == name:
            return jsonify(p)
    return jsonify({})


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
    food_list = []
    hall_list = []
    for i in data['eating']:
        if i['student_id'] == student_id:
            cost_list.append(i['cost'])
            food_list.append(i['food'])
            hall_list.append(i['hall'])
        if len(cost_list) == 10:
            break

    s = '您好{}同学，你目前余额为{}元\n最近的十笔消费为：\n'.format(name, money)
    for i in range(len(cost_list)):
        s += '[{}]: {}元 {} {}\n'.format(i + 1, cost_list[i], food_list[i], hall_list[i])
    return s


@app.route('/get_recommend', methods=['GET'])
def get_recommend():
    student_id = request.args.get('student_id', "")

    data = _getdata()
    food = random.choice(data['food'])

    return jsonify(food)


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

def _generate_uuid():
    return str(uuid.uuid4()).lower()


def _format_time(date):
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date))


def _generate_number():
    return random.randint(100, 999)


def _generate_number_instant():
    return random.randint(1000, 9999)


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
    app.run(host='0.0.0.0', debug=True, port=5000)
