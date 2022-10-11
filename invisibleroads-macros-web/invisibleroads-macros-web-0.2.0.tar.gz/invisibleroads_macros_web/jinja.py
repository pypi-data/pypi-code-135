from os.path import dirname, getmtime, join, normpath

from jinja2 import BaseLoader, Environment, TemplateNotFound, pass_context


class RelativeTemplateEnvironment(Environment):

    def join_path(self, template, parent):
        'Support relative template paths via extends, import, include'
        return normpath(join(dirname(parent), template))


class TemplatePathLoader(BaseLoader):

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def get_source(self, environment, template):
        'Support absolute template paths'
        try:
            modification_time = getmtime(template)
        except OSError:
            raise TemplateNotFound(template)

        def is_latest():
            try:
                return modification_time == getmtime(template)
            except OSError:
                return False

        with open(template, encoding=self.encoding) as f:
            text = f.read()
        return text, template.resolve(), is_latest


@pass_context
def url_for(context, name, **d):
    return context['request'].url_for(name, **d)
