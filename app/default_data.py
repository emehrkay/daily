# script used to import the default data into the system
import sys
import json

from tornado.httpclient import HTTPClient
from tornado.options import options
from tornado.httputil import HTTPHeaders

import api.config
from api.bootstrap import MAPPER, REQUEST
from api.model.graph.vertex import *


request = HTTPClient()
base_uri = 'http://localhost:%s' % options.api_port


def body(data):
    return 'body=%s' % json.dumps(data)


def uri(path):
    return '%s%s' % (base_uri, path)


def req(path, method='GET', data=None, headers=None):
    if not data:
        data = {}

    if not headers:
        headers = {}

    args = {'body':body(data), 'headers': headers, 'method': method}
    u = uri(path)
    res = request.fetch(u, **args)
    j = res.body.decode('utf-8')

    try:
        js = json.loads(j)
        d = js.get('data')
    except Exception as e:
        js = {}
        d = {}

    return (res, js, d)


def post(path, data=None, headers=None):
    return req(method="POST", path=path, data=data, headers=headers)


def put(path, data=None, headers=None):
    return req(method="PUT", path=path, data=data, headers=headers)


try:
    gremlin = MAPPER.gremlin

    MAPPER.query(script="daily.V().map{it.get().remove()}")

    data = {'username': 'mark', 'password': 'mark', 'email': 'mark@mark.com'}
    res = post('/register', data=data)
    login = post('/login', data={'email': data['email'], 'password': data['password']})
    session = login[2].get('session_id')


except Exception as e:
    import traceback
    # print(traceback.format_exc())
    # traceback.print_stack(file=sys.stdout)
    # print('EXCEPTION!!!!!')
    # print(e)