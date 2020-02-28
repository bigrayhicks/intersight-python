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


class MetaPropDefinition(object):
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
        'api_access': 'str',
        'name': 'str',
        'op_security': 'str',
        'search_weight': 'float'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'api_access': 'ApiAccess',
        'name': 'Name',
        'op_security': 'OpSecurity',
        'search_weight': 'SearchWeight'
    }

    def __init__(self, object_type=None, api_access='NoAccess', name=None, op_security='ClearText', search_weight=None):
        """
        MetaPropDefinition - a model defined in Swagger
        """

        self._object_type = None
        self._api_access = None
        self._name = None
        self._op_security = None
        self._search_weight = None

        if object_type is not None:
          self.object_type = object_type
        if api_access is not None:
          self.api_access = api_access
        if name is not None:
          self.name = name
        if op_security is not None:
          self.op_security = op_security
        if search_weight is not None:
          self.search_weight = search_weight

    @property
    def object_type(self):
        """
        Gets the object_type of this MetaPropDefinition.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :return: The object_type of this MetaPropDefinition.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this MetaPropDefinition.
        The concrete type of this complex type. The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.

        :param object_type: The object_type of this MetaPropDefinition.
        :type: str
        """

        self._object_type = object_type

    @property
    def api_access(self):
        """
        Gets the api_access of this MetaPropDefinition.
        API access control for the property. Examples are NoAccess, ReadOnly, CreateOnly etc.

        :return: The api_access of this MetaPropDefinition.
        :rtype: str
        """
        return self._api_access

    @api_access.setter
    def api_access(self, api_access):
        """
        Sets the api_access of this MetaPropDefinition.
        API access control for the property. Examples are NoAccess, ReadOnly, CreateOnly etc.

        :param api_access: The api_access of this MetaPropDefinition.
        :type: str
        """
        allowed_values = ["NoAccess", "ReadOnly", "CreateOnly", "ReadWrite", "WriteOnly", "ReadOnCreate"]
        if api_access not in allowed_values:
            raise ValueError(
                "Invalid value for `api_access` ({0}), must be one of {1}"
                .format(api_access, allowed_values)
            )

        self._api_access = api_access

    @property
    def name(self):
        """
        Gets the name of this MetaPropDefinition.
        The name of the property.

        :return: The name of this MetaPropDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MetaPropDefinition.
        The name of the property.

        :param name: The name of this MetaPropDefinition.
        :type: str
        """

        self._name = name

    @property
    def op_security(self):
        """
        Gets the op_security of this MetaPropDefinition.
        The data-at-rest security protection applied to this property when a Managed Object is persisted. For example, Encrypted or Cleartext.

        :return: The op_security of this MetaPropDefinition.
        :rtype: str
        """
        return self._op_security

    @op_security.setter
    def op_security(self, op_security):
        """
        Sets the op_security of this MetaPropDefinition.
        The data-at-rest security protection applied to this property when a Managed Object is persisted. For example, Encrypted or Cleartext.

        :param op_security: The op_security of this MetaPropDefinition.
        :type: str
        """
        allowed_values = ["ClearText", "Encrypted", "Pbkdf2", "Bcrypt", "Sha512crypt"]
        if op_security not in allowed_values:
            raise ValueError(
                "Invalid value for `op_security` ({0}), must be one of {1}"
                .format(op_security, allowed_values)
            )

        self._op_security = op_security

    @property
    def search_weight(self):
        """
        Gets the search_weight of this MetaPropDefinition.
        Enables the property to be searchable from global search. A value of 0 means this property is not globally searchable.

        :return: The search_weight of this MetaPropDefinition.
        :rtype: float
        """
        return self._search_weight

    @search_weight.setter
    def search_weight(self, search_weight):
        """
        Sets the search_weight of this MetaPropDefinition.
        Enables the property to be searchable from global search. A value of 0 means this property is not globally searchable.

        :param search_weight: The search_weight of this MetaPropDefinition.
        :type: float
        """

        self._search_weight = search_weight

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
        if not isinstance(other, MetaPropDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
