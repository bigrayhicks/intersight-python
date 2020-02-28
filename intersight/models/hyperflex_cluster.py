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


class HyperflexCluster(object):
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
        'capacity_runway': 'int',
        'cluster_name': 'str',
        'cluster_type': 'int',
        'cluster_uuid': 'str',
        'compute_node_count': 'int',
        'converged_node_count': 'int',
        'deployment_type': 'str',
        'device_id': 'str',
        'flt_aggr': 'int',
        'hx_version': 'str',
        'hxdp_build_version': 'str',
        'hypervisor_type': 'str',
        'hypervisor_version': 'str',
        'summary': 'HyperflexSummary',
        'utilization_percentage': 'float',
        'utilization_trend_percentage': 'float',
        'vm_count': 'int',
        'alarm': 'list[HyperflexAlarmRef]',
        'health': 'HyperflexHealthRef',
        'nodes': 'list[HyperflexNodeRef]',
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
        'capacity_runway': 'CapacityRunway',
        'cluster_name': 'ClusterName',
        'cluster_type': 'ClusterType',
        'cluster_uuid': 'ClusterUuid',
        'compute_node_count': 'ComputeNodeCount',
        'converged_node_count': 'ConvergedNodeCount',
        'deployment_type': 'DeploymentType',
        'device_id': 'DeviceId',
        'flt_aggr': 'FltAggr',
        'hx_version': 'HxVersion',
        'hxdp_build_version': 'HxdpBuildVersion',
        'hypervisor_type': 'HypervisorType',
        'hypervisor_version': 'HypervisorVersion',
        'summary': 'Summary',
        'utilization_percentage': 'UtilizationPercentage',
        'utilization_trend_percentage': 'UtilizationTrendPercentage',
        'vm_count': 'VmCount',
        'alarm': 'Alarm',
        'health': 'Health',
        'nodes': 'Nodes',
        'registered_device': 'RegisteredDevice'
    }

    def __init__(self, account_moid=None, create_time=None, domain_group_moid=None, mod_time=None, moid=None, object_type=None, owners=None, shared_scope=None, tags=None, version_context=None, ancestors=None, parent=None, permission_resources=None, capacity_runway=None, cluster_name=None, cluster_type=None, cluster_uuid=None, compute_node_count=None, converged_node_count=None, deployment_type='NA', device_id=None, flt_aggr=None, hx_version=None, hxdp_build_version=None, hypervisor_type='ESXi', hypervisor_version=None, summary=None, utilization_percentage=None, utilization_trend_percentage=None, vm_count=None, alarm=None, health=None, nodes=None, registered_device=None):
        """
        HyperflexCluster - a model defined in Swagger
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
        self._capacity_runway = None
        self._cluster_name = None
        self._cluster_type = None
        self._cluster_uuid = None
        self._compute_node_count = None
        self._converged_node_count = None
        self._deployment_type = None
        self._device_id = None
        self._flt_aggr = None
        self._hx_version = None
        self._hxdp_build_version = None
        self._hypervisor_type = None
        self._hypervisor_version = None
        self._summary = None
        self._utilization_percentage = None
        self._utilization_trend_percentage = None
        self._vm_count = None
        self._alarm = None
        self._health = None
        self._nodes = None
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
        if capacity_runway is not None:
          self.capacity_runway = capacity_runway
        if cluster_name is not None:
          self.cluster_name = cluster_name
        if cluster_type is not None:
          self.cluster_type = cluster_type
        if cluster_uuid is not None:
          self.cluster_uuid = cluster_uuid
        if compute_node_count is not None:
          self.compute_node_count = compute_node_count
        if converged_node_count is not None:
          self.converged_node_count = converged_node_count
        if deployment_type is not None:
          self.deployment_type = deployment_type
        if device_id is not None:
          self.device_id = device_id
        if flt_aggr is not None:
          self.flt_aggr = flt_aggr
        if hx_version is not None:
          self.hx_version = hx_version
        if hxdp_build_version is not None:
          self.hxdp_build_version = hxdp_build_version
        if hypervisor_type is not None:
          self.hypervisor_type = hypervisor_type
        if hypervisor_version is not None:
          self.hypervisor_version = hypervisor_version
        if summary is not None:
          self.summary = summary
        if utilization_percentage is not None:
          self.utilization_percentage = utilization_percentage
        if utilization_trend_percentage is not None:
          self.utilization_trend_percentage = utilization_trend_percentage
        if vm_count is not None:
          self.vm_count = vm_count
        if alarm is not None:
          self.alarm = alarm
        if health is not None:
          self.health = health
        if nodes is not None:
          self.nodes = nodes
        if registered_device is not None:
          self.registered_device = registered_device

    @property
    def account_moid(self):
        """
        Gets the account_moid of this HyperflexCluster.
        The Account ID for this managed object.

        :return: The account_moid of this HyperflexCluster.
        :rtype: str
        """
        return self._account_moid

    @account_moid.setter
    def account_moid(self, account_moid):
        """
        Sets the account_moid of this HyperflexCluster.
        The Account ID for this managed object.

        :param account_moid: The account_moid of this HyperflexCluster.
        :type: str
        """

        self._account_moid = account_moid

    @property
    def create_time(self):
        """
        Gets the create_time of this HyperflexCluster.
        The time when this managed object was created.

        :return: The create_time of this HyperflexCluster.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this HyperflexCluster.
        The time when this managed object was created.

        :param create_time: The create_time of this HyperflexCluster.
        :type: datetime
        """

        self._create_time = create_time

    @property
    def domain_group_moid(self):
        """
        Gets the domain_group_moid of this HyperflexCluster.
        The DomainGroup ID for this managed object.

        :return: The domain_group_moid of this HyperflexCluster.
        :rtype: str
        """
        return self._domain_group_moid

    @domain_group_moid.setter
    def domain_group_moid(self, domain_group_moid):
        """
        Sets the domain_group_moid of this HyperflexCluster.
        The DomainGroup ID for this managed object.

        :param domain_group_moid: The domain_group_moid of this HyperflexCluster.
        :type: str
        """

        self._domain_group_moid = domain_group_moid

    @property
    def mod_time(self):
        """
        Gets the mod_time of this HyperflexCluster.
        The time when this managed object was last modified.

        :return: The mod_time of this HyperflexCluster.
        :rtype: datetime
        """
        return self._mod_time

    @mod_time.setter
    def mod_time(self, mod_time):
        """
        Sets the mod_time of this HyperflexCluster.
        The time when this managed object was last modified.

        :param mod_time: The mod_time of this HyperflexCluster.
        :type: datetime
        """

        self._mod_time = mod_time

    @property
    def moid(self):
        """
        Gets the moid of this HyperflexCluster.
        The unique identifier of this Managed Object instance.

        :return: The moid of this HyperflexCluster.
        :rtype: str
        """
        return self._moid

    @moid.setter
    def moid(self, moid):
        """
        Sets the moid of this HyperflexCluster.
        The unique identifier of this Managed Object instance.

        :param moid: The moid of this HyperflexCluster.
        :type: str
        """

        self._moid = moid

    @property
    def object_type(self):
        """
        Gets the object_type of this HyperflexCluster.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :return: The object_type of this HyperflexCluster.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """
        Sets the object_type of this HyperflexCluster.
        The fully-qualified type of this managed object, i.e. the class name. This property is optional. The ObjectType is implied from the URL path. If specified, the value of objectType must match the class name specified in the URL path.

        :param object_type: The object_type of this HyperflexCluster.
        :type: str
        """

        self._object_type = object_type

    @property
    def owners(self):
        """
        Gets the owners of this HyperflexCluster.
        The array of owners which represent effective ownership of this object.

        :return: The owners of this HyperflexCluster.
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """
        Sets the owners of this HyperflexCluster.
        The array of owners which represent effective ownership of this object.

        :param owners: The owners of this HyperflexCluster.
        :type: list[str]
        """

        self._owners = owners

    @property
    def shared_scope(self):
        """
        Gets the shared_scope of this HyperflexCluster.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :return: The shared_scope of this HyperflexCluster.
        :rtype: str
        """
        return self._shared_scope

    @shared_scope.setter
    def shared_scope(self, shared_scope):
        """
        Sets the shared_scope of this HyperflexCluster.
        Intersight provides pre-built workflows, tasks and policies to end users through global catalogs. Objects that are made available through global catalogs are said to have a 'shared' ownership. Shared objects are either made globally available to all end users or restricted to end users based on their license entitlement. Users can use this property to differentiate the scope (global or a specific license tier) to which a shared MO belongs.

        :param shared_scope: The shared_scope of this HyperflexCluster.
        :type: str
        """

        self._shared_scope = shared_scope

    @property
    def tags(self):
        """
        Gets the tags of this HyperflexCluster.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :return: The tags of this HyperflexCluster.
        :rtype: list[MoTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this HyperflexCluster.
        The array of tags, which allow to add key, value meta-data to managed objects.

        :param tags: The tags of this HyperflexCluster.
        :type: list[MoTag]
        """

        self._tags = tags

    @property
    def version_context(self):
        """
        Gets the version_context of this HyperflexCluster.
        The versioning info for this managed object.

        :return: The version_context of this HyperflexCluster.
        :rtype: MoVersionContext
        """
        return self._version_context

    @version_context.setter
    def version_context(self, version_context):
        """
        Sets the version_context of this HyperflexCluster.
        The versioning info for this managed object.

        :param version_context: The version_context of this HyperflexCluster.
        :type: MoVersionContext
        """

        self._version_context = version_context

    @property
    def ancestors(self):
        """
        Gets the ancestors of this HyperflexCluster.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :return: The ancestors of this HyperflexCluster.
        :rtype: list[MoBaseMoRef]
        """
        return self._ancestors

    @ancestors.setter
    def ancestors(self, ancestors):
        """
        Sets the ancestors of this HyperflexCluster.
        The array containing the MO references of the ancestors in the object containment hierarchy.

        :param ancestors: The ancestors of this HyperflexCluster.
        :type: list[MoBaseMoRef]
        """

        self._ancestors = ancestors

    @property
    def parent(self):
        """
        Gets the parent of this HyperflexCluster.
        The direct ancestor of this managed object in the containment hierarchy.

        :return: The parent of this HyperflexCluster.
        :rtype: MoBaseMoRef
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """
        Sets the parent of this HyperflexCluster.
        The direct ancestor of this managed object in the containment hierarchy.

        :param parent: The parent of this HyperflexCluster.
        :type: MoBaseMoRef
        """

        self._parent = parent

    @property
    def permission_resources(self):
        """
        Gets the permission_resources of this HyperflexCluster.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :return: The permission_resources of this HyperflexCluster.
        :rtype: list[MoBaseMoRef]
        """
        return self._permission_resources

    @permission_resources.setter
    def permission_resources(self, permission_resources):
        """
        Sets the permission_resources of this HyperflexCluster.
        A slice of all permission resources (organizations) associated with this object. Permission ties resources and its associated roles/privileges. These resources which can be specified in a permission is PermissionResource. Currently only organizations can be specified in permission. All logical and physical resources part of an organization will have organization in PermissionResources field. If DeviceRegistration contains another DeviceRegistration and if parent is in org1 and child is part of org2, then child objects will have PermissionResources as org1 and org2. Parent Objects will have PermissionResources as org1. All profiles/policies created with in an organization will have the organization as PermissionResources.

        :param permission_resources: The permission_resources of this HyperflexCluster.
        :type: list[MoBaseMoRef]
        """

        self._permission_resources = permission_resources

    @property
    def capacity_runway(self):
        """
        Gets the capacity_runway of this HyperflexCluster.
        The number of days remaining before the cluster's storage utilization reaches the recommended capacity limit of 76%. Default value is math.MaxInt32 to indicate that the capacity runway is \"Unknown\" for a cluster that is not connected or with not sufficient data.

        :return: The capacity_runway of this HyperflexCluster.
        :rtype: int
        """
        return self._capacity_runway

    @capacity_runway.setter
    def capacity_runway(self, capacity_runway):
        """
        Sets the capacity_runway of this HyperflexCluster.
        The number of days remaining before the cluster's storage utilization reaches the recommended capacity limit of 76%. Default value is math.MaxInt32 to indicate that the capacity runway is \"Unknown\" for a cluster that is not connected or with not sufficient data.

        :param capacity_runway: The capacity_runway of this HyperflexCluster.
        :type: int
        """

        self._capacity_runway = capacity_runway

    @property
    def cluster_name(self):
        """
        Gets the cluster_name of this HyperflexCluster.
        The name of this HyperFlex cluster.

        :return: The cluster_name of this HyperflexCluster.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """
        Sets the cluster_name of this HyperflexCluster.
        The name of this HyperFlex cluster.

        :param cluster_name: The cluster_name of this HyperflexCluster.
        :type: str
        """

        self._cluster_name = cluster_name

    @property
    def cluster_type(self):
        """
        Gets the cluster_type of this HyperflexCluster.
        The storage type of this cluster (All Flash or Hybrid).

        :return: The cluster_type of this HyperflexCluster.
        :rtype: int
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """
        Sets the cluster_type of this HyperflexCluster.
        The storage type of this cluster (All Flash or Hybrid).

        :param cluster_type: The cluster_type of this HyperflexCluster.
        :type: int
        """

        self._cluster_type = cluster_type

    @property
    def cluster_uuid(self):
        """
        Gets the cluster_uuid of this HyperflexCluster.
        The unique identifier for this HyperFlex cluster.

        :return: The cluster_uuid of this HyperflexCluster.
        :rtype: str
        """
        return self._cluster_uuid

    @cluster_uuid.setter
    def cluster_uuid(self, cluster_uuid):
        """
        Sets the cluster_uuid of this HyperflexCluster.
        The unique identifier for this HyperFlex cluster.

        :param cluster_uuid: The cluster_uuid of this HyperflexCluster.
        :type: str
        """

        self._cluster_uuid = cluster_uuid

    @property
    def compute_node_count(self):
        """
        Gets the compute_node_count of this HyperflexCluster.
        The number of compute nodes that belong to this cluster.

        :return: The compute_node_count of this HyperflexCluster.
        :rtype: int
        """
        return self._compute_node_count

    @compute_node_count.setter
    def compute_node_count(self, compute_node_count):
        """
        Sets the compute_node_count of this HyperflexCluster.
        The number of compute nodes that belong to this cluster.

        :param compute_node_count: The compute_node_count of this HyperflexCluster.
        :type: int
        """

        self._compute_node_count = compute_node_count

    @property
    def converged_node_count(self):
        """
        Gets the converged_node_count of this HyperflexCluster.
        The number of converged nodes that belong to this cluster.

        :return: The converged_node_count of this HyperflexCluster.
        :rtype: int
        """
        return self._converged_node_count

    @converged_node_count.setter
    def converged_node_count(self, converged_node_count):
        """
        Sets the converged_node_count of this HyperflexCluster.
        The number of converged nodes that belong to this cluster.

        :param converged_node_count: The converged_node_count of this HyperflexCluster.
        :type: int
        """

        self._converged_node_count = converged_node_count

    @property
    def deployment_type(self):
        """
        Gets the deployment_type of this HyperflexCluster.
        The deployment type of the HyperFlex cluster. The cluster can have one of the following configurations: 1. Datacenter: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes on a single site. 2. Stretched Cluster: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes distributed across multiple sites. 3. Edge: The HyperFlex cluster consists of 2-4 standalone nodes. If the cluster is running a HyperFlex Data Platform version less than 4.0 or if the deployment type cannot be determined, the deployment type is set as 'NA' (not available).

        :return: The deployment_type of this HyperflexCluster.
        :rtype: str
        """
        return self._deployment_type

    @deployment_type.setter
    def deployment_type(self, deployment_type):
        """
        Sets the deployment_type of this HyperflexCluster.
        The deployment type of the HyperFlex cluster. The cluster can have one of the following configurations: 1. Datacenter: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes on a single site. 2. Stretched Cluster: The HyperFlex cluster consists of UCS Fabric Interconnect-attached nodes distributed across multiple sites. 3. Edge: The HyperFlex cluster consists of 2-4 standalone nodes. If the cluster is running a HyperFlex Data Platform version less than 4.0 or if the deployment type cannot be determined, the deployment type is set as 'NA' (not available).

        :param deployment_type: The deployment_type of this HyperflexCluster.
        :type: str
        """
        allowed_values = ["NA", "Datacenter", "Stretched Cluster", "Edge"]
        if deployment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_type` ({0}), must be one of {1}"
                .format(deployment_type, allowed_values)
            )

        self._deployment_type = deployment_type

    @property
    def device_id(self):
        """
        Gets the device_id of this HyperflexCluster.
        The unique identifier of the device registration that represents this HyperFlex cluster's connection to Intersight.

        :return: The device_id of this HyperflexCluster.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this HyperflexCluster.
        The unique identifier of the device registration that represents this HyperFlex cluster's connection to Intersight.

        :param device_id: The device_id of this HyperflexCluster.
        :type: str
        """

        self._device_id = device_id

    @property
    def flt_aggr(self):
        """
        Gets the flt_aggr of this HyperflexCluster.
        The number of yellow (warning) and red (critical) alarms stored as an aggregate. The first 16 bits indicate the number of red alarms, and the last 16 bits contain the number of yellow alarms.

        :return: The flt_aggr of this HyperflexCluster.
        :rtype: int
        """
        return self._flt_aggr

    @flt_aggr.setter
    def flt_aggr(self, flt_aggr):
        """
        Sets the flt_aggr of this HyperflexCluster.
        The number of yellow (warning) and red (critical) alarms stored as an aggregate. The first 16 bits indicate the number of red alarms, and the last 16 bits contain the number of yellow alarms.

        :param flt_aggr: The flt_aggr of this HyperflexCluster.
        :type: int
        """

        self._flt_aggr = flt_aggr

    @property
    def hx_version(self):
        """
        Gets the hx_version of this HyperflexCluster.
        The HyperFlex Data Platform version of this cluster.

        :return: The hx_version of this HyperflexCluster.
        :rtype: str
        """
        return self._hx_version

    @hx_version.setter
    def hx_version(self, hx_version):
        """
        Sets the hx_version of this HyperflexCluster.
        The HyperFlex Data Platform version of this cluster.

        :param hx_version: The hx_version of this HyperflexCluster.
        :type: str
        """

        self._hx_version = hx_version

    @property
    def hxdp_build_version(self):
        """
        Gets the hxdp_build_version of this HyperflexCluster.
        The version and build number of the HyperFlex Data Platform for this cluster. After a cluster upgrade, this version string will be updated on the next inventory cycle to reflect the newly installed version.

        :return: The hxdp_build_version of this HyperflexCluster.
        :rtype: str
        """
        return self._hxdp_build_version

    @hxdp_build_version.setter
    def hxdp_build_version(self, hxdp_build_version):
        """
        Sets the hxdp_build_version of this HyperflexCluster.
        The version and build number of the HyperFlex Data Platform for this cluster. After a cluster upgrade, this version string will be updated on the next inventory cycle to reflect the newly installed version.

        :param hxdp_build_version: The hxdp_build_version of this HyperflexCluster.
        :type: str
        """

        self._hxdp_build_version = hxdp_build_version

    @property
    def hypervisor_type(self):
        """
        Gets the hypervisor_type of this HyperflexCluster.
        The type of hypervisor running on this cluster.

        :return: The hypervisor_type of this HyperflexCluster.
        :rtype: str
        """
        return self._hypervisor_type

    @hypervisor_type.setter
    def hypervisor_type(self, hypervisor_type):
        """
        Sets the hypervisor_type of this HyperflexCluster.
        The type of hypervisor running on this cluster.

        :param hypervisor_type: The hypervisor_type of this HyperflexCluster.
        :type: str
        """
        allowed_values = ["ESXi"]
        if hypervisor_type not in allowed_values:
            raise ValueError(
                "Invalid value for `hypervisor_type` ({0}), must be one of {1}"
                .format(hypervisor_type, allowed_values)
            )

        self._hypervisor_type = hypervisor_type

    @property
    def hypervisor_version(self):
        """
        Gets the hypervisor_version of this HyperflexCluster.
        The version of hypervisor running on this cluster.

        :return: The hypervisor_version of this HyperflexCluster.
        :rtype: str
        """
        return self._hypervisor_version

    @hypervisor_version.setter
    def hypervisor_version(self, hypervisor_version):
        """
        Sets the hypervisor_version of this HyperflexCluster.
        The version of hypervisor running on this cluster.

        :param hypervisor_version: The hypervisor_version of this HyperflexCluster.
        :type: str
        """

        self._hypervisor_version = hypervisor_version

    @property
    def summary(self):
        """
        Gets the summary of this HyperflexCluster.
        The summary of HyperFlex cluster health, storage, and number of nodes.

        :return: The summary of this HyperflexCluster.
        :rtype: HyperflexSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this HyperflexCluster.
        The summary of HyperFlex cluster health, storage, and number of nodes.

        :param summary: The summary of this HyperflexCluster.
        :type: HyperflexSummary
        """

        self._summary = summary

    @property
    def utilization_percentage(self):
        """
        Gets the utilization_percentage of this HyperflexCluster.
        The storage utilization percentage is computed based on total capacity and current capacity utilization.

        :return: The utilization_percentage of this HyperflexCluster.
        :rtype: float
        """
        return self._utilization_percentage

    @utilization_percentage.setter
    def utilization_percentage(self, utilization_percentage):
        """
        Sets the utilization_percentage of this HyperflexCluster.
        The storage utilization percentage is computed based on total capacity and current capacity utilization.

        :param utilization_percentage: The utilization_percentage of this HyperflexCluster.
        :type: float
        """

        self._utilization_percentage = utilization_percentage

    @property
    def utilization_trend_percentage(self):
        """
        Gets the utilization_trend_percentage of this HyperflexCluster.
        The storage utilization trend percentage represents the trend in percentage computed using the first and last point from historical data.

        :return: The utilization_trend_percentage of this HyperflexCluster.
        :rtype: float
        """
        return self._utilization_trend_percentage

    @utilization_trend_percentage.setter
    def utilization_trend_percentage(self, utilization_trend_percentage):
        """
        Sets the utilization_trend_percentage of this HyperflexCluster.
        The storage utilization trend percentage represents the trend in percentage computed using the first and last point from historical data.

        :param utilization_trend_percentage: The utilization_trend_percentage of this HyperflexCluster.
        :type: float
        """

        self._utilization_trend_percentage = utilization_trend_percentage

    @property
    def vm_count(self):
        """
        Gets the vm_count of this HyperflexCluster.
        The number of virtual machines present on this cluster.

        :return: The vm_count of this HyperflexCluster.
        :rtype: int
        """
        return self._vm_count

    @vm_count.setter
    def vm_count(self, vm_count):
        """
        Sets the vm_count of this HyperflexCluster.
        The number of virtual machines present on this cluster.

        :param vm_count: The vm_count of this HyperflexCluster.
        :type: int
        """

        self._vm_count = vm_count

    @property
    def alarm(self):
        """
        Gets the alarm of this HyperflexCluster.
        The alarms that have been raised for this HyperFlex cluster. New alarms are added to this collection, and existing alarms are updated if the severity changes. Deleted alarms are not removed but are cleared by marking them as green.

        :return: The alarm of this HyperflexCluster.
        :rtype: list[HyperflexAlarmRef]
        """
        return self._alarm

    @alarm.setter
    def alarm(self, alarm):
        """
        Sets the alarm of this HyperflexCluster.
        The alarms that have been raised for this HyperFlex cluster. New alarms are added to this collection, and existing alarms are updated if the severity changes. Deleted alarms are not removed but are cleared by marking them as green.

        :param alarm: The alarm of this HyperflexCluster.
        :type: list[HyperflexAlarmRef]
        """

        self._alarm = alarm

    @property
    def health(self):
        """
        Gets the health of this HyperflexCluster.
        The health of the HyperFlex cluster. Detailed information concerning the cluster health, which includes cluster operational status, resiliency health status, number of node and disk failues tolerable, and the status of services such as the ZooKeeper ensemble and arbitration service. This relationship is only populated for devices with HyperFlex Data Platform 3.0+. For clusters running an older version, refer to the Summary property of the hyperflex/Clusters API.

        :return: The health of this HyperflexCluster.
        :rtype: HyperflexHealthRef
        """
        return self._health

    @health.setter
    def health(self, health):
        """
        Sets the health of this HyperflexCluster.
        The health of the HyperFlex cluster. Detailed information concerning the cluster health, which includes cluster operational status, resiliency health status, number of node and disk failues tolerable, and the status of services such as the ZooKeeper ensemble and arbitration service. This relationship is only populated for devices with HyperFlex Data Platform 3.0+. For clusters running an older version, refer to the Summary property of the hyperflex/Clusters API.

        :param health: The health of this HyperflexCluster.
        :type: HyperflexHealthRef
        """

        self._health = health

    @property
    def nodes(self):
        """
        Gets the nodes of this HyperflexCluster.
        The nodes belonging to this HyperFlex cluster. The node object contains inventory information about a specific HyperFlex node, such as host IP address, hypervisor type and version, and operational status.

        :return: The nodes of this HyperflexCluster.
        :rtype: list[HyperflexNodeRef]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this HyperflexCluster.
        The nodes belonging to this HyperFlex cluster. The node object contains inventory information about a specific HyperFlex node, such as host IP address, hypervisor type and version, and operational status.

        :param nodes: The nodes of this HyperflexCluster.
        :type: list[HyperflexNodeRef]
        """

        self._nodes = nodes

    @property
    def registered_device(self):
        """
        Gets the registered_device of this HyperflexCluster.
        The registration that represents this HyperFlex cluster's connection to Intersight.

        :return: The registered_device of this HyperflexCluster.
        :rtype: AssetDeviceRegistrationRef
        """
        return self._registered_device

    @registered_device.setter
    def registered_device(self, registered_device):
        """
        Sets the registered_device of this HyperflexCluster.
        The registration that represents this HyperFlex cluster's connection to Intersight.

        :param registered_device: The registered_device of this HyperflexCluster.
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
        if not isinstance(other, HyperflexCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
