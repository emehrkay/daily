from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler


class DayHandler(BaseHandler):

    def get(self, day=None):
        pass


class ListHandler(BaseHandler):

    def get(self, day=None):
        self.write('testing')

    def post(self):
        pass

    def put(self, _id):
        pass

    def delete(self, _id):
        pass


class ListItemHandler(BaseHandler):

    def get(self, list_id, item_id):
        pass

    def post(self, list_id, item_id):
        pass

    def put(self, list_id, item_id):
        pass

    def delete(self, list_id, item_id):
        pass


class ListItemPromoteHandler(BaseHandler):

    def post(self, list_id, item_id):
        pass

    def delete(self, list_id, item_id):
        pass


class ListCommentHandler(BaseHandler):

    def get(self, list_id, comment_id):
        pass

    def post(self, list_id, comment_id):
        pass

    def put(self, list_id, comment_id):
        pass

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
