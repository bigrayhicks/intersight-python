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


class MoVersionContext(object):
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
        'interested_mos': 'list[MoMoRef]',
        'ref_mo': 'MoMoRef',
        'timestamp': 'datetime',
        'version': 'str',
        'version_type': 'str'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'interested_mos': 'InterestedMos',
        'ref_mo': 'RefMo',
        'timestamp': 'Timestamp',
        'version': 'Version',
        'version_type': 'VersionType'
    }

    def __init__(self, object_type=None, interested_mos=None, ref_mo=None, timestamp=None, version=None, version_type='Modified'):
        """
        MoVersionContext - a model defined in Swagger
        """

        self._object_type = None
        self._interested_mos = None
        self._ref_mo = None
        self._timestamp = None
        self._version = None
        self._version_type = None

        if object_type is not None:
          self.object_type = object_type
        if interested_mos is not None:
          self.interested_mos = interested_mos
        if ref_mo is not None:
          self.ref_mo = ref_mo
        if timestamp is not None:
          self.timestamp = timestamp
        if version is not None:
          self.version = version
        if version_type is not None:
          self.version_type = version_type

    @property
    def object_type(self):
        """
        Gets the object_type of this MoVersionContext.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this MoVersionContext.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MoVersionContext.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this MoVersionContext.
        :type: str
        """

        self._object_type = object_type

    @property
    def interested_mos(self):
        """
        Gets the interested_mos of this MoVersionContext.
        A collection of objects that have reference to this versioned object. The lifecycle of the versioned object is based on the interestedMos list; the versioned object will be purged when interestedMos is empty.

        :return: The interested_mos of this MoVersionContext.
        :rtype: list[MoMoRef]
        """
        return self._interested_mos

    @interested_mos.setter
    def interested_mos(self, interested_mos):
        """
        Sets the interested_mos of this MoVersionContext.
        A collection of objects that have reference to this versioned object. The lifecycle of the versioned object is based on the interestedMos list; the versioned object will be purged when interestedMos is empty.

        :param interested_mos: The interested_mos of this MoVersionContext.
        :type: list[MoMoRef]
        """

        self._interested_mos = interested_mos

    @property
    def ref_mo(self):
        """
        Gets the ref_mo of this MoVersionContext.
        A reference to the original Managed Object.

        :return: The ref_mo of this MoVersionContext.
        :rtype: MoMoRef
        """
        return self._ref_mo

    @ref_mo.setter
    def ref_mo(self, ref_mo):
        """
        Sets the ref_mo of this MoVersionContext.
        A reference to the original Managed Object.

        :param ref_mo: The ref_mo of this MoVersionContext.
        :type: MoMoRef
        """

        self._ref_mo = ref_mo

    @property
    def timestamp(self):
        """
        Gets the timestamp of this MoVersionContext.
        The time this versioned Managed Object was created.

        :return: The timestamp of this MoVersionContext.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this MoVersionContext.
        The time this versioned Managed Object was created.

        :param timestamp: The timestamp of this MoVersionContext.
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def version(self):
        """
        Gets the version of this MoVersionContext.
        The version of the Managed Object, e.g. an incrementing number or a hash id.

        :return: The version of this MoVersionContext.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this MoVersionContext.
        The version of the Managed Object, e.g. an incrementing number or a hash id.

        :param version: The version of this MoVersionContext.
        :type: str
        """

        self._version = version

    @property
    def version_type(self):
        """
        Gets the version_type of this MoVersionContext.
        Specifies type of version. Currently the only supported value is \"Configured\" that is used to keep track of snapshots of policies and profiles that are intended to be configured to target endpoints.

        :return: The version_type of this MoVersionContext.
        :rtype: str
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """
        Sets the version_type of this MoVersionContext.
        Specifies type of version. Currently the only supported value is \"Configured\" that is used to keep track of snapshots of policies and profiles that are intended to be configured to target endpoints.

        :param version_type: The version_type of this MoVersionContext.
        :type: str
        """
        allowed_values = ["Modified", "Configured", "Deployed"]
        if version_type not in allowed_values:
            raise ValueError(
                "Invalid value for `version_type` ({0}), must be one of {1}"
                .format(version_type, allowed_values)
            )

        self._version_type = version_type

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
        if not isinstance(other, MoVersionContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
