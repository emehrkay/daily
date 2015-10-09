from tornado.options import options


class TagMixin(object):

    def add_tag(self, entity, tag):
        return self.mapper.connect(entity, tag, edge_model=HasTag)

    def add_tags(self, entity, tags):
        edges = []

        for tag in tags:
            edges.append(self.add_tag(entity, tags))

        return edges

    def get_tags(self, entity):
        trav = self.mapper.start(entity)
        trav.out('has_tag')

        return self.mapper.query(gremlin=trav).data
