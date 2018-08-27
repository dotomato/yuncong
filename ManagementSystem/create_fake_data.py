# -*- conding:utf-8 -*-

import time
import json
import random

name_list = ['黄浩岚', '湛淑兰', '竹飞兰', '清凌寒', '朱静云', '钱从丹', '宰曼彤', '西南非', '枯棕奈']
id_list = ['20175635', '20174922', '20179467', '20175251', '20171504', '20171980', '20171328', '20171911', '20171322']
food_list = ['小炒肉', '木须肉', '手撕包菜', '清焖莲子', '青葱牛柳', '苦瓜炒牛肉', '龙井虾仁', '鱼香肉丝', '凉拌黑木耳', '西红柿炒鸡蛋', '酸辣土豆丝', '红烧狮子头', '孜然羊肉']
materials_list = ['猪肉', '牛肉', '羊肉', '素菜']
vegetarian_list = ['素菜', '肉菜', '肉素混合']
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

data = {'people': [], 'eating': [], 'food': [], 'kv': []}

# for i in range(len(name_list)):
#     data['people'].append(
#         {
#             'id': id_list[i],
#             'name': name_list[i],
#             'room': random.randint(0, 1000),
#             'img': str(id_list[i]) + '.jpg',
#             'money': fix_money(100 + random.random() * 1000),
#         })

for i in range(10):
    x = random.randint(0, len(food_list)-1)
    data['eating'].append(
        {'time': gen_time(),
         'student_id': random.choice(id_list),
         'machine': gen_machine(),
         'food': food_list[x],
         'cost': food_money_list[x],
         'hall': food_hall_list[x],
         'jiko': random.choice(jiko_list)})

for i in range(len(food_list)):
    data['food'].append(
        {
            'food_id': str(i),
            'name': food_list[i],
            'cost': food_money_list[i],
            'hall': food_hall_list[i],
            'materials': random.choice(materials_list),
            'vegetarian': random.choice(vegetarian_list),
            'taste': random.choice(taste_list),
            'times': random.randint(300, 700)
         }
    )

for key in ['eating']:
    data[key].sort(key=lambda x: x['time'], reverse=True)
    for item in data[key]:
        item['time'] = format_time(item['time'])

fd = open('data.json', 'w', encoding='utf-8')
json.dump(data, fd)
fd.close()
