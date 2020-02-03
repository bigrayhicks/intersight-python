# coding: utf-8

"""
    Cisco Intersight OpenAPI specification.

    The Cisco Intersight OpenAPI specification.

    OpenAPI spec version: 1.0.9-1295
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WorkflowCustomDataType(object):
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
        'default': 'WorkflowDefaultValue',
        'description': 'str',
        'label': 'str',
        'name': 'str',
        'required': 'bool',
        'properties': 'WorkflowCustomDataProperty'
    }

    attribute_map = {
        'object_type': 'ObjectType',
        'default': 'Default',
        'description': 'Description',
        'label': 'Label',
        'name': 'Name',
        'required': 'Required',
        'properties': 'Properties'
    }

    def __init__(self, object_type=None, default=None, description=None, label=None, name=None, required=None, properties=None):
        """
        WorkflowCustomDataType - a model defined in Swagger
        """

        self._object_type = None
        self._default = None
        self._description = None
        self._label = None
        self._name = None
        self._required = None
        self._properties = None

        if object_type is not None:
          self.object_type = object_type
        if default is not None:
          self.default = default
        if description is not None:
          self.description = description
        if label is not None:
          self.label = label
        if name is not None:
          self.name = name
        if required is not None:
          self.required = required
        if properties is not None:
          self.properties = properties

    @property
    def object_type(self):
        """
        Gets the object_type of this WorkflowCustomDataType.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :return: The object_type of this WorkflowCustomDataType.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this WorkflowCustomDataType.
        The concrete type of this complex type.  The ObjectType property must be set explicitly by API clients when the type is ambiguous. In all other cases, the  ObjectType is optional.  The type is ambiguous when a managed object contains an array of nested documents, and the documents in the array are heterogeneous, i.e. the array can contain nested documents of different types.    

        :param object_type: The object_type of this WorkflowCustomDataType.
        :type: str
        """

        self._object_type = object_type

    @property
    def default(self):
        """
        Gets the default of this WorkflowCustomDataType.
        Default value for the data type. If default value was provided and the input was required the default value will be used as the input.  

        :return: The default of this WorkflowCustomDataType.
        :rtype: WorkflowDefaultValue
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this WorkflowCustomDataType.
        Default value for the data type. If default value was provided and the input was required the default value will be used as the input.  

        :param default: The default of this WorkflowCustomDataType.
        :type: WorkflowDefaultValue
        """

        self._default = default

    @property
    def description(self):
        """
        Gets the description of this WorkflowCustomDataType.
        Provide a detailed description of the data type.  

        :return: The description of this WorkflowCustomDataType.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WorkflowCustomDataType.
        Provide a detailed description of the data type.  

        :param description: The description of this WorkflowCustomDataType.
        :type: str
        """

        self._description = description

    @property
    def label(self):
        """
        Gets the label of this WorkflowCustomDataType.
        Descriptive name for the data type.  

        :return: The label of this WorkflowCustomDataType.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WorkflowCustomDataType.
        Descriptive name for the data type.  

        :param label: The label of this WorkflowCustomDataType.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this WorkflowCustomDataType.
        Pick a descriptive name for the data type.  

        :return: The name of this WorkflowCustomDataType.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this WorkflowCustomDataType.
        Pick a descriptive name for the data type.  

        :param name: The name of this WorkflowCustomDataType.
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """
        Gets the required of this WorkflowCustomDataType.
        Specifies whether this parameter is required. The field is applicable for task and workflow.    

        :return: The required of this WorkflowCustomDataType.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this WorkflowCustomDataType.
        Specifies whether this parameter is required. The field is applicable for task and workflow.    

        :param required: The required of this WorkflowCustomDataType.
        :type: bool
        """

        self._required = required

    @property
    def properties(self):
        """
        Gets the properties of this WorkflowCustomDataType.
        Captures the custom data type properties.   

        :return: The properties of this WorkflowCustomDataType.
        :rtype: WorkflowCustomDataProperty
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this WorkflowCustomDataType.
        Captures the custom data type properties.   

        :param properties: The properties of this WorkflowCustomDataType.
        :type: WorkflowCustomDataProperty
        """

        self._properties = properties

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
        if not isinstance(other, WorkflowCustomDataType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other