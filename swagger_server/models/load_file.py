# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.meta_load import MetaLoad  # noqa: F401,E501
from swagger_server import util


class LoadFile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, p_load: List[float]=None, p_load_r: List[float]=None, p_load_s: List[float]=None, p_load_t: List[float]=None, q_load: List[float]=None, q_load_r: List[float]=None, q_load_s: List[float]=None, q_load_t: List[float]=None, meta: MetaLoad=None):  # noqa: E501
        """LoadFile - a model defined in Swagger

        :param p_load: The p_load of this LoadFile.  # noqa: E501
        :type p_load: List[float]
        :param p_load_r: The p_load_r of this LoadFile.  # noqa: E501
        :type p_load_r: List[float]
        :param p_load_s: The p_load_s of this LoadFile.  # noqa: E501
        :type p_load_s: List[float]
        :param p_load_t: The p_load_t of this LoadFile.  # noqa: E501
        :type p_load_t: List[float]
        :param q_load: The q_load of this LoadFile.  # noqa: E501
        :type q_load: List[float]
        :param q_load_r: The q_load_r of this LoadFile.  # noqa: E501
        :type q_load_r: List[float]
        :param q_load_s: The q_load_s of this LoadFile.  # noqa: E501
        :type q_load_s: List[float]
        :param q_load_t: The q_load_t of this LoadFile.  # noqa: E501
        :type q_load_t: List[float]
        :param meta: The meta of this LoadFile.  # noqa: E501
        :type meta: MetaLoad
        """
        self.swagger_types = {
            'p_load': List[float],
            'p_load_r': List[float],
            'p_load_s': List[float],
            'p_load_t': List[float],
            'q_load': List[float],
            'q_load_r': List[float],
            'q_load_s': List[float],
            'q_load_t': List[float],
            'meta': MetaLoad
        }

        self.attribute_map = {
            'p_load': 'P_Load',
            'p_load_r': 'P_Load_R',
            'p_load_s': 'P_Load_S',
            'p_load_t': 'P_Load_T',
            'q_load': 'Q_Load',
            'q_load_r': 'Q_Load_R',
            'q_load_s': 'Q_Load_S',
            'q_load_t': 'Q_Load_T',
            'meta': 'meta'
        }

        self._p_load = p_load
        self._p_load_r = p_load_r
        self._p_load_s = p_load_s
        self._p_load_t = p_load_t
        self._q_load = q_load
        self._q_load_r = q_load_r
        self._q_load_s = q_load_s
        self._q_load_t = q_load_t
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'LoadFile':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Load_File of this LoadFile.  # noqa: E501
        :rtype: LoadFile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def p_load(self) -> List[float]:
        """Gets the p_load of this LoadFile.


        :return: The p_load of this LoadFile.
        :rtype: List[float]
        """
        return self._p_load

    @p_load.setter
    def p_load(self, p_load: List[float]):
        """Sets the p_load of this LoadFile.


        :param p_load: The p_load of this LoadFile.
        :type p_load: List[float]
        """

        self._p_load = p_load

    @property
    def p_load_r(self) -> List[float]:
        """Gets the p_load_r of this LoadFile.


        :return: The p_load_r of this LoadFile.
        :rtype: List[float]
        """
        return self._p_load_r

    @p_load_r.setter
    def p_load_r(self, p_load_r: List[float]):
        """Sets the p_load_r of this LoadFile.


        :param p_load_r: The p_load_r of this LoadFile.
        :type p_load_r: List[float]
        """

        self._p_load_r = p_load_r

    @property
    def p_load_s(self) -> List[float]:
        """Gets the p_load_s of this LoadFile.


        :return: The p_load_s of this LoadFile.
        :rtype: List[float]
        """
        return self._p_load_s

    @p_load_s.setter
    def p_load_s(self, p_load_s: List[float]):
        """Sets the p_load_s of this LoadFile.


        :param p_load_s: The p_load_s of this LoadFile.
        :type p_load_s: List[float]
        """

        self._p_load_s = p_load_s

    @property
    def p_load_t(self) -> List[float]:
        """Gets the p_load_t of this LoadFile.


        :return: The p_load_t of this LoadFile.
        :rtype: List[float]
        """
        return self._p_load_t

    @p_load_t.setter
    def p_load_t(self, p_load_t: List[float]):
        """Sets the p_load_t of this LoadFile.


        :param p_load_t: The p_load_t of this LoadFile.
        :type p_load_t: List[float]
        """

        self._p_load_t = p_load_t

    @property
    def q_load(self) -> List[float]:
        """Gets the q_load of this LoadFile.


        :return: The q_load of this LoadFile.
        :rtype: List[float]
        """
        return self._q_load

    @q_load.setter
    def q_load(self, q_load: List[float]):
        """Sets the q_load of this LoadFile.


        :param q_load: The q_load of this LoadFile.
        :type q_load: List[float]
        """

        self._q_load = q_load

    @property
    def q_load_r(self) -> List[float]:
        """Gets the q_load_r of this LoadFile.


        :return: The q_load_r of this LoadFile.
        :rtype: List[float]
        """
        return self._q_load_r

    @q_load_r.setter
    def q_load_r(self, q_load_r: List[float]):
        """Sets the q_load_r of this LoadFile.


        :param q_load_r: The q_load_r of this LoadFile.
        :type q_load_r: List[float]
        """

        self._q_load_r = q_load_r

    @property
    def q_load_s(self) -> List[float]:
        """Gets the q_load_s of this LoadFile.


        :return: The q_load_s of this LoadFile.
        :rtype: List[float]
        """
        return self._q_load_s

    @q_load_s.setter
    def q_load_s(self, q_load_s: List[float]):
        """Sets the q_load_s of this LoadFile.


        :param q_load_s: The q_load_s of this LoadFile.
        :type q_load_s: List[float]
        """

        self._q_load_s = q_load_s

    @property
    def q_load_t(self) -> List[float]:
        """Gets the q_load_t of this LoadFile.


        :return: The q_load_t of this LoadFile.
        :rtype: List[float]
        """
        return self._q_load_t

    @q_load_t.setter
    def q_load_t(self, q_load_t: List[float]):
        """Sets the q_load_t of this LoadFile.


        :param q_load_t: The q_load_t of this LoadFile.
        :type q_load_t: List[float]
        """

        self._q_load_t = q_load_t

    @property
    def meta(self) -> MetaLoad:
        """Gets the meta of this LoadFile.


        :return: The meta of this LoadFile.
        :rtype: MetaLoad
        """
        return self._meta

    @meta.setter
    def meta(self, meta: MetaLoad):
        """Sets the meta of this LoadFile.


        :param meta: The meta of this LoadFile.
        :type meta: MetaLoad
        """

        self._meta = meta