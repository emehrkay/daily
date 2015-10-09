from gizmo.entity import Vertex
from gizmo.field import String, Boolean, DateTime, Float, List, Integer

from . import TYPE


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


class Tag(BaseVertex):
    name = String()


class User(BaseVertex):
    email = String()
    password = String()
