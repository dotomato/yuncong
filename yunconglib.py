# -*- conding:utf-8 -*-

import urllib.request
import urllib.parse
import json
import base64
import time
import os
from PIL import Image, ImageDraw, ImageFont
from aip import AipSpeech
import myserverlib

BASE_URL = 'http://120.25.161.56:8000'
REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
    }
NAME_DATA_FILE = 'name_data.json'

# ***************** BaiDu Ai API *******************

APP_ID = '11592048'
API_KEY = 'bcj2xdLuu8z0bo8RuGQ1Zt73'
SECRET_KEY = 'XnYvfdw0134VYZOXcud1qN4zAfSfRHsX'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def group_create(groupId):
    url = BASE_URL+'/face/clustering/group/create'
    values = {
        'groupId': groupId,
        'tag': None
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, REQUEST_HEADERS)
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload['result'] == 0


def group_delete(groupId):
    url = BASE_URL+'/face/clustering/group/delete'
    values = {
        'groupId': groupId
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, REQUEST_HEADERS)
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload['result'] == 0


def face_create(groupId, img_bin, people_name):
    url = BASE_URL+'/face/clustering/face/create'
    values = {
        'groupId': groupId,
        'tag': 'fuck',
        'img': base64.b64encode(img_bin)
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, REQUEST_HEADERS)
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    print(payload)
    if payload['result'] == 0:
        _save_name(payload['faceId'], people_name)
        return True, payload['faceId']
    else:
        return False, -1


def _save_name(yuncong_id, name):
    fp = open(NAME_DATA_FILE, 'r', encoding='utf-8')
    data = json.load(fp)
    fp.close()

    data[yuncong_id] = name

    fp = open(NAME_DATA_FILE, 'w', encoding='utf-8')
    json.dump(data, fp)
    fp.close()


def _get_name(yuncong_id):
    fp = open(NAME_DATA_FILE, 'r', encoding='utf-8')
    data = json.load(fp)
    fp.close()

    return data[yuncong_id]


# 传入一个文件夹，里面只能有人脸图片，文件名即作为人名
def recreate_yuncong_data_from_direcory(groupId, dir):
    print('group_delete:', group_delete(groupId))
    print('group_create:', group_create(groupId))
    img_file_list = list(os.walk(dir))[0][2]
    print('scan img:', img_file_list)
    for img_file in img_file_list:
        with open(os.path.join(dir, img_file), 'rb') as f:
            img_bin = f.read()
            people_name = img_file.split('.')[0]
            result = face_create(groupId, img_bin, people_name)
            print('add face:', people_name, result)


def face_identify(groupId, img_bin):
    url = BASE_URL+'/face/recog/group/identify'
    values = {
        'groupId': groupId,
        'img': base64.b64encode(img_bin),
        'topN': 1
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, REQUEST_HEADERS)
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    if payload['result'] == 0:
        people_name = _get_name(payload['faces'][0]['faceId'])
        return True, people_name
    else:
        return False, ''


def multi_face_identify(groupId, img_path):
    img_fd = open(img_path, 'rb')
    img_bin = img_fd.read()
    img_fd.close()

    url = BASE_URL+'/face/recog/group/identify/ext1'
    values = {
        'groupId': groupId,
        'img': base64.b64encode(img_bin)
    }
    data = urllib.parse.urlencode(values).encode('utf-8')
    request = urllib.request.Request(url, data, REQUEST_HEADERS)
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    if payload['result'] == 0:
        im = Image.open(img_path)
        draw = ImageDraw.Draw(im)
        draw.ink = 0x0000ff
        font = ImageFont.truetype('simsun.ttc', 18, encoding='utf-8')
        for face in payload['faces']:
            name = _get_name(face['faceId'])
            name = myserverlib.get_info_by_id(name)['name']
            x, y, w, h = face['x'], face['y'], face['width'], face['height']
            draw.rectangle((x, y, x+w, y+h), outline='red')
            draw.text((x, y+h), name, font=font)
        im.save('multi_face_identify_result.jpg')
        return True, 'multi_face_identify_result.jpg'
    else:
        return False, ''


def tts(text):
    result = client.synthesis(text, 'zh', 1, {'per': '4'})
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
        return 'audio.mp3'
    print(result)
    return None


if __name__ == '__main__':
    group = 'cj'
    # recreate_yuncong_data_from_direcory(group, 'train')
    #
    # test_img1 = open('test/1_c.jpg', 'rb').read()
    # print('test 1_c:', face_identify(group, test_img1))
    #
    # test_img2 = open('test/2_d.jpg', 'rb').read()
    # print('test 2_d:', face_identify(group, test_img2))
    #
    # test_img3 = open('test/3_i.jpg', 'rb').read()
    # print('test 3_i:', face_identify(group, test_img3))

    multi_face_identify(group, 'test/multi_face_identify_test.jpg')

    # print(tts('好像做爱做的事情啊~！'))
