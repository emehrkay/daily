import json
import datetime
import urllib.parse as urlparse

from tornado import web, escape
from tornado.options import options


class BaseHandler(web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(BaseHandler, self).__init__(application, request, **kwargs)
        self.mapper = self.application.mapper

    def get_user(self):
        return None

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

    def get_model_by_id(self, _id, entity='v', enabled=True):
        return get_model_by_id(_id, entity, enabled)

    def response(self, data=None, message=None, status=200, errors=None):
        if not data:
            data = {}

        if not message:
            message = ''

        if not errors:
            errors = []

        json = {
            'status': status,
            'message': message,
            'errors': errors,
            'data': data,
        }

        self.write(json)

    def get_user(self):
        try:
            session_id = self.request.headers.get('AUTHORIZATION', None)
            g = self.mapper.gremlin
            g.V().has('"_label"', 'login_log').has('"session_id"', session_id)
            g.inE('"_label"', 'logged_in').outV()
            
            return self.mapper.query(gremlin=g).first()
        except Exception as e:
            return None


def get_model_by_id(_id, entity='v', enabled=True):
    """
    utility method used to get an entity (vertex or edge)
    by its _id value
    """
    g = MAPPER.gremlin

    getattr(g, entity.lower().upper())(str(_id))

    if enabled is not None:
        g.has("'enabled'", str(enabled).lower())

    return MAPPER.query(gremlin=g).first()

