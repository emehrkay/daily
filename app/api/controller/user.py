from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler
from api.util import authorized


class User(BaseHandler):

    @authorized
    def get(self, user_id):
        print('Authorized', user_id)

    def put(self, user_id):
        pass


ROUTES = (
    (r'/user/(\w+)', User),
)

APPLICATION.add_handlers(".*$", ROUTES)
