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


class StoragePureVolume(object):
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
        'create_time': 'datetime',
        'domain_group_moid': 'str',
        'mod_time': 'datetime',
        'moid': 'str',
        'object_type': 'str',
        'owners': 'list[str]',
        'shared_scope': 'str',
        'tags': 'list[MoTag]',
        'version_context': 'MoVersionContext',
        'ancestors': 'list[MoBaseMoRef]',
        'parent': 'MoBaseMoRef',
        'permission_resources': 'list[MoBaseMoRef]',
        'description': 'str',
        'naa_id': 'str',
        'name': 'str',
        'size': 'int',
        'storage_utilization': 'StorageCapacity',
        'storage_array': 'StorageGenericArrayRef',
        'created': 'datetime',
        'serial': 'str',
        'source': 'str',
        'registered_device': 'AssetDeviceRegistrationRef'
    }

    attribute_map = {
        'account_moid': 'AccountMoid',
        'create_time': 'CreateTime',
        'domain_group_moid': 'DomainGroupMoid',
        'mod_time': 'ModTime',
        'moid': 'Moid',
        'object_type': 'ObjectType',
        'owners': 'Owners',
        'shared_scope': 'SharedScope',
        'tags': 'Tags',
        'version_context': 'VersionContext',
        'ancestors': 'Ancestors',
        'parent': 'Parent',
        'permission_resources': 'PermissionResources',
        'description': 'Description',
        'naa_id': 'NaaId',
        'name': 'Name',
        'size': 'Size',
        'storage_utilization': 'StorageUtilization',
        'storage_array': 'StorageArray',
        'created': 'Created',
        'serial': 'Serial',
        'source': 'Source',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, description=None, naa_id=None, name=None, size=None, storage_utilization=None, storage_array=None, created=None, serial=None, source=None, registered_device=None):
        """
        StoragePureVolume - a model defined in Swagger
        """

        self._account_moid = None
        self._create_time = None
        self._domain_group_moid = None
        self._mod_time = None
        self._moid = None
        self._object_type = None
        self._owners = None
        self._shared_scope = None
        self._tags = None
        self._version_context = None
        self._ancestors = None
        self._parent = None
        self._permission_resources = None
        self._description = None
        self._naa_id = None
        self._name = None
        self._size = None
        self._storage_utilization = None
        self._storage_array = None
        self._created = None
        self._serial = None
        self._source = None
        self._registered_device = None

        if account_moid is not None:
          self.account_moid = account_moid
        if create_time is not None:
          self.create_time = create_time
        if domain_group_moid is not None:
          self.domain_group_moid = domain_group_moid
        if mod_time is not None:
          self.mod_time = mod_time
        if moid is not None:
          self.moid = moid
        if object_type is not None:
          self.object_type = object_type
        if owners is not None:
          self.owners = owners
        if shared_scope is not None:
          self.shared_scope = shared_scope
        if tags is not None:
          self.tags = tags
        if version_context is not None:
          self.version_context = version_context
        if ancestors is not None:
          self.ancestors = ancestors
        if parent is not None:
          self.parent = parent
        if permission_resources is not None:
          self.permission_resources = permission_resources
        if description is not None:
          self.description = description
        if naa_id is not None:
          self.naa_id = naa_id
        if name is not None:
          self.name = name
        if size is not None:
          self.size = size
        if storage_utilization is not None:
          self.storage_utilization = storage_utilization
        if storage_array is not None:
          self.storage_array = storage_array
        if created is not None:
          self.created = created
        if serial is not None:
          self.serial = serial
        if source is not None:
          self.source = source
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this StoragePureVolume.
        The Account ID for this managed object.

        :return: The account_moid of this StoragePureVolume.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this StoragePureVolume.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this StoragePureVolume.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this StoragePureVolume.
        The time when this managed object was created.

        :return: The create_time of this StoragePureVolume.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this StoragePureVolume.
        The time when this managed object was created.

        :param create_time: The create_time of this StoragePureVolume.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this StoragePureVolume.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this StoragePureVolume.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this StoragePureVolume.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this StoragePureVolume.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this StoragePureVolume.
        The time when this managed object was last modified.

        :return: The mod_time of this StoragePureVolume.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this StoragePureVolume.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this StoragePureVolume.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this StoragePureVolume.
        The unique identifier of this Managed Object instance.

        :return: The moid of this StoragePureVolume.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this StoragePureVolume.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this StoragePureVolume.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this StoragePureVolume.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this StoragePureVolume.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this StoragePureVolume.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this StoragePureVolume.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this StoragePureVolume.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this StoragePureVolume.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this StoragePureVolume.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this StoragePureVolume.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this StoragePureVolume.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this StoragePureVolume.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this StoragePureVolume.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this StoragePureVolume.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this StoragePureVolume.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this StoragePureVolume.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this StoragePureVolume.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this StoragePureVolume.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this StoragePureVolume.
        The versioning info for this managed object.

        :return: The version_context of this StoragePureVolume.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this StoragePureVolume.
        The versioning info for this managed object.

        :param version_context: The version_context of this StoragePureVolume.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this StoragePureVolume.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this StoragePureVolume.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this StoragePureVolume.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this StoragePureVolume.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this StoragePureVolume.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this StoragePureVolume.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this StoragePureVolume.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this StoragePureVolume.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this StoragePureVolume.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this StoragePureVolume.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this StoragePureVolume.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this StoragePureVolume.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def description(self):
        """
        Gets the description of this StoragePureVolume.
        Short description about the volume.

        :return: The description of this StoragePureVolume.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StoragePureVolume.
        Short description about the volume.

        :param description: The description of this StoragePureVolume.
        :type: str
        """

        self._description = description

    @property
    def naa_id(self):
        """
        Gets the naa_id of this StoragePureVolume.
        NAA id of volume. It is a significant number to identify corresponding lun path in hypervisor.

        :return: The naa_id of this StoragePureVolume.
        :rtype: str
        """
        return self._naa_id

    @naa_id.setter
    def naa_id(self, naa_id):
        """
        Sets the naa_id of this StoragePureVolume.
        NAA id of volume. It is a significant number to identify corresponding lun path in hypervisor.

        :param naa_id: The naa_id of this StoragePureVolume.
        :type: str
        """

        self._naa_id = naa_id

    @property
    def name(self):
        """
        Gets the name of this StoragePureVolume.
        Named entitiy of the volume.

        :return: The name of this StoragePureVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragePureVolume.
        Named entitiy of the volume.

        :param name: The name of this StoragePureVolume.
        :type: str
        """

        self._name = name

    @property
    def size(self):
        """
        Gets the size of this StoragePureVolume.
        User provisioned volume size. It is a size exposed to host.

        :return: The size of this StoragePureVolume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this StoragePureVolume.
        User provisioned volume size. It is a size exposed to host.

        :param size: The size of this StoragePureVolume.
        :type: int
        """

        self._size = size

    @property
    def storage_utilization(self):
        """
        Gets the storage_utilization of this StoragePureVolume.
        Storage utilization of volume entity in storage array.

        :return: The storage_utilization of this StoragePureVolume.
        :rtype: StorageCapacity
        """
        return self._storage_utilization

    @storage_utilization.setter
    def storage_utilization(self, storage_utilization):
        """
        Sets the storage_utilization of this StoragePureVolume.
        Storage utilization of volume entity in storage array.

        :param storage_utilization: The storage_utilization of this StoragePureVolume.
        :type: StorageCapacity
        """

        self._storage_utilization = storage_utilization

    @property
    def storage_array(self):
        """
        Gets the storage_array of this StoragePureVolume.
        Storage array managed object.

        :return: The storage_array of this StoragePureVolume.
        :rtype: StorageGenericArrayRef
        """
        return self._storage_array

    @storage_array.setter
    def storage_array(self, storage_array):
        """
        Sets the storage_array of this StoragePureVolume.
        Storage array managed object.

        :param storage_array: The storage_array of this StoragePureVolume.
        :type: StorageGenericArrayRef
        """

        self._storage_array = storage_array

    @property
    def created(self):
        """
        Gets the created of this StoragePureVolume.
        Creation time of the volume.

        :return: The created of this StoragePureVolume.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this StoragePureVolume.
        Creation time of the volume.

        :param created: The created of this StoragePureVolume.
        :type: datetime
        """

        self._created = created

    @property
    def serial(self):
        """
        Gets the serial of this StoragePureVolume.
        Serial number of the volume.

        :return: The serial of this StoragePureVolume.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this StoragePureVolume.
        Serial number of the volume.

        :param serial: The serial of this StoragePureVolume.
        :type: str
        """

        self._serial = serial

    @property
    def source(self):
        """
        Gets the source of this StoragePureVolume.
        Source from which the volume is created. Applicable only if the volume is cloned from other volume or snapshot.

        :return: The source of this StoragePureVolume.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this StoragePureVolume.
        Source from which the volume is created. Applicable only if the volume is cloned from other volume or snapshot.

        :param source: The source of this StoragePureVolume.
        :type: str
        """

        self._source = source

    @property
    def registered_device(self):
        """
        Gets the registered_device of this StoragePureVolume.
        Device registration managed object that represents this storage array connection to Intersight.

        :return: The registered_device of this StoragePureVolume.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this StoragePureVolume.
        Device registration managed object that represents this storage array connection to Intersight.

        :param registered_device: The registered_device of this StoragePureVolume.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

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
        if not isinstance(other, StoragePureVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
