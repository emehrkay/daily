from tornado.options import options



class TagMixin(object):

    def add_tag(self, entity, tag):
        pass

    def add_tags(self, entity, tags):
        for tag in tags:
            self.add_tag(entity, tags)

    def get_tags(self, entity):
        return []

