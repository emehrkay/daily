from tornado.options import options, define
import os

define('api_port', 6000, 'the port that the api runs on')
define('site_dir', os.path.join(os.path.dirname(__file__)), 'root site directory')
define('upload_dir', os.path.join(os.path.dirname(__file__), 'static', 'upload'))
define('rexster_host', 'localhost')
define('rexster_graph', 'daily')
define('rexster_port', 8182)
define('rexster_auto_commit', True)
define('pagination', 50, 'the number of results to return per page')
define('reset_lifetime', 60 * 60 * 24, 'the lifetime of a password reset token')
define('mailgun_key', 'key-70e3139b23bda35b6d4c77c39c4ad45b', 'the key from mailgun')
define('mailgun_uri', 'https://api.mailgun.net/v3/sandboxea667b10c52c453685cb8c4a03757592.mailgun.org/messages', 'uri used to send emails')
