#!/usr/bin/env python
# encoding: utf-8
import os.path

from tornado import httpserver, ioloop, web
from tornado.options import options

from api import config
from api.bootstrap import APPLICATION
from api import controller

from tornado.web import HTTPError


if __name__ == '__main__':
    """Start the application"""
    #try:
    http_server = httpserver.HTTPServer(APPLICATION)
    http_server.listen(options.api_port)
    ioloop.IOLoop.instance().start()
    # except HTTPError as e:
    #     raise e
    # except Exception as e:
    #     import traceback
    #     print(traceback.format_exc())
    #     traceback.print_stack()
    #     print(e)
