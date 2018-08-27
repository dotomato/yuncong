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
    print(payload)
    if payload['result'] == 0:
        return True, payload['faceId']
    else:
        return False, -1
