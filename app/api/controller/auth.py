from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler
from api.model.graph.vertex import User
from api.util import authorized


class Login(BaseHandler):

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
        # import pudb; pu.db
        try:
            user = self.mapper.query(gremlin=g).first()
            print('UXER', user, user.data)
            login = self.mapper.login(user, True)
            data['session_id'] = login['session_id']
        except Exception as e:
            print(self.mapper)
            print(e)
            errors.append('There was an error logging in')

        self.response(errors=errors, data=data)


class Logout(BaseHandler):

    @authorized
    def put(self):
        errors = []
        status = 200

        try:
            user = self.get_user()
            print(user, user.data)
            self.mapper.logout(user)
        except Exception as e:
            print(e)
            errors.append('There was an error')
            status = 500

        self.response(errors=errors, status=status)


class Registration(BaseHandler):

    def post(self):
        pass


ROUTES = (
    (r'/login', Login),
    (r'/logout', Logout),
    (r'/register', Registration),
)

APPLICATION.add_handlers(".*$", ROUTES)
