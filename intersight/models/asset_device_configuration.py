# coding: utf-8

"""
    Intersight REST API

    This is Intersight REST API 

    OpenAPI spec version: 1.0.7-681
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AssetDeviceConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'account_moid': 'str',
        'ancestors': 'list[MoBaseMoRef]',
        'create_time': 'datetime',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'parent': 'MoBaseMoRef',
        'tags': 'list[MoTag]',
        'device': 'AssetDeviceRegistrationRef',
        'local_configuration_locked': 'bool',
        'log_level': 'str'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'ancestors': 'Ancestors',
        'create_time': 'CreateTime',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'parent': 'Parent',
        'tags': 'Tags',
        'device': 'Device',
        'local_configuration_locked': 'LocalConfigurationLocked',
        'log_level': 'LogLevel'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, device=None, local_configuration_locked=None, log_level=None):
        """
        AssetDeviceConfiguration - a model defined in Swagger
        """

        self._account_moid = None
        self._ancestors = None
        self._create_time = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._parent = None
        self._tags = None
        self._device = None
        self._local_configuration_locked = None
        self._log_level = None

        if account_moid is not None:
          self.account_moid = account_moid
        if ancestors is not None:
          self.ancestors = ancestors
        if create_time is not None:
          self.create_time = create_time
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if parent is not None:
          self.parent = parent
        if tags is not None:
          self.tags = tags
        if device is not None:
          self.device = device
        if local_configuration_locked is not None:
          self.local_configuration_locked = local_configuration_locked
        if log_level is not None:
          self.log_level = log_level

    @property
    def account_moid(self):
        """
        Gets the account_moid of this AssetDeviceConfiguration.
        The Account ID for this managed object.  

        :return: The account_moid of this AssetDeviceConfiguration.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this AssetDeviceConfiguration.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this AssetDeviceConfiguration.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this AssetDeviceConfiguration.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this AssetDeviceConfiguration.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this AssetDeviceConfiguration.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this AssetDeviceConfiguration.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this AssetDeviceConfiguration.
        The time when this managed object was created.  

        :return: The create_time of this AssetDeviceConfiguration.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this AssetDeviceConfiguration.
        The time when this managed object was created.  

        :param create_time: The create_time of this AssetDeviceConfiguration.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this AssetDeviceConfiguration.
        The time when this managed object was last modified.  

        :return: The mod_time of this AssetDeviceConfiguration.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this AssetDeviceConfiguration.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this AssetDeviceConfiguration.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this AssetDeviceConfiguration.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this AssetDeviceConfiguration.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this AssetDeviceConfiguration.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this AssetDeviceConfiguration.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this AssetDeviceConfiguration.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this AssetDeviceConfiguration.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this AssetDeviceConfiguration.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this AssetDeviceConfiguration.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this AssetDeviceConfiguration.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this AssetDeviceConfiguration.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this AssetDeviceConfiguration.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this AssetDeviceConfiguration.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this AssetDeviceConfiguration.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this AssetDeviceConfiguration.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this AssetDeviceConfiguration.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this AssetDeviceConfiguration.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this AssetDeviceConfiguration.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this AssetDeviceConfiguration.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this AssetDeviceConfiguration.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this AssetDeviceConfiguration.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def device(self):
        """
        Gets the device of this AssetDeviceConfiguration.

        :return: The device of this AssetDeviceConfiguration.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this AssetDeviceConfiguration.

        :param device: The device of this AssetDeviceConfiguration.
        :type: AssetDeviceRegistrationRef
        """

        self._device = device

    @property
    def local_configuration_locked(self):
        """
        Gets the local_configuration_locked of this AssetDeviceConfiguration.
        Specifies whether configuration through the platforms local management interface has been disabled, with only configuration through the Intersight service enabled  

        :return: The local_configuration_locked of this AssetDeviceConfiguration.
        :rtype: bool
        """
        return self._local_configuration_locked

    @local_configuration_locked.setter
    def local_configuration_locked(self, local_configuration_locked):
        """
        Sets the local_configuration_locked of this AssetDeviceConfiguration.
        Specifies whether configuration through the platforms local management interface has been disabled, with only configuration through the Intersight service enabled  

        :param local_configuration_locked: The local_configuration_locked of this AssetDeviceConfiguration.
        :type: bool
        """

        self._local_configuration_locked = local_configuration_locked

    @property
    def log_level(self):
        """
        Gets the log_level of this AssetDeviceConfiguration.
        The log level of the device connector service.   

        :return: The log_level of this AssetDeviceConfiguration.
        :rtype: str
        """
        return self._log_level

    @log_level.setter
    def log_level(self, log_level):
        """
        Sets the log_level of this AssetDeviceConfiguration.
        The log level of the device connector service.   

        :param log_level: The log_level of this AssetDeviceConfiguration.
        :type: str
        """

        self._log_level = log_level

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AssetDeviceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
