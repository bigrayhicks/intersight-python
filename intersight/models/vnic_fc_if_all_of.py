# coding: utf-8
"""
    Cisco Intersight

    Cisco Intersight is a management platform delivered as a service with embedded analytics for your Cisco and 3rd party IT infrastructure. This platform offers an intelligent level of management that enables IT organizations to analyze, simplify, and automate their environments in more advanced ways than the prior generations of tools. Cisco Intersight provides an integrated and intuitive management experience for resources in the traditional data center as well as at the edge. With flexible deployment options to address complex security needs, getting started with Intersight is quick and easy. Cisco Intersight has deep integration with Cisco UCS and HyperFlex systems allowing for remote deployment, configuration, and ongoing maintenance. The model-based deployment works for a single system in a remote location or hundreds of systems in a data center and enables rapid, standardized configuration and deployment. It also streamlines maintaining those systems whether you are working with small or very large configurations.   # noqa: E501

    The version of the OpenAPI document: 1.0.9-1295
    Contact: intersight@cisco.com
    Generated by: https://openapi-generator.tech
"""

import pprint
import re  # noqa: F401

import six

from intersight.configuration import Configuration


class VnicFcIfAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'order': 'int',
        'persistent_bindings': 'bool',
        'placement': 'VnicPlacementSettings',
        'type': 'str',
        'fc_adapter_policy': 'VnicFcAdapterPolicy',
        'fc_network_policy': 'VnicFcNetworkPolicy',
        'fc_qos_policy': 'VnicFcQosPolicy',
        'organization': 'OrganizationOrganization',
        'san_connectivity_policy': 'VnicSanConnectivityPolicy'
    }

    attribute_map = {
        'name': 'Name',
        'order': 'Order',
        'persistent_bindings': 'PersistentBindings',
        'placement': 'Placement',
        'type': 'Type',
        'fc_adapter_policy': 'FcAdapterPolicy',
        'fc_network_policy': 'FcNetworkPolicy',
        'fc_qos_policy': 'FcQosPolicy',
        'organization': 'Organization',
        'san_connectivity_policy': 'SanConnectivityPolicy'
    }

    def __init__(self,
                 name=None,
                 order=None,
                 persistent_bindings=None,
                 placement=None,
                 type='fc-initiator',
                 fc_adapter_policy=None,
                 fc_network_policy=None,
                 fc_qos_policy=None,
                 organization=None,
                 san_connectivity_policy=None,
                 local_vars_configuration=None):  # noqa: E501
        """VnicFcIfAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._order = None
        self._persistent_bindings = None
        self._placement = None
        self._type = None
        self._fc_adapter_policy = None
        self._fc_network_policy = None
        self._fc_qos_policy = None
        self._organization = None
        self._san_connectivity_policy = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if order is not None:
            self.order = order
        if persistent_bindings is not None:
            self.persistent_bindings = persistent_bindings
        if placement is not None:
            self.placement = placement
        if type is not None:
            self.type = type
        if fc_adapter_policy is not None:
            self.fc_adapter_policy = fc_adapter_policy
        if fc_network_policy is not None:
            self.fc_network_policy = fc_network_policy
        if fc_qos_policy is not None:
            self.fc_qos_policy = fc_qos_policy
        if organization is not None:
            self.organization = organization
        if san_connectivity_policy is not None:
            self.san_connectivity_policy = san_connectivity_policy

    @property
    def name(self):
        """Gets the name of this VnicFcIfAllOf.  # noqa: E501

        Name of the virtual fibre channel interface.    # noqa: E501

        :return: The name of this VnicFcIfAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VnicFcIfAllOf.

        Name of the virtual fibre channel interface.    # noqa: E501

        :param name: The name of this VnicFcIfAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this VnicFcIfAllOf.  # noqa: E501

        The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two.    # noqa: E501

        :return: The order of this VnicFcIfAllOf.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this VnicFcIfAllOf.

        The order in which the virtual interface is brought up. The order assigned to an interface should be unique for all the Ethernet and Fibre-Channel interfaces on each PCI link on a VIC adapter. The maximum value of PCI order is limited by the number of virtual interfaces (Ethernet and Fibre-Channel) on each PCI link on a VIC adapter. All VIC adapters have a single PCI link except VIC 1385 which has two.    # noqa: E501

        :param order: The order of this VnicFcIfAllOf.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def persistent_bindings(self):
        """Gets the persistent_bindings of this VnicFcIfAllOf.  # noqa: E501

        Enables retention of LUN ID associations in memory until they are manually cleared.    # noqa: E501

        :return: The persistent_bindings of this VnicFcIfAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._persistent_bindings

    @persistent_bindings.setter
    def persistent_bindings(self, persistent_bindings):
        """Sets the persistent_bindings of this VnicFcIfAllOf.

        Enables retention of LUN ID associations in memory until they are manually cleared.    # noqa: E501

        :param persistent_bindings: The persistent_bindings of this VnicFcIfAllOf.  # noqa: E501
        :type: bool
        """

        self._persistent_bindings = persistent_bindings

    @property
    def placement(self):
        """Gets the placement of this VnicFcIfAllOf.  # noqa: E501


        :return: The placement of this VnicFcIfAllOf.  # noqa: E501
        :rtype: VnicPlacementSettings
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        """Sets the placement of this VnicFcIfAllOf.


        :param placement: The placement of this VnicFcIfAllOf.  # noqa: E501
        :type: VnicPlacementSettings
        """

        self._placement = placement

    @property
    def type(self):
        """Gets the type of this VnicFcIfAllOf.  # noqa: E501

        VHBA Type configuration for SAN Connectivity Policy. This configuration is supported only on Cisco VIC 14XX series and higher series of adapters.     # noqa: E501

        :return: The type of this VnicFcIfAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VnicFcIfAllOf.

        VHBA Type configuration for SAN Connectivity Policy. This configuration is supported only on Cisco VIC 14XX series and higher series of adapters.     # noqa: E501

        :param type: The type of this VnicFcIfAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "fc-initiator", "fc-nvme-initiator", "fc-nvme-target", "fc-target"
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values))

        self._type = type

    @property
    def fc_adapter_policy(self):
        """Gets the fc_adapter_policy of this VnicFcIfAllOf.  # noqa: E501


        :return: The fc_adapter_policy of this VnicFcIfAllOf.  # noqa: E501
        :rtype: VnicFcAdapterPolicy
        """
        return self._fc_adapter_policy

    @fc_adapter_policy.setter
    def fc_adapter_policy(self, fc_adapter_policy):
        """Sets the fc_adapter_policy of this VnicFcIfAllOf.


        :param fc_adapter_policy: The fc_adapter_policy of this VnicFcIfAllOf.  # noqa: E501
        :type: VnicFcAdapterPolicy
        """

        self._fc_adapter_policy = fc_adapter_policy

    @property
    def fc_network_policy(self):
        """Gets the fc_network_policy of this VnicFcIfAllOf.  # noqa: E501


        :return: The fc_network_policy of this VnicFcIfAllOf.  # noqa: E501
        :rtype: VnicFcNetworkPolicy
        """
        return self._fc_network_policy

    @fc_network_policy.setter
    def fc_network_policy(self, fc_network_policy):
        """Sets the fc_network_policy of this VnicFcIfAllOf.


        :param fc_network_policy: The fc_network_policy of this VnicFcIfAllOf.  # noqa: E501
        :type: VnicFcNetworkPolicy
        """

        self._fc_network_policy = fc_network_policy

    @property
    def fc_qos_policy(self):
        """Gets the fc_qos_policy of this VnicFcIfAllOf.  # noqa: E501


        :return: The fc_qos_policy of this VnicFcIfAllOf.  # noqa: E501
        :rtype: VnicFcQosPolicy
        """
        return self._fc_qos_policy

    @fc_qos_policy.setter
    def fc_qos_policy(self, fc_qos_policy):
        """Sets the fc_qos_policy of this VnicFcIfAllOf.


        :param fc_qos_policy: The fc_qos_policy of this VnicFcIfAllOf.  # noqa: E501
        :type: VnicFcQosPolicy
        """

        self._fc_qos_policy = fc_qos_policy

    @property
    def organization(self):
        """Gets the organization of this VnicFcIfAllOf.  # noqa: E501


        :return: The organization of this VnicFcIfAllOf.  # noqa: E501
        :rtype: OrganizationOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this VnicFcIfAllOf.


        :param organization: The organization of this VnicFcIfAllOf.  # noqa: E501
        :type: OrganizationOrganization
        """

        self._organization = organization

    @property
    def san_connectivity_policy(self):
        """Gets the san_connectivity_policy of this VnicFcIfAllOf.  # noqa: E501


        :return: The san_connectivity_policy of this VnicFcIfAllOf.  # noqa: E501
        :rtype: VnicSanConnectivityPolicy
        """
        return self._san_connectivity_policy

    @san_connectivity_policy.setter
    def san_connectivity_policy(self, san_connectivity_policy):
        """Sets the san_connectivity_policy of this VnicFcIfAllOf.


        :param san_connectivity_policy: The san_connectivity_policy of this VnicFcIfAllOf.  # noqa: E501
        :type: VnicSanConnectivityPolicy
        """

        self._san_connectivity_policy = san_connectivity_policy

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict()
                        if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VnicFcIfAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VnicFcIfAllOf):
            return True

        return self.to_dict() != other.to_dict()
