import sys

from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler
from api.model.graph.vertex import User
from api.util import authorized

from gizmo.error import GizmoException


class LoginHandler(BaseHandler):

    def get(self):
        """utility method used to check if the current
        user has a valid seesion or not
        """
        self.write('testing')

    def post(self):
        errors = []
        data = {}
        email = self.get_arg('email')
        password = self.get_arg('password')
        g = self.mapper.gremlin.V().has('"email"', email).has('"password"', password)

        try:
            user = self.mapper.query(gremlin=g).first()
            login = self.mapper.login(user, True)
            data['session_id'] = login['session_id']
        except Exception as e:
            errors.append('There was an error logging in')

        self.response(errors=errors, data=data)


class LogoutHandler(BaseHandler):

    @authorized
    def get(self):
        self.put()

    @authorized
    def post(self):
        self.put()

    @authorized
    def put(self):
        errors = []
        status = 200

        try:
            user = self.get_user()
            self.mapper.logout(user)
        except Exception as e:
            errors.append('There was an error')
            status = 500

        self.response(errors=errors, status=status)


ROUTES = (
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
)

APPLICATION.add_handlers(".*$", ROUTES)
