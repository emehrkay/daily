from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler
from api.util import authorized


class UserHandler(BaseHandler):

    @authorized
    def get(self, user_id):
        print('Authorized', user_id)

    @authorized
    def put(self, user_id):
        pass


ROUTES = (
    (r'/user/(\w+)', UserHandler),
)

APPLICATION.add_handlers(".*$", ROUTES)
