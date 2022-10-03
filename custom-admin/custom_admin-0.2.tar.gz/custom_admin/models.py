import inspect
import logging
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db import models
from django.template.loader import get_template
from django.utils.safestring import mark_safe

from custom_admin.inlines import AdminInlineQueryset

logger = logging.getLogger(__name__)


class EmailReport(models.Model):
    enabled = models.BooleanField(default=True)
    report_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.report_name if self.report_name is not None else "Email Report {}".format(self.pk)

    @classmethod
    def get_or_create(cls, report_name):
        try:
            return cls.objects.get(report_name=report_name)
        except cls.DoesNotExist:
            return cls.objects.create(report_name=report_name)

    @property
    def recipients(self):
        return EmailRecipient.objects.filter(
            pk__in=[r.pk for r in EmailRecipient.objects.filter(enabled=True) if self in r.reports.all()]
        )

    def send(self, subject, template_path, context_dict, **kwargs):
        if self.enabled:
            to_list = list(set(self.recipients.values_list("email", flat=True)))

            # Plaintext file with template tags in it
            message = get_template(template_path).render(context_dict)

            return send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL if kwargs.get("from", None) is None else kwargs.get("from"),
                to_list,
                fail_silently=False,
            )

        return False

    @property
    def recipients_inline(self):
        inline = AdminInlineQueryset(self.recipients, fields=["email", "enabled"])
        return inline.html


class EmailRecipient(models.Model):
    enabled = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    reports = models.ManyToManyField(EmailReport)

    def __str__(self):
        return self.email if self.email is not None else "Email Recipient {}".format(self.pk)


class ExceptionLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(get_user_model(), blank=True, null=True, on_delete=models.CASCADE)
    exception = models.TextField(blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    function_name = models.CharField(max_length=255, blank=True, null=True)
    line_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "Exception at {} for user {}".format(self.path, self.user, self.function_name)

    @classmethod
    def add(cls, request, exception, **kwargs):
        debug_filename = os.path.basename(inspect.stack()[1][1])
        debug_function_name = inspect.stack()[1][3]
        debug_line_number = inspect.stack()[1][2]

        try:
            ExceptionLog.objects.create(
                user=request.user,
                exception=exception,
                traceback=exception.__traceback__,
                message=kwargs.get("message", None),
                path=request.build_absolute_uri(),
                filename=debug_filename,
                function_name=debug_function_name,
                line_number=debug_line_number,
            )
        except Exception as e:
            logger.error("Error creating Exception Log: {} - For exception: {}".format(e, exception))

    @property
    def formatted_traceback(self):
        return mark_safe("<pre>{}</pre>".format(self.traceback))
