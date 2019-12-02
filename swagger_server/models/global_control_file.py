# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meta_gloabl_control import MetaGloablControl  # noqa: F401,E501

from swagger_server import util


class GlobalControlFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, ess_control: List[float]=None, meta: MetaGloablControl=None):  # noqa: E501
        """GlobalControlFile - a model defined in Swagger

        :param ess_control: The ess_control of this GlobalControlFile.  # noqa: E501
        :type ess_control: List[float]
        :param meta: The meta of this GlobalControlFile.  # noqa: E501
        :type meta: MetaGloablControl
        """
        self.swagger_types = {
            'ess_control': List[float],
            'meta': MetaGloablControl
        }

        self.attribute_map = {
            'ess_control': 'ESS_Control',
            'meta': 'meta'
        }

        self._ess_control = ess_control
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'GlobalControlFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Global_Control_File of this GlobalControlFile.  # noqa: E501
        :rtype: GlobalControlFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ess_control(self) -> List[float]:
        """Gets the ess_control of this GlobalControlFile.


        :return: The ess_control of this GlobalControlFile.
        :rtype: List[float]
        """
        return self._ess_control

    @ess_control.setter
    def ess_control(self, ess_control: List[float]):
        """Sets the ess_control of this GlobalControlFile.


        :param ess_control: The ess_control of this GlobalControlFile.
        :type ess_control: List[float]
        """
        if ess_control is None:
            raise ValueError("Invalid value for `ess_control`, must not be `None`")  # noqa: E501

        self._ess_control = ess_control

    @property
    def meta(self) -> MetaGloablControl:
        """Gets the meta of this GlobalControlFile.


        :return: The meta of this GlobalControlFile.
        :rtype: MetaGloablControl
        """
        return self._meta

    @meta.setter
    def meta(self, meta: MetaGloablControl):
        """Sets the meta of this GlobalControlFile.


        :param meta: The meta of this GlobalControlFile.
        :type meta: MetaGloablControl
        """

        self._meta = meta