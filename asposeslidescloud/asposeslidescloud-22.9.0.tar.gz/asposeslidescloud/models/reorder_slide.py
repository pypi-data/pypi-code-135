# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose">
#   Copyright (c) 2018 Aspose.Slides for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

import pprint
import re  # noqa: F401

import six

from asposeslidescloud.models.task import Task

class ReorderSlide(Task):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'old_position': 'int',
        'new_position': 'int'
    }

    attribute_map = {
        'type': 'type',
        'old_position': 'oldPosition',
        'new_position': 'newPosition'
    }

    type_determiners = {
        'type': 'ReoderSlide',
    }

    def __init__(self, type='ReoderSlide', old_position=None, new_position=None):  # noqa: E501
        """ReorderSlide - a model defined in Swagger"""  # noqa: E501
        super(ReorderSlide, self).__init__(type)

        self._old_position = None
        self._new_position = None
        self.type = 'ReoderSlide'

        self.old_position = old_position
        self.new_position = new_position

    @property
    def old_position(self):
        """Gets the old_position of this ReorderSlide.  # noqa: E501

        Old position.  # noqa: E501

        :return: The old_position of this ReorderSlide.  # noqa: E501
        :rtype: int
        """
        return self._old_position

    @old_position.setter
    def old_position(self, old_position):
        """Sets the old_position of this ReorderSlide.

        Old position.  # noqa: E501

        :param old_position: The old_position of this ReorderSlide.  # noqa: E501
        :type: int
        """
        self._old_position = old_position

    @property
    def new_position(self):
        """Gets the new_position of this ReorderSlide.  # noqa: E501

        New position.  # noqa: E501

        :return: The new_position of this ReorderSlide.  # noqa: E501
        :rtype: int
        """
        return self._new_position

    @new_position.setter
    def new_position(self, new_position):
        """Sets the new_position of this ReorderSlide.

        New position.  # noqa: E501

        :param new_position: The new_position of this ReorderSlide.  # noqa: E501
        :type: int
        """
        self._new_position = new_position

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReorderSlide):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
