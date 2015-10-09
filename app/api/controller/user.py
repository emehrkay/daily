from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler


class User(BaseHandler):

    def put(self, user_id):
        pass


ROUTES = (
    (r'/user/(\w+)', User),
)

APPLICATION.add_handlers(".*$", ROUTES)
