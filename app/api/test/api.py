import random
import json

from . import BaseTestCase
from api.model.constants import DEFAULT_SERVER_MESSAGE


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


if __name__ == '__main__':
    unittest.main()
