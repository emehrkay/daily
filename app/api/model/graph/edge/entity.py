from gizmo.entity import Edge
from gizmo.field import String, Boolean, DateTime, Float, List

from . import TYPE


class BaseEdge(Edge):
    pass


class HasComment(BaseEdge):
    _node_type = TYPE['has_comment']


class HasItem(BaseEdge):
    _node_type = TYPE['has_item']


class HasList(BaseEdge):
    _node_type = TYPE['has_list']


class HasTag(BaseEdge):
    _node_type = TYPE['has_tag']


class IsContent(BaseEdge):
    _node_type = TYPE['is_content']


class UserList(BaseEdge):
    _node_type = TYPE['USER_LIST']
