from django.contrib.auth import get_user_model
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext as _
from rolepermissions.checkers import has_role

User = get_user_model()


@deconstructible
class PhoneNumberUserExistenceValidator(BaseValidator):
    code = 'phone_number_user_not_exist'
    message = _('User with %(show_value)s was not found.')

    def compare(self, value, correct_value):
        user = User.objects.filter(phone_number=value, is_active=True)
        if user.exists():
            user = user.first()
            if correct_value is None:
                return False
            else:
                user_has_role = has_role(user, [correct_value])
                if user_has_role:
                    return False
                return True
        return True
