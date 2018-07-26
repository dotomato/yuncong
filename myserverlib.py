# -*- conding:utf-8 -*-

import urllib.request
import urllib.parse
import json

BASE_URL = 'http://localhost:5000'
REQUEST_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
    }

def get_info_by_id(_id):
    url = BASE_URL + '/get_info?id=' + str(_id)
    request = urllib.request.Request(url, headers=REQUEST_HEADERS, method='GET')
    result = urllib.request.urlopen(request).read().decode('utf-8')
    payload = json.loads(result)
    return payload
