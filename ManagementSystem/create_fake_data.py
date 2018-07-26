# -*- conding:utf-8 -*-

import time
import json
import random

name_list = ['黄浩岚', '湛淑兰', '竹飞兰', '清凌寒', '朱静云', '钱从丹',   '宰曼彤',   '西南非', '枯棕奈']
id_list = [20175635, 20174922, 20179467, 20175251, 20171504, 20171980, 20171328, 20171911, 20171322]
error_list = ["宿舍开门识别失败", "食堂点菜识别失败", "食堂点菜余额不足", "上课签到识别失败"]

def gen_time():
    return time.time() - random.random() * 24 * 60 * 60

def pick_id():
    return id_list[random.randint(0, len(id_list)-1)]

def gen_machine():
    return random.randint(0, 99)

def pick_error():
    return error_list[random.randint(0, len(error_list)-1)]

def format_time(date):
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date))

def fix_money(x):
    return int(x*100)/100

data = {}
data['people'] = []
for i in range(len(name_list)):
    data['people'].append(
        {
            'id': id_list[i],
            'name':name_list[i],
            'room':random.randint(0, 1000),
            'img':str(id_list[i])+'.jpg',
            'money': fix_money(100+random.random()*1000),
            'lessontime': 0.5 * random.randint(0, 6)
        })

data['eating'] = []
for i in range(100):
    data['eating'].append({'time':gen_time(), 'id':pick_id(), 'machine':gen_machine(), 'cost': fix_money(0.2*random.randint(10, 100))})

data['lesson'] = []
for i in range(100):
    data['lesson'].append({'time':gen_time(), 'id':pick_id(), 'machine':gen_machine()})

data['door'] = []
for i in range(100):
    data['door'].append({'time':gen_time(), 'id':pick_id(), 'machine':gen_machine()})

data['error'] = []
for i in range(100):
    data['error'].append({'time':gen_time(), 'id':pick_id(), 'machine':gen_machine(), 'errortype':pick_error()})


for key in ['eating', 'lesson', 'door', 'error']:
    data[key].sort(key=lambda x: x['time'], reverse=True)
    for item in data[key]:
        item['time'] = format_time(item['time'])


fd = open('data.json', 'w', encoding='utf-8')
json.dump(data, fd)
fd.close()
