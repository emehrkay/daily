from tornado.options import options

from gizmo.mapper import _GenericMapper, Query, Mapper
from gizmo.utils import current_date_time
from gizmo.event import MapperMixin

from gremlinpy.gremlin import Gremlin, Function
from gremlinpy.statement import GetEdge

from . import User, Item, List, Tag, Day, LoginLog
from .mixin import TagMixin
from api.model.graph.edge.entity import *


class BaseMapper(_GenericMapper):

    def add_owner(owner, entity):
        return self.mapper.connect(owner, entity, edge_model=IsOwner)


class DayMapper(BaseMapper):
    model = Day

    def get_or_create(self, epoch_day, user):
        mapper = self.mapper
        g = mapper.gremlin

        # get or create the day
        # get or create the main list for the user for that day
        g.V().has('_type', 'day').getProperty('epoch_day', epoch_day)
        g.func('in_v', 'day_list').func('in_v', 'has_list')

        try:
            return mapper.query(gremlin=g).first()
        except Exception as e:
            day = Day({'day': epoch_day})
            main = List()
            list_mapper = mapper.get_mapper(main)

            self.add_list(day, main)
            list_mapper.add_user(main, user)
            self.mapper.send()

            return main

    def add_list(self, day, listing):
        self.mapper.connect(listing, day, edge_model=DayList)


class ItemMapper(TagMixin, BaseMapper):
    model = Item


class ListMapper(BaseMapper):
    model = List

    def add_user(self, listing, user):
        self.add_owner(user, listing)
        return self.mapper.connect(user, listing, edge_model=HasList)

    def add_item(self, listing, item):
        return self.mapper.connect(lisitng, item, edge_model=HasItem)


class TagMapper(BaseMapper):
    model = Tag
    unique_fields = ('name',)


class UserMapper(BaseMapper):
    model = User
    unique_fields = ('email',)
    error_on_non_unique = True

    def logout(self, user):
        g = self.mapper.start(user)
        # TODO: change this to a where class once gremlinpy is upadted to support predicates
        # we only want to modify the vertices who have a valid_until value
        # outE('_label', 'logged_in').inV().where(__.values('valid_until').is(gt(0)))
        where = "__.values('valid_until').is(gt(0))"
        g.outE("'_label'", 'logged_in').inV().unbound('where', where)
        sessions = self.mapper.query(gremlin=g)

        if len(sessions):
            for sess in sessions:
                sess['valid_until'] = 0
                sess['session_id'] = ''
                self.mapper.save(sess)

            self.mapper.send()

    def login(self, user, invalidate_sessions=False):
        login = LoginLog()

        if invalidate_sessions:
            self.logout(user)

        edge = self.mapper.connect(user, login, edge_model=LoggedIn)

        self.mapper.save(edge).send()

        return login

    def get_by_email(self, email):
        g = self.mapper.gremlin

        g.V().has('_label', 'user').has('email', email)

        return self.mapper.query(gremlin=g).first()
