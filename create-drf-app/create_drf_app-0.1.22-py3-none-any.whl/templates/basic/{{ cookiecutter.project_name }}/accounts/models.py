"""
"""
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager
from '{{ cookiecutter.project_name }}.models' import TimeStampedModelMixin


class Account(AbstractBaseUser, PermissionsMixin, TimeStampedModelMixin):
    """
    User class implementing a fully featured Account model with
    admin-compliant permissions.
    Username and password are required. Other fields are optional.
    """

    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(
        _('email address'),
        unique=True,
        help_text=_('Required.'),
        error_messages={
            'unique': _("An account with that email already exists."),
        },
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the account can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this account should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    # photo = models.ImageField(_('user photo'), upload_to='user_photo', blank=True, null=True)
    # gender = models.CharField(_('gender'), max_length=32, blank=True, null=True)
    # phone_number = models.CharField(_('phone number'), max_length=32, blank=True, null=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the accout."""
        return self.first_name

    def email_account(self, subject, message, from_email=None, **kwargs):
        """Send an email to this account."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
