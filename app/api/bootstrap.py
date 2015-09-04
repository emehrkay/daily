import os.path

from tornado.options import options
from tornado import web

from gizmo.mapper import Mapper
from gizmo.request import Binary, Async
from gremlinpy.gremlin import Gremlin


class Application(web.Application):
    """main appliction launcher"""

    def __init__(self):
        settings = {
            'debug': True,
            'autoescape': None,
            'upload_dir': options.upload_dir,
        }

        routes = []

        web.Application.__init__(self, routes, **settings)

        self.mapper = MAPPER


REQUEST = Async(options.rexster_host, options.rexster_graph, port=options.rexster_port)
GREMLIN = Gremlin()
MAPPER = Mapper(REQUEST, GREMLIN, auto_commit=options.rexster_auto_commit)
APPLICATION = Application()
