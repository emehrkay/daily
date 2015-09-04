from tornado.options import options

from gizmo.mapper import _GenericMapper, Query, Mapper
from gizmo.utils import current_date_time
from gizmo.event import MapperMixin

from gremlinpy.gremlin import Gremlin, Function
from gremlinpy.statement import GetEdge


from . import TYPE, User, Item, List, Tag
from .mixin import TagMixin
from api.model.graph.edge import TYPE as ETYPE


class BaseMapper(_GenericMapper):
    pass


class ItemMapper(TagMixin, BaseMapper):
    model = Item


class ListMapper(BaseMapper):
    model = List


class TagMapper(BaseMapper):
    model = Tag
    unique_fields = ('name',)


class UserMapper(BaseMapper):
    model = User

