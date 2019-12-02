# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.mqtt import MQTT  # noqa: F401,E501
from swagger_server import util


class SourceESS(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, mqtt: MQTT=None):  # noqa: E501
        """SourceESS - a model defined in Swagger

        :param mqtt: The mqtt of this SourceESS.  # noqa: E501
        :type mqtt: MQTT
        """
        self.swagger_types = {
            'mqtt': MQTT
        }

        self.attribute_map = {
            'mqtt': 'mqtt'
        }

        self._mqtt = mqtt

    @classmethod
    def from_dict(cls, dikt) -> 'SourceESS':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SourceESS of this SourceESS.  # noqa: E501
        :rtype: SourceESS
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mqtt(self) -> MQTT:
        """Gets the mqtt of this SourceESS.


        :return: The mqtt of this SourceESS.
        :rtype: MQTT
        """
        return self._mqtt

    @mqtt.setter
    def mqtt(self, mqtt: MQTT):
        """Sets the mqtt of this SourceESS.


        :param mqtt: The mqtt of this SourceESS.
        :type mqtt: MQTT
        """

        self._mqtt = mqtt