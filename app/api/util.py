import functools

from tornado.web import HTTPError

def authorized(method):
    """
    simple decorator used to see if there is an authorized
    user for the request method
    """
    @functools.wraps(method)
    def _method(self, *args, **kwargs):
        auth = self.request.headers.get('AUTHORIZATION', None)

        if auth:
            g = self.mapper.gremlin
            where = '__.values("valid_until").is(gt(%s))' % 0
            g.V().has('"_label"', 'login_log').has('"session_id"', auth)
            g.unbound('where', where)
            auth = len(self.mapper.query(gremlin=g)) > 0

        if not auth:
            raise HTTPError(401)
        else:
            method(self, *args, **kwargs)
    return _method
