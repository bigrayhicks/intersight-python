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


class EquipmentChassis(object):
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
        'device_mo_id': 'str',
        'dn': 'str',
        'rn': 'str',
        'model': 'str',
        'revision': 'str',
        'serial': 'str',
        'vendor': 'str',
        'chassis_id': 'int',
        'connection_path': 'str',
        'connection_status': 'str',
        'description': 'str',
        'fault_summary': 'int',
        'name': 'str',
        'oper_state': 'str',
        'part_number': 'str',
        'pid': 'str',
        'platform_type': 'str',
        'product_name': 'str',
        'sku': 'str',
        'vid': 'str',
        'blades': 'list[ComputeBladeRef]',
        'fanmodules': 'list[EquipmentFanModuleRef]',
        'ioms': 'list[EquipmentIoCardRef]',
        'psus': 'list[EquipmentPsuRef]',
        'registered_device': 'AssetDeviceRegistrationRef',
        'sasexpanders': 'list[StorageSasExpanderRef]',
        'siocs': 'list[EquipmentSystemIoControllerRef]',
        'storage_enclosures': 'list[StorageEnclosureRef]'
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
        'device_mo_id': 'DeviceMoId',
        'dn': 'Dn',
        'rn': 'Rn',
        'model': 'Model',
        'revision': 'Revision',
        'serial': 'Serial',
        'vendor': 'Vendor',
        'chassis_id': 'ChassisId',
        'connection_path': 'ConnectionPath',
        'connection_status': 'ConnectionStatus',
        'description': 'Description',
        'fault_summary': 'FaultSummary',
        'name': 'Name',
        'oper_state': 'OperState',
        'part_number': 'PartNumber',
        'pid': 'Pid',
        'platform_type': 'PlatformType',
        'product_name': 'ProductName',
        'sku': 'Sku',
        'vid': 'Vid',
        'blades': 'Blades',
        'fanmodules': 'Fanmodules',
        'ioms': 'Ioms',
        'psus': 'Psus',
        'registered_device': 'RegisteredDevice',
        'sasexpanders': 'Sasexpanders',
        'siocs': 'Siocs',
        'storage_enclosures': 'StorageEnclosures'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, device_mo_id=None, dn=None, rn=None, model=None, revision=None, serial=None, vendor=None, chassis_id=None, connection_path=None, connection_status=None, description=None, fault_summary=None, name=None, oper_state=None, part_number=None, pid=None, platform_type=None, product_name=None, sku=None, vid=None, blades=None, fanmodules=None, ioms=None, psus=None, registered_device=None, sasexpanders=None, siocs=None, storage_enclosures=None):
        """
        EquipmentChassis - a model defined in Swagger
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
        self._device_mo_id = None
        self._dn = None
        self._rn = None
        self._model = None
        self._revision = None
        self._serial = None
        self._vendor = None
        self._chassis_id = None
        self._connection_path = None
        self._connection_status = None
        self._description = None
        self._fault_summary = None
        self._name = None
        self._oper_state = None
        self._part_number = None
        self._pid = None
        self._platform_type = None
        self._product_name = None
        self._sku = None
        self._vid = None
        self._blades = None
        self._fanmodules = None
        self._ioms = None
        self._psus = None
        self._registered_device = None
        self._sasexpanders = None
        self._siocs = None
        self._storage_enclosures = None

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
        if device_mo_id is not None:
          self.device_mo_id = device_mo_id
        if dn is not None:
          self.dn = dn
        if rn is not None:
          self.rn = rn
        if model is not None:
          self.model = model
        if revision is not None:
          self.revision = revision
        if serial is not None:
          self.serial = serial
        if vendor is not None:
          self.vendor = vendor
        if chassis_id is not None:
          self.chassis_id = chassis_id
        if connection_path is not None:
          self.connection_path = connection_path
        if connection_status is not None:
          self.connection_status = connection_status
        if description is not None:
          self.description = description
        if fault_summary is not None:
          self.fault_summary = fault_summary
        if name is not None:
          self.name = name
        if oper_state is not None:
          self.oper_state = oper_state
        if part_number is not None:
          self.part_number = part_number
        if pid is not None:
          self.pid = pid
        if platform_type is not None:
          self.platform_type = platform_type
        if product_name is not None:
          self.product_name = product_name
        if sku is not None:
          self.sku = sku
        if vid is not None:
          self.vid = vid
        if blades is not None:
          self.blades = blades
        if fanmodules is not None:
          self.fanmodules = fanmodules
        if ioms is not None:
          self.ioms = ioms
        if psus is not None:
          self.psus = psus
        if registered_device is not None:
          self.registered_device = registered_device
        if sasexpanders is not None:
          self.sasexpanders = sasexpanders
        if siocs is not None:
          self.siocs = siocs
        if storage_enclosures is not None:
          self.storage_enclosures = storage_enclosures

    @property
    def account_moid(self):
        """
        Gets the account_moid of this EquipmentChassis.
        The Account ID for this managed object.

        :return: The account_moid of this EquipmentChassis.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this EquipmentChassis.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this EquipmentChassis.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this EquipmentChassis.
        The time when this managed object was created.

        :return: The create_time of this EquipmentChassis.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this EquipmentChassis.
        The time when this managed object was created.

        :param create_time: The create_time of this EquipmentChassis.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this EquipmentChassis.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this EquipmentChassis.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this EquipmentChassis.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this EquipmentChassis.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this EquipmentChassis.
        The time when this managed object was last modified.

        :return: The mod_time of this EquipmentChassis.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this EquipmentChassis.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this EquipmentChassis.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this EquipmentChassis.
        The unique identifier of this Managed Object instance.

        :return: The moid of this EquipmentChassis.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this EquipmentChassis.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this EquipmentChassis.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this EquipmentChassis.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this EquipmentChassis.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this EquipmentChassis.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this EquipmentChassis.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this EquipmentChassis.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this EquipmentChassis.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this EquipmentChassis.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this EquipmentChassis.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this EquipmentChassis.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this EquipmentChassis.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this EquipmentChassis.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this EquipmentChassis.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this EquipmentChassis.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this EquipmentChassis.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this EquipmentChassis.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this EquipmentChassis.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this EquipmentChassis.
        The versioning info for this managed object.

        :return: The version_context of this EquipmentChassis.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this EquipmentChassis.
        The versioning info for this managed object.

        :param version_context: The version_context of this EquipmentChassis.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this EquipmentChassis.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this EquipmentChassis.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this EquipmentChassis.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this EquipmentChassis.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this EquipmentChassis.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this EquipmentChassis.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this EquipmentChassis.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this EquipmentChassis.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this EquipmentChassis.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this EquipmentChassis.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this EquipmentChassis.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this EquipmentChassis.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def device_mo_id(self):
        """
        Gets the device_mo_id of this EquipmentChassis.

        :return: The device_mo_id of this EquipmentChassis.
        :rtype: str
        """
        return self._device_mo_id

    @device_mo_id.setter
    def device_mo_id(self, device_mo_id):
        """
        Sets the device_mo_id of this EquipmentChassis.

        :param device_mo_id: The device_mo_id of this EquipmentChassis.
        :type: str
        """

        self._device_mo_id = device_mo_id

    @property
    def dn(self):
        """
        Gets the dn of this EquipmentChassis.
        The Distinguished Name unambiguously identifies an object in the system.

        :return: The dn of this EquipmentChassis.
        :rtype: str
        """
        return self._dn

    @dn.setter
    def dn(self, dn):
        """
        Sets the dn of this EquipmentChassis.
        The Distinguished Name unambiguously identifies an object in the system.

        :param dn: The dn of this EquipmentChassis.
        :type: str
        """

        self._dn = dn

    @property
    def rn(self):
        """
        Gets the rn of this EquipmentChassis.
        The Relative Name uniquely identifies an object within a given context.

        :return: The rn of this EquipmentChassis.
        :rtype: str
        """
        return self._rn

    @rn.setter
    def rn(self, rn):
        """
        Sets the rn of this EquipmentChassis.
        The Relative Name uniquely identifies an object within a given context.

        :param rn: The rn of this EquipmentChassis.
        :type: str
        """

        self._rn = rn

    @property
    def model(self):
        """
        Gets the model of this EquipmentChassis.
        This field identifies the model of the given component.

        :return: The model of this EquipmentChassis.
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """
        Sets the model of this EquipmentChassis.
        This field identifies the model of the given component.

        :param model: The model of this EquipmentChassis.
        :type: str
        """

        self._model = model

    @property
    def revision(self):
        """
        Gets the revision of this EquipmentChassis.

        :return: The revision of this EquipmentChassis.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this EquipmentChassis.

        :param revision: The revision of this EquipmentChassis.
        :type: str
        """

        self._revision = revision

    @property
    def serial(self):
        """
        Gets the serial of this EquipmentChassis.
        This field identifies the serial of the given component.

        :return: The serial of this EquipmentChassis.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this EquipmentChassis.
        This field identifies the serial of the given component.

        :param serial: The serial of this EquipmentChassis.
        :type: str
        """

        self._serial = serial

    @property
    def vendor(self):
        """
        Gets the vendor of this EquipmentChassis.
        This field identifies the vendor of the given component.

        :return: The vendor of this EquipmentChassis.
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """
        Sets the vendor of this EquipmentChassis.
        This field identifies the vendor of the given component.

        :param vendor: The vendor of this EquipmentChassis.
        :type: str
        """

        self._vendor = vendor

    @property
    def chassis_id(self):
        """
        Gets the chassis_id of this EquipmentChassis.
        The assigned identifier for a chassis.

        :return: The chassis_id of this EquipmentChassis.
        :rtype: int
        """
        return self._chassis_id

    @chassis_id.setter
    def chassis_id(self, chassis_id):
        """
        Sets the chassis_id of this EquipmentChassis.
        The assigned identifier for a chassis.

        :param chassis_id: The chassis_id of this EquipmentChassis.
        :type: int
        """

        self._chassis_id = chassis_id

    @property
    def connection_path(self):
        """
        Gets the connection_path of this EquipmentChassis.
        This field identifies the connectivity path for the chassis enclosure.

        :return: The connection_path of this EquipmentChassis.
        :rtype: str
        """
        return self._connection_path

    @connection_path.setter
    def connection_path(self, connection_path):
        """
        Sets the connection_path of this EquipmentChassis.
        This field identifies the connectivity path for the chassis enclosure.

        :param connection_path: The connection_path of this EquipmentChassis.
        :type: str
        """

        self._connection_path = connection_path

    @property
    def connection_status(self):
        """
        Gets the connection_status of this EquipmentChassis.
        This field identifies the connectivity status for the chassis enclosure.

        :return: The connection_status of this EquipmentChassis.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        """
        Sets the connection_status of this EquipmentChassis.
        This field identifies the connectivity status for the chassis enclosure.

        :param connection_status: The connection_status of this EquipmentChassis.
        :type: str
        """

        self._connection_status = connection_status

    @property
    def description(self):
        """
        Gets the description of this EquipmentChassis.
        This field is to provide description for chassis model.

        :return: The description of this EquipmentChassis.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this EquipmentChassis.
        This field is to provide description for chassis model.

        :param description: The description of this EquipmentChassis.
        :type: str
        """

        self._description = description

    @property
    def fault_summary(self):
        """
        Gets the fault_summary of this EquipmentChassis.

        :return: The fault_summary of this EquipmentChassis.
        :rtype: int
        """
        return self._fault_summary

    @fault_summary.setter
    def fault_summary(self, fault_summary):
        """
        Sets the fault_summary of this EquipmentChassis.

        :param fault_summary: The fault_summary of this EquipmentChassis.
        :type: int
        """

        self._fault_summary = fault_summary

    @property
    def name(self):
        """
        Gets the name of this EquipmentChassis.
        This field identifies the name for the chassis enclosure.

        :return: The name of this EquipmentChassis.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EquipmentChassis.
        This field identifies the name for the chassis enclosure.

        :param name: The name of this EquipmentChassis.
        :type: str
        """

        self._name = name

    @property
    def oper_state(self):
        """
        Gets the oper_state of this EquipmentChassis.

        :return: The oper_state of this EquipmentChassis.
        :rtype: str
        """
        return self._oper_state

    @oper_state.setter
    def oper_state(self, oper_state):
        """
        Sets the oper_state of this EquipmentChassis.

        :param oper_state: The oper_state of this EquipmentChassis.
        :type: str
        """

        self._oper_state = oper_state

    @property
    def part_number(self):
        """
        Gets the part_number of this EquipmentChassis.
        Part Number identifier for the chassis enclosure.

        :return: The part_number of this EquipmentChassis.
        :rtype: str
        """
        return self._part_number

    @part_number.setter
    def part_number(self, part_number):
        """
        Sets the part_number of this EquipmentChassis.
        Part Number identifier for the chassis enclosure.

        :param part_number: The part_number of this EquipmentChassis.
        :type: str
        """

        self._part_number = part_number

    @property
    def pid(self):
        """
        Gets the pid of this EquipmentChassis.
        This field identifies the Product ID for the chassis enclosure.

        :return: The pid of this EquipmentChassis.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """
        Sets the pid of this EquipmentChassis.
        This field identifies the Product ID for the chassis enclosure.

        :param pid: The pid of this EquipmentChassis.
        :type: str
        """

        self._pid = pid

    @property
    def platform_type(self):
        """
        Gets the platform_type of this EquipmentChassis.

        :return: The platform_type of this EquipmentChassis.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """
        Sets the platform_type of this EquipmentChassis.

        :param platform_type: The platform_type of this EquipmentChassis.
        :type: str
        """

        self._platform_type = platform_type

    @property
    def product_name(self):
        """
        Gets the product_name of this EquipmentChassis.
        This field identifies the Product Name for the chassis enclosure.

        :return: The product_name of this EquipmentChassis.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """
        Sets the product_name of this EquipmentChassis.
        This field identifies the Product Name for the chassis enclosure.

        :param product_name: The product_name of this EquipmentChassis.
        :type: str
        """

        self._product_name = product_name

    @property
    def sku(self):
        """
        Gets the sku of this EquipmentChassis.
        This field identifies the Stock Keeping Unit for the chassis enclosure.

        :return: The sku of this EquipmentChassis.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this EquipmentChassis.
        This field identifies the Stock Keeping Unit for the chassis enclosure.

        :param sku: The sku of this EquipmentChassis.
        :type: str
        """

        self._sku = sku

    @property
    def vid(self):
        """
        Gets the vid of this EquipmentChassis.
        This field identifies the Vendor ID for the chassis enclosure.

        :return: The vid of this EquipmentChassis.
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """
        Sets the vid of this EquipmentChassis.
        This field identifies the Vendor ID for the chassis enclosure.

        :param vid: The vid of this EquipmentChassis.
        :type: str
        """

        self._vid = vid

    @property
    def blades(self):
        """
        Gets the blades of this EquipmentChassis.

        :return: The blades of this EquipmentChassis.
        :rtype: list[ComputeBladeRef]
        """
        return self._blades

    @blades.setter
    def blades(self, blades):
        """
        Sets the blades of this EquipmentChassis.

        :param blades: The blades of this EquipmentChassis.
        :type: list[ComputeBladeRef]
        """

        self._blades = blades

    @property
    def fanmodules(self):
        """
        Gets the fanmodules of this EquipmentChassis.

        :return: The fanmodules of this EquipmentChassis.
        :rtype: list[EquipmentFanModuleRef]
        """
        return self._fanmodules

    @fanmodules.setter
    def fanmodules(self, fanmodules):
        """
        Sets the fanmodules of this EquipmentChassis.

        :param fanmodules: The fanmodules of this EquipmentChassis.
        :type: list[EquipmentFanModuleRef]
        """

        self._fanmodules = fanmodules

    @property
    def ioms(self):
        """
        Gets the ioms of this EquipmentChassis.

        :return: The ioms of this EquipmentChassis.
        :rtype: list[EquipmentIoCardRef]
        """
        return self._ioms

    @ioms.setter
    def ioms(self, ioms):
        """
        Sets the ioms of this EquipmentChassis.

        :param ioms: The ioms of this EquipmentChassis.
        :type: list[EquipmentIoCardRef]
        """

        self._ioms = ioms

    @property
    def psus(self):
        """
        Gets the psus of this EquipmentChassis.

        :return: The psus of this EquipmentChassis.
        :rtype: list[EquipmentPsuRef]
        """
        return self._psus

    @psus.setter
    def psus(self, psus):
        """
        Sets the psus of this EquipmentChassis.

        :param psus: The psus of this EquipmentChassis.
        :type: list[EquipmentPsuRef]
        """

        self._psus = psus

    @property
    def registered_device(self):
        """
        Gets the registered_device of this EquipmentChassis.
        The Device to which this Managed Object is associated.

        :return: The registered_device of this EquipmentChassis.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this EquipmentChassis.
        The Device to which this Managed Object is associated.

        :param registered_device: The registered_device of this EquipmentChassis.
        :type: AssetDeviceRegistrationRef
        """

        self._registered_device = registered_device

    @property
    def sasexpanders(self):
        """
        Gets the sasexpanders of this EquipmentChassis.

        :return: The sasexpanders of this EquipmentChassis.
        :rtype: list[StorageSasExpanderRef]
        """
        return self._sasexpanders

    @sasexpanders.setter
    def sasexpanders(self, sasexpanders):
        """
        Sets the sasexpanders of this EquipmentChassis.

        :param sasexpanders: The sasexpanders of this EquipmentChassis.
        :type: list[StorageSasExpanderRef]
        """

        self._sasexpanders = sasexpanders

    @property
    def siocs(self):
        """
        Gets the siocs of this EquipmentChassis.

        :return: The siocs of this EquipmentChassis.
        :rtype: list[EquipmentSystemIoControllerRef]
        """
        return self._siocs

    @siocs.setter
    def siocs(self, siocs):
        """
        Sets the siocs of this EquipmentChassis.

        :param siocs: The siocs of this EquipmentChassis.
        :type: list[EquipmentSystemIoControllerRef]
        """

        self._siocs = siocs

    @property
    def storage_enclosures(self):
        """
        Gets the storage_enclosures of this EquipmentChassis.
        This field identifies the chassis enclosures.

        :return: The storage_enclosures of this EquipmentChassis.
        :rtype: list[StorageEnclosureRef]
        """
        return self._storage_enclosures

    @storage_enclosures.setter
    def storage_enclosures(self, storage_enclosures):
        """
        Sets the storage_enclosures of this EquipmentChassis.
        This field identifies the chassis enclosures.

        :param storage_enclosures: The storage_enclosures of this EquipmentChassis.
        :type: list[StorageEnclosureRef]
        """

        self._storage_enclosures = storage_enclosures

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
        if not isinstance(other, EquipmentChassis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
