# import pudb; pu.db
import json
import random

from tornado.testing import AsyncHTTPTestCase

from . import config
from api.bootstrap import APPLICATION, MAPPER
from api import controller


MAPPER.logger = None


class BaseTestCase(AsyncHTTPTestCase):

    def setUp(self):
        MAPPER.logger = None
        super(BaseTestCase, self).setUp()

    def body(self, data):
        return 'body=%s' % json.dumps(data)

    def get_app(self):
        return APPLICATION

    def send_request(self, url, callback, wait=True, **kwargs):
        """
        set wait to False if you're calling this method within the context of
        another reequest see the auth_tests logout for example
        """
        client = self.get_http_client()
        client.fetch(self.get_url(url), callback, **kwargs)

        if wait:
            self.wait(timeout=50000)


class GraphTestMixin(object):

    def truncate_graph(self):
        script = "%s.V().map{it.get().remove()}" % str(MAPPER.gremlin.gv)

        MAPPER.query(script=script)

    def setUp(self):
        self.truncate_graph()
        super(GraphTestMixin, self).setUp()

    def tearDown(self):
        # self.truncate_graph()
        super(GraphTestMixin, self).tearDown()
