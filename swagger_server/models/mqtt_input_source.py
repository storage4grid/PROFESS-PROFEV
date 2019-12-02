# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.chargers_mqtt import ChargersMqtt  # noqa: F401,E501
from swagger_server.models.ess import ESS  # noqa: F401,E501
from swagger_server.models.ev_file import EvFile  # noqa: F401,E501
from swagger_server.models.generic import Generic  # noqa: F401,E501
from swagger_server.models.global_control import GlobalControl  # noqa: F401,E501
from swagger_server.models.grid import Grid  # noqa: F401,E501
from swagger_server.models.horizons import Horizons  # noqa: F401,E501
from swagger_server.models.load import Load  # noqa: F401,E501
from swagger_server.models.pv import PV  # noqa: F401,E501
from swagger_server.models.uncertainity_file import UncertainityFile  # noqa: F401,E501
from swagger_server import util


class MQTTInputSource(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, generic: Generic=None, load: Load=None, photovoltaic: PV=None, ess: ESS=None, grid: Grid=None, global_control: GlobalControl=None, horizons: Horizons=None, ev: EvFile=None, chargers: ChargersMqtt=None, uncertainity: UncertainityFile=None):  # noqa: E501
        """MQTTInputSource - a model defined in Swagger

        :param generic: The generic of this MQTTInputSource.  # noqa: E501
        :type generic: Generic
        :param load: The load of this MQTTInputSource.  # noqa: E501
        :type load: Load
        :param photovoltaic: The photovoltaic of this MQTTInputSource.  # noqa: E501
        :type photovoltaic: PV
        :param ess: The ess of this MQTTInputSource.  # noqa: E501
        :type ess: ESS
        :param grid: The grid of this MQTTInputSource.  # noqa: E501
        :type grid: Grid
        :param global_control: The global_control of this MQTTInputSource.  # noqa: E501
        :type global_control: GlobalControl
        :param horizons: The horizons of this MQTTInputSource.  # noqa: E501
        :type horizons: Horizons
        :param ev: The ev of this MQTTInputSource.  # noqa: E501
        :type ev: EvFile
        :param chargers: The chargers of this MQTTInputSource.  # noqa: E501
        :type chargers: ChargersMqtt
        :param uncertainity: The uncertainity of this MQTTInputSource.  # noqa: E501
        :type uncertainity: UncertainityFile
        """
        self.swagger_types = {
            'generic': Generic,
            'load': Load,
            'photovoltaic': PV,
            'ess': ESS,
            'grid': Grid,
            'global_control': GlobalControl,
            'horizons': Horizons,
            'ev': EvFile,
            'chargers': ChargersMqtt,
            'uncertainity': UncertainityFile
        }

        self.attribute_map = {
            'generic': 'generic',
            'load': 'load',
            'photovoltaic': 'photovoltaic',
            'ess': 'ESS',
            'grid': 'grid',
            'global_control': 'global_control',
            'horizons': 'horizons',
            'ev': 'EV',
            'chargers': 'chargers',
            'uncertainity': 'uncertainity'
        }

        self._generic = generic
        self._load = load
        self._photovoltaic = photovoltaic
        self._ess = ess
        self._grid = grid
        self._global_control = global_control
        self._horizons = horizons
        self._ev = ev
        self._chargers = chargers
        self._uncertainity = uncertainity

    @classmethod
    def from_dict(cls, dikt) -> 'MQTTInputSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MQTTInputSource of this MQTTInputSource.  # noqa: E501
        :rtype: MQTTInputSource
        """
        return util.deserialize_model(dikt, cls)

    @property
    def generic(self) -> Generic:
        """Gets the generic of this MQTTInputSource.


        :return: The generic of this MQTTInputSource.
        :rtype: Generic
        """
        return self._generic

    @generic.setter
    def generic(self, generic: Generic):
        """Sets the generic of this MQTTInputSource.


        :param generic: The generic of this MQTTInputSource.
        :type generic: Generic
        """

        self._generic = generic

    @property
    def load(self) -> Load:
        """Gets the load of this MQTTInputSource.


        :return: The load of this MQTTInputSource.
        :rtype: Load
        """
        return self._load

    @load.setter
    def load(self, load: Load):
        """Sets the load of this MQTTInputSource.


        :param load: The load of this MQTTInputSource.
        :type load: Load
        """

        self._load = load

    @property
    def photovoltaic(self) -> PV:
        """Gets the photovoltaic of this MQTTInputSource.


        :return: The photovoltaic of this MQTTInputSource.
        :rtype: PV
        """
        return self._photovoltaic

    @photovoltaic.setter
    def photovoltaic(self, photovoltaic: PV):
        """Sets the photovoltaic of this MQTTInputSource.


        :param photovoltaic: The photovoltaic of this MQTTInputSource.
        :type photovoltaic: PV
        """

        self._photovoltaic = photovoltaic

    @property
    def ess(self) -> ESS:
        """Gets the ess of this MQTTInputSource.


        :return: The ess of this MQTTInputSource.
        :rtype: ESS
        """
        return self._ess

    @ess.setter
    def ess(self, ess: ESS):
        """Sets the ess of this MQTTInputSource.


        :param ess: The ess of this MQTTInputSource.
        :type ess: ESS
        """

        self._ess = ess

    @property
    def grid(self) -> Grid:
        """Gets the grid of this MQTTInputSource.


        :return: The grid of this MQTTInputSource.
        :rtype: Grid
        """
        return self._grid

    @grid.setter
    def grid(self, grid: Grid):
        """Sets the grid of this MQTTInputSource.


        :param grid: The grid of this MQTTInputSource.
        :type grid: Grid
        """

        self._grid = grid

    @property
    def global_control(self) -> GlobalControl:
        """Gets the global_control of this MQTTInputSource.


        :return: The global_control of this MQTTInputSource.
        :rtype: GlobalControl
        """
        return self._global_control

    @global_control.setter
    def global_control(self, global_control: GlobalControl):
        """Sets the global_control of this MQTTInputSource.


        :param global_control: The global_control of this MQTTInputSource.
        :type global_control: GlobalControl
        """

        self._global_control = global_control

    @property
    def horizons(self) -> Horizons:
        """Gets the horizons of this MQTTInputSource.


        :return: The horizons of this MQTTInputSource.
        :rtype: Horizons
        """
        return self._horizons

    @horizons.setter
    def horizons(self, horizons: Horizons):
        """Sets the horizons of this MQTTInputSource.


        :param horizons: The horizons of this MQTTInputSource.
        :type horizons: Horizons
        """

        self._horizons = horizons

    @property
    def ev(self) -> EvFile:
        """Gets the ev of this MQTTInputSource.


        :return: The ev of this MQTTInputSource.
        :rtype: EvFile
        """
        return self._ev

    @ev.setter
    def ev(self, ev: EvFile):
        """Sets the ev of this MQTTInputSource.


        :param ev: The ev of this MQTTInputSource.
        :type ev: EvFile
        """

        self._ev = ev

    @property
    def chargers(self) -> ChargersMqtt:
        """Gets the chargers of this MQTTInputSource.


        :return: The chargers of this MQTTInputSource.
        :rtype: ChargersMqtt
        """
        return self._chargers

    @chargers.setter
    def chargers(self, chargers: ChargersMqtt):
        """Sets the chargers of this MQTTInputSource.


        :param chargers: The chargers of this MQTTInputSource.
        :type chargers: ChargersMqtt
        """

        self._chargers = chargers

    @property
    def uncertainity(self) -> UncertainityFile:
        """Gets the uncertainity of this MQTTInputSource.


        :return: The uncertainity of this MQTTInputSource.
        :rtype: UncertainityFile
        """
        return self._uncertainity

    @uncertainity.setter
    def uncertainity(self, uncertainity: UncertainityFile):
        """Sets the uncertainity of this MQTTInputSource.


        :param uncertainity: The uncertainity of this MQTTInputSource.
        :type uncertainity: UncertainityFile
        """

        self._uncertainity = uncertainity