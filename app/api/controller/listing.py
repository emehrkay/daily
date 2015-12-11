from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler
from api.util import authorized


class DayHandler(BaseHandler):

    @authorized
    def get(self, day=None):
        pass


class ListHandler(BaseHandler):

    @authorized
    def get(self, day=None):
        self.write('testing')

    @authorized
    def post(self):
        pass

    @authorized
    def put(self, _id):
        pass

    @authorized
    def delete(self, _id):
        pass


class ListItemHandler(BaseHandler):

    @authorized
    def get(self, list_id, item_id):
        pass

    @authorized
    def post(self, list_id, item_id):
        pass

    @authorized
    def put(self, list_id, item_id):
        pass

    @authorized
    def delete(self, list_id, item_id):
        pass


class ListItemPromoteHandler(BaseHandler):

    @authorized
    def post(self, list_id, item_id):
        pass

    @authorized
    def delete(self, list_id, item_id):
        pass


class ListCommentHandler(BaseHandler):

    @authorized
    def get(self, list_id, comment_id):
        pass

    @authorized
    def post(self, list_id, comment_id):
        pass

    @authorized
    def put(self, list_id, comment_id):
        pass

    @authorized
    def delete(self, list_id, comment_id):
        pass


ROUTES = (
    (r'/day(?:/(\w+)?)?', DayHandler),
    (r'/list(?:/(\w+)?)?', ListHandler),
    (r'/list/(\w+)/item(?:/(\w+)?)?', ListItemHandler),
    (r'/list/(\w+)/item(?:/(\w+)?)?/promote', ListItemPromoteHandler),
    (r'/list/(\w+)/comment(?:/(\w+)?)?', ListCommentHandler),
)

APPLICATION.add_handlers(".*$", ROUTES)
