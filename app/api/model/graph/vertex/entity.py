from gizmo.entity import Vertex
from gizmo.field import String, Boolean, DateTime, Float, List, Integer

from . import TYPE


class BaseVertex(Vertex):
    pass


class Comment(BaseVertex):
    _node_type = TYPE['COMMENT']
    content = String()


class ContentType(BaseVertex):
    _node_type = TYPE['CONTENT_TYPE']
    name = String()
    description = String()


class Item(BaseVertex):
    _node_type = TYPE['ITEM']
    content = String()
    actionable = Boolean(False)
    task = Boolean(True)
    active = Boolean(True)
    order = Integer()


class List(BaseVertex):
    _node_type = TYPE['LIST']
    name = String()
    active = Boolean(True)
    order = Integer()


class Tag(BaseVertex):
    _node_type = TYPE['TAG']
    name = String()


class User(BaseVertex):
    _node_type = TYPE['USER']
    email = String()
    password = String()
