# -*- conding:utf-8 -*-

import urllib.request
import urllib.parse
import json
import base64
import os

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


def face_create(groupId, img_bin, people_name):
    url = BASE_URL+'/face/clustering/face/create'
    values = {
        'groupId': groupId,
        'tag': base64.b64encode(people_name.encode('utf-8')),
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


# 传入一个文件夹，里面只能有人脸图片，文件名即作为人名
def recreate_yuncong_data_from_direcory(groupId, dir):
    print('group_delete:', group_delete(groupId))
    print('group_delete:', group_create(groupId))
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
        people_name = payload['faces'][0]['tag']
        people_name = base64.b64decode(people_name).decode('utf-8')
        return True, people_name
    else:
        return False, ''


if __name__ == '__main__':
    group = 'cj'
    recreate_yuncong_data_from_direcory(group, 'train')

    test_img1 = open('test/1_c.jpg', 'rb').read()
    print('test 1_c:', face_identify(group, test_img1))

    test_img2 = open('test/2_d.jpg', 'rb').read()
    print('test 2_d:', face_identify(group, test_img2))

    test_img3 = open('test/3_i.jpg', 'rb').read()
    print('test 3_i:', face_identify(group, test_img3))