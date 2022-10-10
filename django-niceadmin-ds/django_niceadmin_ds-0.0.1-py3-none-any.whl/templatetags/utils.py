from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

# 템플릿에서 문자열을 split하기 위해 커스텀 필터를 만듦 - 현재까지는 medicio템플릿에서 사용함.


@register.filter
@stringfilter
def replace_space(string: str):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.replace("_", " ")

