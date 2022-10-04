
class GObject(object):

    def __init__(self, class_name='GenericObj', **kwargs):
        self.class_name = class_name
        self.kwargs = kwargs

    def all(self):
        return list(self.kwargs.keys())

    def __repr__(self):
        return f"<class '{self.class_name}'>"

    def __getattr__(self, item):
        return self.kwargs[item]

    def __getitem__(self, item):
        return self.kwargs[item]

    def get(self, item, default=None):
        return self.kwargs.get(item, default)

    def to_dict(self):
        return self.kwargs
