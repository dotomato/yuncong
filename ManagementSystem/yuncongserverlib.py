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


def face_create(groupId, img_bin):
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
    if payload['result'] == 0:
        return True, payload['faceId']
    else:
        return False, -1


if __name__ == '__main__':
    group = 'cj'
    group_delete(group)
    group_create(group)
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

    # multi_face_identify(group, 'test/multi_face_identify_test.jpg')

    # print(tts('好像做爱做的事情啊~！'))
