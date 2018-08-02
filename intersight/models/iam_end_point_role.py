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


class IamEndPointRole(object):
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
        'account': 'IamAccountRef',
        'end_point_privileges': 'list[IamEndPointPrivilegeRef]',
        'name': 'str',
        'role_type': 'str',
        'system': 'IamSystemRef',
        'type': 'str'
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
        'account': 'Account',
        'end_point_privileges': 'EndPointPrivileges',
        'name': 'Name',
        'role_type': 'RoleType',
        'system': 'System',
        'type': 'Type'
    }

    def __init__(self, account_moid=None, ancestors=None, create_time=None, mod_time=None, moid=None, object_type=None, owners=None, parent=None, tags=None, account=None, end_point_privileges=None, name=None, role_type=None, system=None, type='null'):
        """
        IamEndPointRole - a model defined in Swagger
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
        self._account = None
        self._end_point_privileges = None
        self._name = None
        self._role_type = None
        self._system = None
        self._type = None

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
        if account is not None:
          self.account = account
        if end_point_privileges is not None:
          self.end_point_privileges = end_point_privileges
        if name is not None:
          self.name = name
        if role_type is not None:
          self.role_type = role_type
        if system is not None:
          self.system = system
        if type is not None:
          self.type = type

    @property
    def account_moid(self):
        """
        Gets the account_moid of this IamEndPointRole.
        The Account ID for this managed object.  

        :return: The account_moid of this IamEndPointRole.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this IamEndPointRole.
        The Account ID for this managed object.  

        :param account_moid: The account_moid of this IamEndPointRole.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def ancestors(self):
        """
        Gets the ancestors of this IamEndPointRole.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :return: The ancestors of this IamEndPointRole.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this IamEndPointRole.
        Ancestors is an array containing the MO references of the ancestors in the object containment hierarchy. 

        :param ancestors: The ancestors of this IamEndPointRole.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def create_time(self):
        """
        Gets the create_time of this IamEndPointRole.
        The time when this managed object was created.  

        :return: The create_time of this IamEndPointRole.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this IamEndPointRole.
        The time when this managed object was created.  

        :param create_time: The create_time of this IamEndPointRole.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def mod_time(self):
        """
        Gets the mod_time of this IamEndPointRole.
        The time when this managed object was last modified.  

        :return: The mod_time of this IamEndPointRole.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this IamEndPointRole.
        The time when this managed object was last modified.  

        :param mod_time: The mod_time of this IamEndPointRole.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this IamEndPointRole.
        A unique identifier of this Managed Object instance.  

        :return: The moid of this IamEndPointRole.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this IamEndPointRole.
        A unique identifier of this Managed Object instance.  

        :param moid: The moid of this IamEndPointRole.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this IamEndPointRole.
        The fully-qualified type of this managed object, e.g. the class name.  

        :return: The object_type of this IamEndPointRole.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this IamEndPointRole.
        The fully-qualified type of this managed object, e.g. the class name.  

        :param object_type: The object_type of this IamEndPointRole.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this IamEndPointRole.
        An array of owners which represent effective ownership of this object.   

        :return: The owners of this IamEndPointRole.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this IamEndPointRole.
        An array of owners which represent effective ownership of this object.   

        :param owners: The owners of this IamEndPointRole.
        :type: list[str]
        """

        self._owners = owners

    @property
    def parent(self):
        """
        Gets the parent of this IamEndPointRole.
        The direct ancestor of this managed object in the containment hierarchy. 

        :return: The parent of this IamEndPointRole.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this IamEndPointRole.
        The direct ancestor of this managed object in the containment hierarchy. 

        :param parent: The parent of this IamEndPointRole.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def tags(self):
        """
        Gets the tags of this IamEndPointRole.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :return: The tags of this IamEndPointRole.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this IamEndPointRole.
        An array of tags, which allow to add key, value meta-data to managed objects.   

        :param tags: The tags of this IamEndPointRole.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def account(self):
        """
        Gets the account of this IamEndPointRole.

        :return: The account of this IamEndPointRole.
        :rtype: IamAccountRef
        """
        return self._account

    @account.setter
    def account(self, account):
        """
        Sets the account of this IamEndPointRole.

        :param account: The account of this IamEndPointRole.
        :type: IamAccountRef
        """

        self._account = account

    @property
    def end_point_privileges(self):
        """
        Gets the end_point_privileges of this IamEndPointRole.
        Privileges assigned to this end point role. These privileges are assigned to users using end point roles to perform operations such as GUI/CLI cross launch. 

        :return: The end_point_privileges of this IamEndPointRole.
        :rtype: list[IamEndPointPrivilegeRef]
        """
        return self._end_point_privileges

    @end_point_privileges.setter
    def end_point_privileges(self, end_point_privileges):
        """
        Sets the end_point_privileges of this IamEndPointRole.
        Privileges assigned to this end point role. These privileges are assigned to users using end point roles to perform operations such as GUI/CLI cross launch. 

        :param end_point_privileges: The end_point_privileges of this IamEndPointRole.
        :type: list[IamEndPointPrivilegeRef]
        """

        self._end_point_privileges = end_point_privileges

    @property
    def name(self):
        """
        Gets the name of this IamEndPointRole.
        Name of the end point role.   

        :return: The name of this IamEndPointRole.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IamEndPointRole.
        Name of the end point role.   

        :param name: The name of this IamEndPointRole.
        :type: str
        """

        self._name = name

    @property
    def role_type(self):
        """
        Gets the role_type of this IamEndPointRole.
        Used to specify tags to roles such as ep-admin, ep-readonly.  

        :return: The role_type of this IamEndPointRole.
        :rtype: str
        """
        return self._role_type

    @role_type.setter
    def role_type(self, role_type):
        """
        Sets the role_type of this IamEndPointRole.
        Used to specify tags to roles such as ep-admin, ep-readonly.  

        :param role_type: The role_type of this IamEndPointRole.
        :type: str
        """

        self._role_type = role_type

    @property
    def system(self):
        """
        Gets the system of this IamEndPointRole.

        :return: The system of this IamEndPointRole.
        :rtype: IamSystemRef
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this IamEndPointRole.

        :param system: The system of this IamEndPointRole.
        :type: IamSystemRef
        """

        self._system = system

    @property
    def type(self):
        """
        Gets the type of this IamEndPointRole.
        Type of the end point such as UCSFI, IMC etc.    

        :return: The type of this IamEndPointRole.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this IamEndPointRole.
        Type of the end point such as UCSFI, IMC etc.    

        :param type: The type of this IamEndPointRole.
        :type: str
        """
        allowed_values = ["", "APIC", "UCSFI", "IMC", "IMCM4", "IMCM5", "HX", "UCSD", "IntersightAppliance", "PureStorage"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, IamEndPointRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
