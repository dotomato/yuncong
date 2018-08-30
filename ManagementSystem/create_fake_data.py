# -*- conding:utf-8 -*-

import time
import json
import random
import yuncongserverlib

group = 'cj'

name_list = ['杨骏', '陈君', '周鸿宇', '孟海宁', '魏润宇', '顾一']
id_list = ['201618001027062', '201628017729007', '201628017728027', '201718013229035', '201618001027061', '201618001027063']
phone_list = ['15611102621', '18222333097',  '15835781246', '13758467912', '13054871389', '18235467192']
gender_list = ['男', '男', '男', '女', '男', '女']
major_list = ['电子信息工程', '计算机应用技术', '模式识别', '电子信息工程', '电子信息工程', '电子信息工程']
age_list = ['23', '24', '23', '22', '23', '22', '23']

food_list = ['小炒肉', '木须肉', '手撕包菜', '清焖莲子', '青葱牛柳', '苦瓜炒牛肉', '龙井虾仁', '鱼香肉丝', '凉拌黑木耳', '西红柿炒鸡蛋', '酸辣土豆丝', '红烧狮子头', '孜然羊肉']
materials_list = ['猪肉', '牛肉', '包心菜', '莲子', '牛肉', '牛肉', '虾肉', '鱼肉', '黑木耳', '鸡蛋', '土豆', '猪肉', '羊肉']
vegetarian_list = ['肉菜', '肉菜', '素菜', '素菜', '肉菜', '肉素混合', '肉素混合', '肉素混合', '素菜', '肉素混合', '素菜', '肉菜', '肉菜']
taste_list = ['酸', '甜', '苦', '辣']
money_list = [10, 12, 14, 16, 18, 20]
food_money_list = random.choices(money_list, k=len(food_list))
hall_list = ['特色风味食堂', '东区一食堂', '西区一食堂', '西区二食堂']
food_hall_list = random.choices(hall_list, k=len(food_list))
jiko_list = ['无', '免辣', '免葱', '免汁']


def gen_time():
    return time.time() - random.random() * 24 * 60 * 60

def gen_machine():
    return random.randint(0, 99)


def format_time(date):
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(date))


def fix_money(x):
    return int(x * 100) / 100


def get_student_fav_food(i):
    student_id = id_list[i]
    h = hash(student_id)
    c = len(food_list)
    return abs(h) % c


def get_student_eating_food(i):
    fav = get_student_fav_food(i)
    if random.random() < 0.6:
        return fav
    else:
        return random.randint(0, len(food_list)-1)


def get_student_fav_jiko(i):
    student_id = id_list[i]
    h = hash(student_id)
    c = len(jiko_list)
    return abs(h) % c


def get_student_eating_jiko(i):
    fav = get_student_fav_jiko(i)
    if random.random() < 0.6:
        return fav
    else:
        return random.randint(0, len(jiko_list)-1)


data = {'people': [], 'eating': [], 'food': [], 'book': [], 'kv': []}

yuncongserverlib.group_delete(group)
yuncongserverlib.group_create(group)

for i in range(len(name_list)):
    img_file = open('people/'+id_list[i]+'.jpg', 'rb')
    img_bin = img_file.read()
    img_file.close()
    result = yuncongserverlib.face_create(group, img_bin)
    print(result)
    if not result[0]:
        exit(-1)

    data['people'].append(
        {
            'yuncong_id': result[1],
            'student_id': id_list[i],
            'name': name_list[i],
            'gender': gender_list[i],
            'major': major_list[i],
            'age': age_list[i],
            'room': str(random.randint(0, 1000)),
            'phone': phone_list[i],
            'img': id_list[i] + '.jpg',
            'money': str(fix_money(100 + random.random() * 1000))
        })


for i in range(len(food_list)):
    data['food'].append(
        {
            'food_id': str(i),
            'name': food_list[i],
            'cost': food_money_list[i],
            'hall': food_hall_list[i],
            'materials': materials_list[i],
            'vegetarian': vegetarian_list[i],
            'taste': random.choice(taste_list),
            'times': random.randint(300, 700)
         }
    )


for i in range(100):
    student_index = random.randint(0, len(name_list) - 1)
    x1 = get_student_eating_food(student_index)
    x2 = get_student_eating_jiko(student_index)
    data['eating'].append(
        {'time': gen_time(),
         'student_id': id_list[student_index],
         'machine': gen_machine(),
         'food': food_list[x1],
         'cost': food_money_list[x1],
         'hall': food_hall_list[x1],
         'jiko': jiko_list[x2],
         'number': -1
         })


for key in ['eating']:
    data[key].sort(key=lambda x: x['time'], reverse=True)
    for item in data[key]:
        item['time'] = format_time(item['time'])


fd = open('data.json', 'w', encoding='utf-8')
json.dump(data, fd)
fd.close()
