# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NotificationDetailsResponse(Model):
    """NotificationDetailsResponse.

    :param message: The full notification message
    :type message: str
    :param created_by_user:
    :type created_by_user: ~energycap.sdk.models.UserChild
    :param primary_action:
    :type primary_action:
     ~energycap.sdk.models.NotificationActionButtonResponse
    :param secondary_action:
    :type secondary_action:
     ~energycap.sdk.models.NotificationActionButtonResponse
    :param notification_id: The id of the notification
    :type notification_id: long
    :param read: True if the notification has been read
    :type read: bool
    :param archived: True if the notification has been archived
    :type archived: bool
    :param subject: Subject of the notification
    :type subject: str
    :param created_date: The date and time the notification was generated
    :type created_date: datetime
    :param notification_type:
    :type notification_type: ~energycap.sdk.models.NotificationType
    """

    _attribute_map = {
        'message': {'key': 'message', 'type': 'str'},
        'created_by_user': {'key': 'createdByUser', 'type': 'UserChild'},
        'primary_action': {'key': 'primaryAction', 'type': 'NotificationActionButtonResponse'},
        'secondary_action': {'key': 'secondaryAction', 'type': 'NotificationActionButtonResponse'},
        'notification_id': {'key': 'notificationId', 'type': 'long'},
        'read': {'key': 'read', 'type': 'bool'},
        'archived': {'key': 'archived', 'type': 'bool'},
        'subject': {'key': 'subject', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'notification_type': {'key': 'notificationType', 'type': 'NotificationType'},
    }

    def __init__(self, **kwargs):
        super(NotificationDetailsResponse, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)
        self.created_by_user = kwargs.get('created_by_user', None)
        self.primary_action = kwargs.get('primary_action', None)
        self.secondary_action = kwargs.get('secondary_action', None)
        self.notification_id = kwargs.get('notification_id', None)
        self.read = kwargs.get('read', None)
        self.archived = kwargs.get('archived', None)
        self.subject = kwargs.get('subject', None)
        self.created_date = kwargs.get('created_date', None)
        self.notification_type = kwargs.get('notification_type', None)
