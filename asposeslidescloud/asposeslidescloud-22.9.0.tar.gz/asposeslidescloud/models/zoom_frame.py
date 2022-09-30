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

from asposeslidescloud.models.zoom_object import ZoomObject

class ZoomFrame(ZoomObject):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'self_uri': 'ResourceUri',
        'alternate_links': 'list[ResourceUri]',
        'name': 'str',
        'width': 'float',
        'height': 'float',
        'alternative_text': 'str',
        'alternative_text_title': 'str',
        'hidden': 'bool',
        'x': 'float',
        'y': 'float',
        'z_order_position': 'int',
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'three_d_format': 'ThreeDFormat',
        'line_format': 'LineFormat',
        'hyperlink_click': 'Hyperlink',
        'hyperlink_mouse_over': 'Hyperlink',
        'type': 'str',
        'image_type': 'str',
        'return_to_parent': 'bool',
        'show_background': 'bool',
        'image': 'ResourceUri',
        'transition_duration': 'float',
        'target_slide_index': 'int'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'name': 'name',
        'width': 'width',
        'height': 'height',
        'alternative_text': 'alternativeText',
        'alternative_text_title': 'alternativeTextTitle',
        'hidden': 'hidden',
        'x': 'x',
        'y': 'y',
        'z_order_position': 'zOrderPosition',
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'three_d_format': 'threeDFormat',
        'line_format': 'lineFormat',
        'hyperlink_click': 'hyperlinkClick',
        'hyperlink_mouse_over': 'hyperlinkMouseOver',
        'type': 'type',
        'image_type': 'imageType',
        'return_to_parent': 'returnToParent',
        'show_background': 'showBackground',
        'image': 'image',
        'transition_duration': 'transitionDuration',
        'target_slide_index': 'targetSlideIndex'
    }

    type_determiners = {
        'type': 'ZoomFrame',
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, width=None, height=None, alternative_text=None, alternative_text_title=None, hidden=None, x=None, y=None, z_order_position=None, fill_format=None, effect_format=None, three_d_format=None, line_format=None, hyperlink_click=None, hyperlink_mouse_over=None, type='ZoomFrame', image_type=None, return_to_parent=None, show_background=None, image=None, transition_duration=None, target_slide_index=None):  # noqa: E501
        """ZoomFrame - a model defined in Swagger"""  # noqa: E501
        super(ZoomFrame, self).__init__(self_uri, alternate_links, name, width, height, alternative_text, alternative_text_title, hidden, x, y, z_order_position, fill_format, effect_format, three_d_format, line_format, hyperlink_click, hyperlink_mouse_over, type, image_type, return_to_parent, show_background, image, transition_duration)

        self._target_slide_index = None
        self.type = 'ZoomFrame'

        if target_slide_index is not None:
            self.target_slide_index = target_slide_index

    @property
    def target_slide_index(self):
        """Gets the target_slide_index of this ZoomFrame.  # noqa: E501

        Links to the target slide  # noqa: E501

        :return: The target_slide_index of this ZoomFrame.  # noqa: E501
        :rtype: int
        """
        return self._target_slide_index

    @target_slide_index.setter
    def target_slide_index(self, target_slide_index):
        """Sets the target_slide_index of this ZoomFrame.

        Links to the target slide  # noqa: E501

        :param target_slide_index: The target_slide_index of this ZoomFrame.  # noqa: E501
        :type: int
        """
        self._target_slide_index = target_slide_index

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
        if not isinstance(other, ZoomFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
