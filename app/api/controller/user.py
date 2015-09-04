from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler


class Test(BaseHandler):

    def get(self):
        self.write('testing')


ROUTES = (
    (r'/', Test),
)

APPLICATION.add_handlers(".*$", ROUTES)

print(Test)