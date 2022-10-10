from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext as _


@deconstructible
class ValueStartsWithValidator(BaseValidator):
    code = 'starts_with'
    message = _('Ensure this value starts with %(limit_value)s, it starts with %(show_value)s.')

    def compare(self, value, correct_value):
        # shaqayegh: true output raise exception
        return value != correct_value

    def clean(self, x):
        return x[0]
