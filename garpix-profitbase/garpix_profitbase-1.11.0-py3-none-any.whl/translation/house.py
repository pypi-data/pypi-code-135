from modeltranslation.translator import TranslationOptions, register
from ..models import House


@register(House)
class HouseTranslationOptions(TranslationOptions):
    pass
