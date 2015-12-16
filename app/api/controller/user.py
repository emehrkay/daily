from gizmo.error import GizmoException

from api.bootstrap import APPLICATION, MAPPER
from api.controller.base import BaseHandler
from api.model.graph.vertex import User
from api.util import authorized


class UserHandler(BaseHandler):

    @authorized
    def get(self, user_id):
        print('Authorized', user_id)

    @authorized
    def put(self, user_id):
        pass


class RegistrationHandler(BaseHandler):
    request_fields = {
        'required': ['email', 'password', 'password2'],
        'optional': []
    }

    def post(self):
        errors = []
        res_data = {}
        status = 200

        try:
            data = self.get_data()
            user = self.mapper.create_model(data=data, model_class=User)
            self.mapper.save(user).send()
            res_data = user.data
        except GizmoException as e:
            status = 400
            errors = e.errors

        self.response(errors=errors, data=res_data, status_code=status)


ROUTES = (
    (r'/register', RegistrationHandler),
    (r'/user/(\w+)', UserHandler),
)

APPLICATION.add_handlers(".*$", ROUTES)
