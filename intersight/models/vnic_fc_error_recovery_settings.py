# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1461
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VnicFcErrorRecoverySettings(object):
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
        'object_type': 'str',
        'enabled': 'bool',
        'io_retry_count': 'int',
        'io_retry_timeout': 'int',
        'link_down_timeout': 'int',
        'port_down_timeout': 'int'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'enabled': 'Enabled',
        'io_retry_count': 'IoRetryCount',
        'io_retry_timeout': 'IoRetryTimeout',
        'link_down_timeout': 'LinkDownTimeout',
        'port_down_timeout': 'PortDownTimeout'
    }

    def __init__(self, object_type=None, enabled=None, io_retry_count=None, io_retry_timeout=None, link_down_timeout=None, port_down_timeout=None):
        """
        VnicFcErrorRecoverySettings - a model defined in Swagger
        """

        self._object_type = None
        self._enabled = None
        self._io_retry_count = None
        self._io_retry_timeout = None
        self._link_down_timeout = None
        self._port_down_timeout = None

        if object_type is not None:
          self.object_type = object_type
        if enabled is not None:
          self.enabled = enabled
        if io_retry_count is not None:
          self.io_retry_count = io_retry_count
        if io_retry_timeout is not None:
          self.io_retry_timeout = io_retry_timeout
        if link_down_timeout is not None:
          self.link_down_timeout = link_down_timeout
        if port_down_timeout is not None:
          self.port_down_timeout = port_down_timeout

    @property
    def object_type(self):
        """
        Gets the object_type of this VnicFcErrorRecoverySettings.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this VnicFcErrorRecoverySettings.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this VnicFcErrorRecoverySettings.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this VnicFcErrorRecoverySettings.
        :type: str
        """

        self._object_type = object_type

    @property
    def enabled(self):
        """
        Gets the enabled of this VnicFcErrorRecoverySettings.
        Enables Fibre Channel Error recovery.

        :return: The enabled of this VnicFcErrorRecoverySettings.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this VnicFcErrorRecoverySettings.
        Enables Fibre Channel Error recovery.

        :param enabled: The enabled of this VnicFcErrorRecoverySettings.
        :type: bool
        """

        self._enabled = enabled

    @property
    def io_retry_count(self):
        """
        Gets the io_retry_count of this VnicFcErrorRecoverySettings.
        The number of times an I/O request to a port is retried because the port is busy before the system decides the port is unavailable.

        :return: The io_retry_count of this VnicFcErrorRecoverySettings.
        :rtype: int
        """
        return self._io_retry_count

    @io_retry_count.setter
    def io_retry_count(self, io_retry_count):
        """
        Sets the io_retry_count of this VnicFcErrorRecoverySettings.
        The number of times an I/O request to a port is retried because the port is busy before the system decides the port is unavailable.

        :param io_retry_count: The io_retry_count of this VnicFcErrorRecoverySettings.
        :type: int
        """

        self._io_retry_count = io_retry_count

    @property
    def io_retry_timeout(self):
        """
        Gets the io_retry_timeout of this VnicFcErrorRecoverySettings.
        The number of seconds the adapter waits before aborting the pending command and resending the same IO request.

        :return: The io_retry_timeout of this VnicFcErrorRecoverySettings.
        :rtype: int
        """
        return self._io_retry_timeout

    @io_retry_timeout.setter
    def io_retry_timeout(self, io_retry_timeout):
        """
        Sets the io_retry_timeout of this VnicFcErrorRecoverySettings.
        The number of seconds the adapter waits before aborting the pending command and resending the same IO request.

        :param io_retry_timeout: The io_retry_timeout of this VnicFcErrorRecoverySettings.
        :type: int
        """

        self._io_retry_timeout = io_retry_timeout

    @property
    def link_down_timeout(self):
        """
        Gets the link_down_timeout of this VnicFcErrorRecoverySettings.
        The number of milliseconds the port should actually be down before it is marked down and fabric connectivity is lost.

        :return: The link_down_timeout of this VnicFcErrorRecoverySettings.
        :rtype: int
        """
        return self._link_down_timeout

    @link_down_timeout.setter
    def link_down_timeout(self, link_down_timeout):
        """
        Sets the link_down_timeout of this VnicFcErrorRecoverySettings.
        The number of milliseconds the port should actually be down before it is marked down and fabric connectivity is lost.

        :param link_down_timeout: The link_down_timeout of this VnicFcErrorRecoverySettings.
        :type: int
        """

        self._link_down_timeout = link_down_timeout

    @property
    def port_down_timeout(self):
        """
        Gets the port_down_timeout of this VnicFcErrorRecoverySettings.
        The number of milliseconds a remote Fibre Channel port should be offline before informing the SCSI upper layer that the port is unavailable. For a server with a VIC adapter running ESXi, the recommended value is 10000. For a server with a port used to boot a Windows OS from the SAN, the recommended value is 5000 milliseconds.

        :return: The port_down_timeout of this VnicFcErrorRecoverySettings.
        :rtype: int
        """
        return self._port_down_timeout

    @port_down_timeout.setter
    def port_down_timeout(self, port_down_timeout):
        """
        Sets the port_down_timeout of this VnicFcErrorRecoverySettings.
        The number of milliseconds a remote Fibre Channel port should be offline before informing the SCSI upper layer that the port is unavailable. For a server with a VIC adapter running ESXi, the recommended value is 10000. For a server with a port used to boot a Windows OS from the SAN, the recommended value is 5000 milliseconds.

        :param port_down_timeout: The port_down_timeout of this VnicFcErrorRecoverySettings.
        :type: int
        """

        self._port_down_timeout = port_down_timeout

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
        if not isinstance(other, VnicFcErrorRecoverySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
