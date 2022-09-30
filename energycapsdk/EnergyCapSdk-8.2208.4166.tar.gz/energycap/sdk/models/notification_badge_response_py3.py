# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NotificationBadgeResponse(Model):
    """NotificationBadgeResponse.

    :param total_notifications: Total of unread and unarchived notifications
    :type total_notifications: int
    :param new_notifications: Total of unread and unarchived notifications
     since the last checked date time
    :type new_notifications: int
    :param last_check_date_time_utc: The date and time in UTC the query to get
     the badge data was run
    :type last_check_date_time_utc: datetime
    """

    _attribute_map = {
        'total_notifications': {'key': 'totalNotifications', 'type': 'int'},
        'new_notifications': {'key': 'newNotifications', 'type': 'int'},
        'last_check_date_time_utc': {'key': 'lastCheckDateTimeUtc', 'type': 'iso-8601'},
    }

    def __init__(self, *, total_notifications: int=None, new_notifications: int=None, last_check_date_time_utc=None, **kwargs) -> None:
        super(NotificationBadgeResponse, self).__init__(**kwargs)
        self.total_notifications = total_notifications
        self.new_notifications = new_notifications
        self.last_check_date_time_utc = last_check_date_time_utc
