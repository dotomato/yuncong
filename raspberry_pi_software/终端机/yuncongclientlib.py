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

# ***************** BaiDu Ai API *******************


APP_ID = '11592048'
API_KEY = 'bcj2xdLuu8z0bo8RuGQ1Zt73'
SECRET_KEY = 'XnYvfdw0134VYZOXcud1qN4zAfSfRHsX'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


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
        return True, payload['faces'][0]['faceId']
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
            yuncond_id = face['faceId']
            name = myserverlib.get_info_by_yuncong_id(yuncond_id)['name']
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

    test_img1 = open('test/123.jpg', 'rb').read()
    result = face_identify(group, test_img1)
    print(result)
    print('test 123:', myserverlib.get_info_by_yuncong_id(result[1]))

    test_img1 = open('test/234.jpg', 'rb').read()
    result = face_identify(group, test_img1)
    print(result)
    print('test 123:', myserverlib.get_info_by_yuncong_id(result[1]))

    test_img1 = open('test/345.jpg', 'rb').read()
    result = face_identify(group, test_img1)
    print(result)
    print('test 123:', myserverlib.get_info_by_yuncong_id(result[1]))

    multi_face_identify(group, 'test/aaa.jpg')

    # print(tts('好像做爱做的事情啊~！'))
