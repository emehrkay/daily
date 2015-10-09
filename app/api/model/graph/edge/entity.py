from gizmo.entity import Edge
from gizmo.field import String, Boolean, DateTime, Float, List

from . import TYPE


class BaseEdge(Edge):
    pass


class DayList(BaseEdge):
    pass


class HasComment(BaseEdge):
    pass


class HasItem(BaseEdge):
    pass


class HasList(BaseEdge):
    pass


class HasTag(BaseEdge):
    pass


class IsContent(BaseEdge):
    pass


class IsOwner(BaseEdge):
    pass


class UserList(BaseEdge):
    pass
