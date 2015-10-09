from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler


class Login(BaseHandler):

    def get(self):
        """utility method used to check if the current
        user has a valid seesion or not
        """
        self.write('testing')

    def post(self):
        email = self.get_arg('email')
        password = self.get_arg('password')

        print(email, password)


class Logout(BaseHandler):

    def put(self, user_id):
        pass


class Registration(BaseHandler):

    def post(self):
        pass


ROUTES = (
    (r'/login', Login),
    (r'/logout', Logout),
    (r'/register', Registration),
)

APPLICATION.add_handlers(".*$", ROUTES)
