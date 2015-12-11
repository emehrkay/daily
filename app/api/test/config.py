import os

from tornado.options import parse_config_file

import api.config


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.config.py');
parse_config_file(file)