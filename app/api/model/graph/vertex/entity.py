from gizmo.entity import Vertex
from gizmo.field import String, Boolean, DateTime, Float, List, Integer

from . import get_a_uuid


class BaseVertex(Vertex):
    pass


class Comment(BaseVertex):
    content = String()


class ContentType(BaseVertex):
    name = String()
    description = String()


class Day(BaseVertex):
    epoch_day = Integer()


class Item(BaseVertex):
    content = String()
    actionable = Boolean(False)
    task = Boolean(True)
    active = Boolean(True)
    order = Integer()


class List(BaseVertex):
    name = String()
    active = Boolean(True)
    order = Integer(value=0)


class LoginLog(BaseVertex):
    session_id = String(value=get_a_uuid)
    valid_until = DateTime()


class Tag(BaseVertex):
    name = String()


class User(BaseVertex):
    email = String()
    password = String()
