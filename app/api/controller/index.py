import sys

from api.bootstrap import APPLICATION
from api.controller.base import BaseHandler

from gizmo.error import GizmoException


class IndexHandler(BaseHandler):

    def get(self):
        self.response(message='Daily Server')


ROUTES = (
    (r'/', IndexHandler),
)

APPLICATION.add_handlers(".*$", ROUTES)