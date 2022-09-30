# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_ses',
 'django_ses.management',
 'django_ses.management.commands',
 'django_ses.migrations']

package_data = \
{'': ['*'], 'django_ses': ['templates/django_ses/*']}

install_requires = \
['boto3>=1.0.0', 'django>=2.2', 'pytz>=2016.10']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1'],
 'bounce': ['cryptography>=36.0.2,<37.0.0', 'requests>=2.27.1,<3.0.0'],
 'events': ['cryptography>=36.0.2,<37.0.0', 'requests>=2.27.1,<3.0.0']}

setup_kwargs = {
    'name': 'django-ses',
    'version': '3.2.0',
    'description': "A Django email backend for Amazon's Simple Email Service",
    'long_description': '==========\nDjango-SES\n==========\n:Info: A Django email backend for Amazon\'s Simple Email Service\n:Author: Harry Marr (http://github.com/hmarr, http://twitter.com/harrymarr)\n:Collaborators: Paul Craciunoiu (http://github.com/pcraciunoiu, http://twitter.com/embrangler)\n\n|pypi| |build| |python| |django|\n\nA bird\'s eye view\n=================\nDjango-SES is a drop-in mail backend for Django_. Instead of sending emails\nthrough a traditional SMTP mail server, Django-SES routes email through\nAmazon Web Services\' excellent Simple Email Service (SES_).\n\n\nPlease Contribute!\n==================\nThis project is maintained, but not actively used by the maintainer. Interested\nin helping maintain this project? Reach out via GitHub Issues if you\'re actively\nusing `django-ses` and would be interested in contributing to it.\n\n\nChangelog\n=========\n\nFor details about each release, see the GitHub releases page: https://github.com/django-ses/django-ses/releases or CHANGES.md.\n\n\nUsing Django directly\n=====================\n\nAmazon SES allows you to also setup usernames and passwords. If you do configure\nthings that way, you do not need this package. The Django default email backend\nis capable of authenticating with Amazon SES and correctly sending email.\n\nUsing django-ses gives you additional features like deliverability reports that\ncan be hard and/or cumbersome to obtain when using the SMTP interface.\n\n\nWhy SES instead of SMTP?\n========================\nConfiguring, maintaining, and dealing with some complicated edge cases can be\ntime-consuming. Sending emails with Django-SES might be attractive to you if:\n\n* You don\'t want to maintain mail servers.\n* You are already deployed on EC2 (In-bound traffic to SES is free from EC2\n  instances).\n* You need to send a high volume of email.\n* You don\'t want to have to worry about PTR records, Reverse DNS, email\n  whitelist/blacklist services.\n* You want to improve delivery rate and inbox cosmetics by DKIM signing\n  your messages using SES\'s Easy DKIM feature.\n* Django-SES is a truely drop-in replacement for the default mail backend.\n  Your code should require no changes.\n\nGetting going\n=============\nAssuming you\'ve got Django_ installed, you\'ll just need to install django-ses::\n\n    pip install django-ses\n\n\nTo receive bounces or webhook events install the events "extra"::\n\n    pip install django-ses[events]\n\nAdd the following to your settings.py::\n\n    EMAIL_BACKEND = \'django_ses.SESBackend\'\n\n    # These are optional -- if they\'re set as environment variables they won\'t\n    # need to be set here as well\n    AWS_ACCESS_KEY_ID = \'YOUR-ACCESS-KEY-ID\'\n    AWS_SECRET_ACCESS_KEY = \'YOUR-SECRET-ACCESS-KEY\'\n\n    # Additionally, if you are not using the default AWS region of us-east-1,\n    # you need to specify a region, like so:\n    AWS_SES_REGION_NAME = \'us-west-2\'\n    AWS_SES_REGION_ENDPOINT = \'email.us-west-2.amazonaws.com\'\n\nAlternatively, instead of `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`, you\ncan include the following two settings values. This is useful in situations\nwhere you would like to use a separate access key to send emails via SES than\nyou would to upload files via S3::\n\n    AWS_SES_ACCESS_KEY_ID = \'YOUR-ACCESS-KEY-ID\'\n    AWS_SES_SECRET_ACCESS_KEY = \'YOUR-SECRET-ACCESS-KEY\'\n\nNow, when you use ``django.core.mail.send_mail``, Simple Email Service will\nsend the messages by default.\n\nSince SES imposes a rate limit and will reject emails after the limit has been\nreached, django-ses will attempt to conform to the rate limit by querying the\nAPI for your current limit and then sending no more than that number of\nmessages in a two-second period (which is half of the rate limit, just to\nbe sure to stay clear of the limit). This is controlled by the following setting:\n\n    AWS_SES_AUTO_THROTTLE = 0.5 # (default; safety factor applied to rate limit)\n\nTo turn off automatic throttling, set this to None.\n\nCheck out the ``example`` directory for more information.\n\nMonitoring email status using Amazon Simple Notification Service (Amazon SNS)\n=============================================================================\nTo set this up, install `django-ses` with the `events` extra::\n\n    pip install django-ses[events]\n\nThen add a event url handler in your `urls.py`::\n\n    from django_ses.views import SESEventWebhookView\n    from django.views.decorators.csrf import csrf_exempt\n    urlpatterns = [ ...\n                    url(r\'^ses/event-webhook/$\', SESEventWebhookView.as_view(), name=\'handle-event-webhook\'),\n                    ...\n    ]\n\nSESEventWebhookView handles bounce, complaint, send, delivery, open and click events.\nIt is also capable of auto confirming subscriptions, it handles `SubscriptionConfirmation` notification.\n\nOn AWS\n-------\n1. Add an SNS topic.\n\n2. In SES setup an SNS destination in "Configuration Sets". Use this\nconfiguration set by setting ``AWS_SES_CONFIGURATION_SET``. Set the topic\nto what you created in 1.\n\n3. Add an https subscriber to the topic. (eg. https://www.yourdomain.com/ses/event-webhook/)\nDo not check "Enable raw message delivery".\n\n\nBounces\n-------\nUsing signal \'bounce_received\' for manager bounce email. For example::\n\n    from django_ses.signals import bounce_received\n    from django.dispatch import receiver\n\n\n    @receiver(bounce_received)\n    def bounce_handler(sender, mail_obj, bounce_obj, raw_message, *args, **kwargs):\n        # you can then use the message ID and/or recipient_list(email address) to identify any problematic email messages that you have sent\n        message_id = mail_obj[\'messageId\']\n        recipient_list = mail_obj[\'destination\']\n        ...\n        print("This is bounce email object")\n        print(mail_obj)\n\nComplaint\n---------\nUsing signal \'complaint_received\' for manager complaint email. For example::\n\n    from django_ses.signals import complaint_received\n    from django.dispatch import receiver\n\n\n    @receiver(complaint_received)\n    def complaint_handler(sender, mail_obj, complaint_obj, raw_message,  *args, **kwargs):\n        ...\n\nSend\n----\nUsing signal \'send_received\' for manager send email. For example::\n\n    from django_ses.signals import send_received\n    from django.dispatch import receiver\n\n\n    @receiver(send_received)\n    def send_handler(sender, mail_obj, raw_message,  *args, **kwargs):\n        ...\n\nDelivery\n--------\nUsing signal \'delivery_received\' for manager delivery email. For example::\n\n    from django_ses.signals import delivery_received\n    from django.dispatch import receiver\n\n\n    @receiver(delivery_received)\n    def delivery_handler(sender, mail_obj, delivery_obj, raw_message,  *args, **kwargs):\n        ...\n\nOpen\n----\nUsing signal \'open_received\' for manager open email. For example::\n\n    from django_ses.signals import open_received\n    from django.dispatch import receiver\n\n\n    @receiver(open_received)\n    def open_handler(sender, mail_obj, raw_message, *args, **kwargs):\n        ...\n\nClick\n-----\nUsing signal \'click_received\' for manager send email. For example::\n\n    from django_ses.signals import click_received\n    from django.dispatch import receiver\n\n\n    @receiver(click_received)\n    def click_handler(sender, mail_obj, raw_message, *args, **kwargs):\n        ...\n        \nTesting Signals\n===============\n\nIf you would like to test your signals, you can optionally disable `AWS_SES_VERIFY_EVENT_SIGNATURES` in settings. Examples for the JSON object AWS SNS sends can be found here: https://docs.aws.amazon.com/sns/latest/dg/sns-message-and-json-formats.html#http-subscription-confirmation-json\n\nSES Event Monitoring with Configuration Sets\n============================================\n\nYou can track your SES email sending at a granular level using `SES Event Publishing`_.\nTo do this, you set up an SES Configuration Set and add event\nhandlers to it to send your events on to a destination within AWS (SNS,\nCloudwatch or Kinesis Firehose) for further processing and analysis.\n\nTo ensure that emails you send via `django-ses` will be tagged with your\nSES Configuration Set, set the `AWS_SES_CONFIGURATION_SET` setting in your\nsettings.py to the name of the configuration set::\n\n    AWS_SES_CONFIGURATION_SET = \'my-configuration-set-name\'\n\nThis will add the `X-SES-CONFIGURATION-SET` header to all your outgoing\ne-mails.\n\nIf you want to set the SES Configuration Set on a per message basis, set\n`AWS_SES_CONFIGURATION_SET` to a callable.  The callable should conform to the\nfollowing prototype::\n\n    def ses_configuration_set(message, dkim_domain=None, dkim_key=None,\n                                dkim_selector=None, dkim_headers=()):\n        configuration_set = \'my-default-set\'\n        # use message and dkim_* to modify configuration_set\n        return configuration_set\n\n    AWS_SES_CONFIGURATION_SET = ses_configuration_set\n\nwhere\n\n* `message` is a `django.core.mail.EmailMessage` object (or subclass)\n* `dkim_domain` is a string containing the DKIM domain for this message\n* `dkim_key` is a string containing the DKIM private key for this message\n* `dkim_selector` is a string containing the DKIM selector (see DKIM, below for\n  explanation)\n* `dkim_headers` is a list of strings containing the names of the headers to\n  be DKIM signed (see DKIM, below for explanation)\n\nDKIM\n====\n\nUsing DomainKeys_ is entirely optional, however it is recommended by Amazon for\nauthenticating your email address and improving delivery success rate.  See\nhttp://docs.amazonwebservices.com/ses/latest/DeveloperGuide/DKIM.html.\nBesides authentication, you might also want to consider using DKIM in order to\nremove the `via email-bounces.amazonses.com` message shown to gmail users -\nsee http://support.google.com/mail/bin/answer.py?hl=en&answer=1311182.\n\nCurrently there are two methods to use DKIM with Django-SES: traditional Manual\nSigning and the more recently introduced Amazon Easy DKIM feature.\n\nEasy DKIM\n---------\nEasy DKIM is a feature of Amazon SES that automatically signs every message\nthat you send from a verified email address or domain with a DKIM signature.\n\nYou can enable Easy DKIM in the AWS Management Console for SES. There you can\nalso add the required domain verification and DKIM records to Route 53 (or\ncopy them to your alternate DNS).\n\nOnce enabled and verified Easy DKIM needs no additional dependencies or\nDKIM specific settings to work with Django-SES.\n\nFor more information and a setup guide see:\nhttp://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\n\nManual DKIM Signing\n-------------------\nTo enable Manual DKIM Signing you should install the pydkim_ package and specify values\nfor the ``DKIM_PRIVATE_KEY`` and ``DKIM_DOMAIN`` settings.  You can generate a\nprivate key with a command such as ``openssl genrsa 512`` and get the public key\nportion with ``openssl rsa -pubout <private.key``.  The public key should be\npublished to ``ses._domainkey.example.com`` if your domain is example.com.  You\ncan use a different name instead of ``ses`` by changing the ``DKIM_SELECTOR``\nsetting.\n\nThe SES relay will modify email headers such as `Date` and `Message-Id` so by\ndefault only the `From`, `To`, `Cc`, `Subject` headers are signed, not the full\nset of headers.  This is sufficient for most DKIM validators but can be overridden\nwith the ``DKIM_HEADERS`` setting.\n\n\nExample settings.py::\n\n   DKIM_DOMAIN = \'example.com\'\n   DKIM_PRIVATE_KEY = \'\'\'\n   -----BEGIN RSA PRIVATE KEY-----\n   xxxxxxxxxxx\n   -----END RSA PRIVATE KEY-----\n   \'\'\'\n\nExample DNS record published to Route53 with boto:\n\n   route53 add_record ZONEID ses._domainkey.example.com. TXT \'"v=DKIM1; p=xxx"\' 86400\n\n\n.. _DomainKeys: http://dkim.org/\n\n\nIdentity Owners\n===============\n\nWith Identity owners, you can use validated SES-domains across multiple accounts:\nhttps://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html\n\nThis is useful if you got multiple environments in different accounts and still want to send mails via the same domain.\n\nYou can configure the following environment variables to use them as described in boto3-docs_::\n\n    AWS_SES_SOURCE_ARN=arn:aws:ses:eu-central-1:012345678910:identity/example.com\n    AWS_SES_FROM_ARN=arn:aws:ses:eu-central-1:012345678910:identity/example.com\n    AWS_SES_RETURN_PATH_ARN=arn:aws:ses:eu-central-1:012345678910:identity/example.com\n\n.. _boto3-docs: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_raw_email\n\n\nSES Sending Stats\n=================\n\nDjango SES comes with two ways of viewing sending statistics.\n\nThe first one is a simple read-only report on your 24 hour sending quota,\nverified email addresses and bi-weekly sending statistics.\n\nTo generate and view SES sending statistics reports, include, update\n``INSTALLED_APPS``::\n\n    INSTALLED_APPS = (\n        # ...\n        \'django.contrib.admin\',\n        \'django_ses\',\n        # ...\n    )\n\n... and ``urls.py``::\n\n    urlpatterns += (url(r\'^admin/django-ses/\', include(\'django_ses.urls\')),)\n\n*Optional enhancements to stats:*\n\nOverride the dashboard view\n---------------------------\nYou can override the Dashboard view, for example, to add more context data::\n\n    class CustomSESDashboardView(DashboardView):\n        def get_context_data(self, **kwargs):\n            context = super().get_context_data(**kwargs)\n            context.update(**admin.site.each_context(self.request))\n            return context\n\nThen update your urls::\n\n    urlpatterns += path(\'admin/django-ses/\', CustomSESDashboardView.as_view(), name=\'django_ses_stats\'),\n\n\nLink the dashboard from the admin\n---------------------------------\nYou can use adminplus for this (https://github.com/jsocol/django-adminplus)::\n\n    from django_ses.views import DashboardView\n    admin.site.register_view(\'django-ses\', DashboardView.as_view(), \'Django SES Stats\')\n\n\n\nStore daily stats\n-----------------\nIf you need to keep send statistics around for longer than two weeks,\ndjango-ses also comes with a model that lets you store these. To use this\nfeature you\'ll need to run::\n\n    python manage.py migrate\n\nTo collect the statistics, run the ``get_ses_statistics`` management command\n(refer to next section for details). After running this command the statistics\nwill be viewable via ``/admin/django_ses/``.\n\nDjango SES Management Commands\n==============================\n\nTo use these you must include ``django_ses`` in your INSTALLED_APPS.\n\nManaging Verified Email Addresses\n---------------------------------\n\nManage verified email addresses through the management command.\n\n    python manage.py ses_email_address --list\n\nAdd emails to the verified email list through:\n\n    python manage.py ses_email_address --add john.doe@example.com\n\nRemove emails from the verified email list through:\n\n    python manage.py ses_email_address --delete john.doe@example.com\n\nYou can toggle the console output through setting the verbosity level.\n\n    python manage.py ses_email_address --list --verbosity 0\n\n\nCollecting Sending Statistics\n-----------------------------\n\nTo collect and store SES sending statistics in the database, run:\n\n    python manage.py get_ses_statistics\n\nSending statistics are aggregated daily (UTC time). Stats for the latest day\n(when you run the command) may be inaccurate if run before end of day (UTC).\nIf you want to keep your statistics up to date, setup ``cron`` to run this\ncommand a short time after midnight (UTC) daily.\n\n\nDjango Builtin-in Error Emails\n==============================\n\nIf you\'d like Django\'s `Builtin Email Error Reporting`_ to function properly\n(actually send working emails), you\'ll have to explicitly set the\n``SERVER_EMAIL`` setting to one of your SES-verified addresses. Otherwise, your\nerror emails will all fail and you\'ll be blissfully unaware of a problem.\n\n*Note:* You will need to sign up for SES_ and verify any emails you\'re going\nto use in the `from_email` argument to `django.core.mail.send_email()`. Boto_\nhas a `verify_email_address()` method: https://github.com/boto/boto/blob/master/boto/ses/connection.py\n\n.. _Builtin Email Error Reporting: https://docs.djangoproject.com/en/dev/howto/error-reporting/\n.. _Django: http://djangoproject.com\n.. _Boto: http://boto.cloudhackers.com/\n.. _SES: http://aws.amazon.com/ses/\n.. _SES Event Publishing: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-using-event-publishing.html\n\n\nRequirements\n============\ndjango-ses requires supported version of Django or Python.\n\n\nFull List of Settings\n=====================\n\n``AWS_ACCESS_KEY_ID``, ``AWS_SECRET_ACCESS_KEY``\n  *Required.* Your API keys for Amazon SES.\n\n``AWS_SES_ACCESS_KEY_ID``, ``AWS_SES_SECRET_ACCESS_KEY``\n  *Required.* Alternative API keys for Amazon SES. This is useful in situations\n  where you would like to use separate access keys for different AWS services.\n\n``AWS_SES_SESSION_TOKEN``, ``AWS_SES_SECRET_ACCESS_KEY``\n  Optional. Use `AWS_SES_SESSION_TOKEN` to provide session token\n  when temporary credentials are used. Details:\n  https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html\n  https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html\n\n``AWS_SES_REGION_NAME``, ``AWS_SES_REGION_ENDPOINT``\n  Optionally specify what region your SES service is using. Note that this is\n  required if your SES service is not using us-east-1, as omitting these settings\n  implies this region. Details:\n  http://readthedocs.org/docs/boto/en/latest/ref/ses.html#boto.ses.regions\n  http://docs.aws.amazon.com/general/latest/gr/rande.html\n\n``AWS_SES_RETURN_PATH``\n  Instruct Amazon SES to forward bounced emails and complaints to this email.\n  For more information please refer to http://aws.amazon.com/ses/faqs/#38\n\n``AWS_SES_CONFIGURATION_SET``\n  Optional. Use this to mark your e-mails as from being from a particular SES\n  Configuration Set. Set this to a string if you want all messages to have the\n  same configuration set.  Set this to a callable if you want to set\n  configuration set on a per message basis.\n\n``TIME_ZONE``\n  Default Django setting, optionally set this. Details:\n  https://docs.djangoproject.com/en/dev/ref/settings/#time-zone\n\n``DKIM_DOMAIN``, ``DKIM_PRIVATE_KEY``\n  Optional. If these settings are defined and the pydkim_ module is installed\n  then email messages will be signed with the specified key.   You will also\n  need to publish your public key on DNS; the selector is set to ``ses`` by\n  default.  See http://dkim.org/ for further detail.\n\n``AWS_SES_SOURCE_ARN``\n  Instruct Amazon SES to use a domain from another account.\n  For more information please refer to https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html\n\n``AWS_SES_FROM_ARN``\n  Instruct Amazon SES to use a domain from another account.\n  For more information please refer to https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html\n\n``AWS_SES_RETURN_PATH_ARN``\n  Instruct Amazon SES to use a domain from another account.\n  For more information please refer to https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization-delegate-sender-tasks-email.html\n\n``AWS_SES_VERIFY_EVENT_SIGNATURES``, ``AWS_SES_VERIFY_BOUNCE_SIGNATURES``\n  Optional. Default is True. Verify the contents of the message by matching the signature\n  you recreated from the message contents with the signature that Amazon SNS sent with the message.\n  See https://docs.aws.amazon.com/sns/latest/dg/sns-verify-signature-of-message.html for further detail.\n\n``EVENT_CERT_DOMAINS``, ``BOUNCE_CERT_DOMAINS``\n  Optional. Default is \'amazonaws.com\' and \'amazon.com\'.\n\n.. _pydkim: http://hewgill.com/pydkim/\n\nProxy\n=====\n\nIf you are using a proxy, please enable it via the env variables.\n\nIf your proxy server does not have a password try the following:\n\n.. code-block:: python\n\n   import os\n   os.environ["HTTP_PROXY"] = "http://proxy.com:port"\n   os.environ["HTTPS_PROXY"] = "https://proxy.com:port"\n\nif your proxy server has a password try the following:\n\n.. code-block:: python\n\n   import os\n   os.environ["HTTP_PROXY"] = "http://user:password@proxy.com:port"\n   os.environ["HTTPS_PROXY"] = "https://user:password@proxy.com:port"\n\nSource: https://stackoverflow.com/a/33501223/1331671\n\nContributing\n============\nIf you\'d like to fix a bug, add a feature, etc\n\n#. Start by opening an issue.\n    Be explicit so that project collaborators can understand and reproduce the\n    issue, or decide whether the feature falls within the project\'s goals.\n    Code examples can be useful, too.\n\n#. File a pull request.\n    You may write a prototype or suggested fix.\n\n#. Check your code for errors, complaints.\n    Use `check.py <https://github.com/jbalogh/check>`_\n\n#. Write and run tests.\n    Write your own test showing the issue has been resolved, or the feature\n    works as intended.\n\nRunning Tests\n=============\nTo run the tests::\n\n    python runtests.py\n\nIf you want to debug the tests, just add this file as a python script to your IDE run configuration.\n\nCreating a Release\n==================\n\nTo create a release:\n\n* Run ``poetry version {patch|minor|major}`` as explained in `the docs <https://python-poetry.org/docs/cli/#version>`_. This will update the version in pyproject.toml.\n* Commit that change and use git to tag that commit with a version that matches the pattern ``v*.*.*``.\n* Push the tag and the commit (note some IDEs don\'t push tags by default).\n\n\n.. |pypi| image:: https://badge.fury.io/py/django-ses.svg\n    :target: http://badge.fury.io/py/django-ses\n.. |build| image:: https://github.com/django-ses/django-ses/actions/workflows/ci.yml/badge.svg\n    :target: https://github.com/django-ses/django-ses/actions/workflows/ci.yml\n.. |python| image:: https://img.shields.io/badge/python-3.7+-blue.svg\n    :target: https://pypi.org/project/django-ses/\n.. |django| image:: https://img.shields.io/badge/django-2.2%7C%203.2+-blue.svg\n    :target: https://www.djangoproject.com/\n',
    'author': 'Harry Marr',
    'author_email': 'harry@hmarr.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/django-ses/django-ses',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
