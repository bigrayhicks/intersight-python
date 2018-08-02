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


class SnmpUser(object):
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
        'auth_password': 'str',
        'auth_type': 'str',
        'is_auth_password_set': 'bool',
        'is_privacy_password_set': 'bool',
        'name': 'str',
        'privacy_password': 'str',
        'privacy_type': 'str',
        'security_level': 'str'
    }

    attribute_map = {
        'auth_password': 'AuthPassword',
        'auth_type': 'AuthType',
        'is_auth_password_set': 'IsAuthPasswordSet',
        'is_privacy_password_set': 'IsPrivacyPasswordSet',
        'name': 'Name',
        'privacy_password': 'PrivacyPassword',
        'privacy_type': 'PrivacyType',
        'security_level': 'SecurityLevel'
    }

    def __init__(self, auth_password=None, auth_type='NA', is_auth_password_set=None, is_privacy_password_set=None, name=None, privacy_password=None, privacy_type='NA', security_level='AuthPriv'):
        """
        SnmpUser - a model defined in Swagger
        """

        self._auth_password = None
        self._auth_type = None
        self._is_auth_password_set = None
        self._is_privacy_password_set = None
        self._name = None
        self._privacy_password = None
        self._privacy_type = None
        self._security_level = None

        if auth_password is not None:
          self.auth_password = auth_password
        if auth_type is not None:
          self.auth_type = auth_type
        if is_auth_password_set is not None:
          self.is_auth_password_set = is_auth_password_set
        if is_privacy_password_set is not None:
          self.is_privacy_password_set = is_privacy_password_set
        if name is not None:
          self.name = name
        if privacy_password is not None:
          self.privacy_password = privacy_password
        if privacy_type is not None:
          self.privacy_type = privacy_type
        if security_level is not None:
          self.security_level = security_level

    @property
    def auth_password(self):
        """
        Gets the auth_password of this SnmpUser.
        Authorization password for the user  

        :return: The auth_password of this SnmpUser.
        :rtype: str
        """
        return self._auth_password

    @auth_password.setter
    def auth_password(self, auth_password):
        """
        Sets the auth_password of this SnmpUser.
        Authorization password for the user  

        :param auth_password: The auth_password of this SnmpUser.
        :type: str
        """

        self._auth_password = auth_password

    @property
    def auth_type(self):
        """
        Gets the auth_type of this SnmpUser.
        Authorization protocol for authenticating the user  

        :return: The auth_type of this SnmpUser.
        :rtype: str
        """
        return self._auth_type

    @auth_type.setter
    def auth_type(self, auth_type):
        """
        Sets the auth_type of this SnmpUser.
        Authorization protocol for authenticating the user  

        :param auth_type: The auth_type of this SnmpUser.
        :type: str
        """
        allowed_values = ["NA", "MD5", "SHA"]
        if auth_type not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_type` ({0}), must be one of {1}"
                .format(auth_type, allowed_values)
            )

        self._auth_type = auth_type

    @property
    def is_auth_password_set(self):
        """
        Gets the is_auth_password_set of this SnmpUser.

        :return: The is_auth_password_set of this SnmpUser.
        :rtype: bool
        """
        return self._is_auth_password_set

    @is_auth_password_set.setter
    def is_auth_password_set(self, is_auth_password_set):
        """
        Sets the is_auth_password_set of this SnmpUser.

        :param is_auth_password_set: The is_auth_password_set of this SnmpUser.
        :type: bool
        """

        self._is_auth_password_set = is_auth_password_set

    @property
    def is_privacy_password_set(self):
        """
        Gets the is_privacy_password_set of this SnmpUser.

        :return: The is_privacy_password_set of this SnmpUser.
        :rtype: bool
        """
        return self._is_privacy_password_set

    @is_privacy_password_set.setter
    def is_privacy_password_set(self, is_privacy_password_set):
        """
        Sets the is_privacy_password_set of this SnmpUser.

        :param is_privacy_password_set: The is_privacy_password_set of this SnmpUser.
        :type: bool
        """

        self._is_privacy_password_set = is_privacy_password_set

    @property
    def name(self):
        """
        Gets the name of this SnmpUser.
        SNMP username. Must have a minimum of 1 and and a maximum of 31 characters.  

        :return: The name of this SnmpUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SnmpUser.
        SNMP username. Must have a minimum of 1 and and a maximum of 31 characters.  

        :param name: The name of this SnmpUser.
        :type: str
        """

        self._name = name

    @property
    def privacy_password(self):
        """
        Gets the privacy_password of this SnmpUser.
        Privacy password for the user  

        :return: The privacy_password of this SnmpUser.
        :rtype: str
        """
        return self._privacy_password

    @privacy_password.setter
    def privacy_password(self, privacy_password):
        """
        Sets the privacy_password of this SnmpUser.
        Privacy password for the user  

        :param privacy_password: The privacy_password of this SnmpUser.
        :type: str
        """

        self._privacy_password = privacy_password

    @property
    def privacy_type(self):
        """
        Gets the privacy_type of this SnmpUser.
        Privacy protocol for the user  

        :return: The privacy_type of this SnmpUser.
        :rtype: str
        """
        return self._privacy_type

    @privacy_type.setter
    def privacy_type(self, privacy_type):
        """
        Sets the privacy_type of this SnmpUser.
        Privacy protocol for the user  

        :param privacy_type: The privacy_type of this SnmpUser.
        :type: str
        """
        allowed_values = ["NA", "DES", "AES"]
        if privacy_type not in allowed_values:
            raise ValueError(
                "Invalid value for `privacy_type` ({0}), must be one of {1}"
                .format(privacy_type, allowed_values)
            )

        self._privacy_type = privacy_type

    @property
    def security_level(self):
        """
        Gets the security_level of this SnmpUser.
        Security mechanism used for communication between agent and manager   

        :return: The security_level of this SnmpUser.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        """
        Sets the security_level of this SnmpUser.
        Security mechanism used for communication between agent and manager   

        :param security_level: The security_level of this SnmpUser.
        :type: str
        """
        allowed_values = ["AuthPriv", "NoAuthNoPriv", "AuthNoPriv"]
        if security_level not in allowed_values:
            raise ValueError(
                "Invalid value for `security_level` ({0}), must be one of {1}"
                .format(security_level, allowed_values)
            )

        self._security_level = security_level

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
        if not isinstance(other, SnmpUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
