import random
import json

from . import BaseTestCase, GraphTestMixin
from api.model.constants import DEFAULT_SERVER_MESSAGE
from api.bootstrap import MAPPER
from api.model.graph.vertex import User


class ApiTest(BaseTestCase):

    def test_can_connect_to_api_and_recieve_json(self):
        content_type = 'application/json; charset=UTF-8'
        fields = {
            'server_time': str,
            'message': str,
            'errors': list,
            'data': list,
        }

        def handle_get(response):
            j = json.loads(response.body.decode('utf-8'))

            self.assertEqual(content_type, response.headers['Content-Type'])

            for field, f_type in fields.items():
                self.assertIn(field, j)
                self.assertIsInstance(j[field], f_type)

            self.assertEqual(DEFAULT_SERVER_MESSAGE, j['message'])
            self.stop()

        self.send_request('/', handle_get, method='GET')


class UserTests(GraphTestMixin, BaseTestCase):

    def get_users(self):
        g = MAPPER.gremlin
        u = User()
        g.V().has('"_label"', str(u))

        return MAPPER.query(gremlin=g)

    def test_cannot_register_new_user_because_of_missing_fields(self):
        data = {
            'email': 'mark@mark.com',
            'password': 'password'
        }

        def handle(response):
            j = json.loads(response.body.decode('utf-8'))
            users = self.get_users()

            self.assertEqual(1, len(j['errors']))
            self.assertEqual('password2 field is required', j['errors'][0])
            self.assertEqual(0, len(users))
            self.stop()

        self.send_request('/register', handle, method='POST', body=self.body(data))

    def test_can_register_new_user(self):
        data = {
            'email': 'mark@mark.com',
            'password': 'password',
            'password2': 'password',
        }

        def handle(response):
            j = json.loads(response.body.decode('utf-8'))
            users = self.get_users()

            self.assertEqual(0, len(j['errors']))
            self.assertEqual(1, len(users))
            self.stop()

        self.send_request('/register', handle, method='POST', body=self.body(data))


if __name__ == '__main__':
    unittest.main()
