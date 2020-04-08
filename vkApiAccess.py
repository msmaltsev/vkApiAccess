# !usr/env/bin python3
# -*- coding: utf8 -*-

API_VER = '5.103'
try:
    with open('ACCESS_TOKEN', 'r', encoding='utf8') as at_file:
        ACCESS_TOKEN = at_file.read()
except Exception as e:
    print(e)
    ACCESS_TOKEN = ''

import requests as req
import json
import time


def callMethod(method, access_token = ACCESS_TOKEN, req_method = 'get', **kwargs):

    base = 'https://api.vk.com/method/%s'%method

    payload = kwargs
    payload['v'] = API_VER
    payload['access_token'] = access_token
    
    r = eval('req.%s(base, params=payload)'%req_method)
    t = r.text
    try: j = json.loads(t)
    except: 
        print(r.url)
        print(t)
        raise ConnectionError('no valid json reply received')

    if 'error' in j.keys():
        error_data = j['error']
        raise ConnectionError('Error {0}: {1}'.format(error_data['error_code'], error_data['error_msg']))
        response = {}
    else:
        response = j['response']

    return response


if __name__ == '__main__':

    r = callMethod('wall.get', users_ids = [13754027])
    print(r)

