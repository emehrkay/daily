import json
import datetime
import urllib.parse as urlparse

from tornado import web, escape
from tornado.options import options


class BaseHandler(web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)

    def get_arg(self, name=None, default=None):
        """
        method used to get the argument from the request
        all requests are sent as encoded json tied to the body argument
        PUT methods do not get data from self.request.get_argument
        so direct parsing of self.request.body is used


        """
        req = urlparse.parse_qs(self.request.body)
        body = {}

        for k in req:
            body[k] = req[k][0]

        body = body.get(b'body', b'{}').decode("utf-8")
        body = json.loads(body)

        if name:
            body = body.get(name, None)
            
            if not body:
                body = self.get_argument(name, default)

        return body