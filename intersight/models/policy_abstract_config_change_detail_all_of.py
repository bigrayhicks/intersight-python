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


class PolicyAbstractConfigChangeDetailAllOf(object):
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
        'changes': 'list[str]',
        'config_change_context': 'PolicyConfigResultContext',
        'config_change_flag': 'str',
        'disruptions': 'list[str]',
        'message': 'str',
        'mod_status': 'str'
    }

    attribute_map = {
        'changes': 'Changes',
        'config_change_context': 'ConfigChangeContext',
        'config_change_flag': 'ConfigChangeFlag',
        'disruptions': 'Disruptions',
        'message': 'Message',
        'mod_status': 'ModStatus'
    }

    def __init__(self,
                 changes=None,
                 config_change_context=None,
                 config_change_flag='Pending-changes',
                 disruptions=None,
                 message=None,
                 mod_status='None',
                 local_vars_configuration=None):  # noqa: E501
        """PolicyAbstractConfigChangeDetailAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._changes = None
        self._config_change_context = None
        self._config_change_flag = None
        self._disruptions = None
        self._message = None
        self._mod_status = None
        self.discriminator = None

        if changes is not None:
            self.changes = changes
        if config_change_context is not None:
            self.config_change_context = config_change_context
        if config_change_flag is not None:
            self.config_change_flag = config_change_flag
        if disruptions is not None:
            self.disruptions = disruptions
        self.message = message
        if mod_status is not None:
            self.mod_status = mod_status

    @property
    def changes(self):
        """Gets the changes of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501


        :return: The changes of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this PolicyAbstractConfigChangeDetailAllOf.


        :param changes: The changes of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :type: list[str]
        """

        self._changes = changes

    @property
    def config_change_context(self):
        """Gets the config_change_context of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501


        :return: The config_change_context of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :rtype: PolicyConfigResultContext
        """
        return self._config_change_context

    @config_change_context.setter
    def config_change_context(self, config_change_context):
        """Sets the config_change_context of this PolicyAbstractConfigChangeDetailAllOf.


        :param config_change_context: The config_change_context of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :type: PolicyConfigResultContext
        """

        self._config_change_context = config_change_context

    @property
    def config_change_flag(self):
        """Gets the config_change_flag of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501

        Config change flag to differentiate Pending-changes and Config-drift.    # noqa: E501

        :return: The config_change_flag of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._config_change_flag

    @config_change_flag.setter
    def config_change_flag(self, config_change_flag):
        """Sets the config_change_flag of this PolicyAbstractConfigChangeDetailAllOf.

        Config change flag to differentiate Pending-changes and Config-drift.    # noqa: E501

        :param config_change_flag: The config_change_flag of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["Pending-changes", "Drift-changes"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and config_change_flag not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `config_change_flag` ({0}), must be one of {1}"  # noqa: E501
                .format(config_change_flag, allowed_values))

        self._config_change_flag = config_change_flag

    @property
    def disruptions(self):
        """Gets the disruptions of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501


        :return: The disruptions of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._disruptions

    @disruptions.setter
    def disruptions(self, disruptions):
        """Sets the disruptions of this PolicyAbstractConfigChangeDetailAllOf.


        :param disruptions: The disruptions of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :type: list[str]
        """

        self._disruptions = disruptions

    @property
    def message(self):
        """Gets the message of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501

        Detailed description of the config change.    # noqa: E501

        :return: The message of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PolicyAbstractConfigChangeDetailAllOf.

        Detailed description of the config change.    # noqa: E501

        :param message: The message of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def mod_status(self):
        """Gets the mod_status of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501

        Modification status of the mo in this config change.     # noqa: E501

        :return: The mod_status of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :rtype: str
        """
        return self._mod_status

    @mod_status.setter
    def mod_status(self, mod_status):
        """Sets the mod_status of this PolicyAbstractConfigChangeDetailAllOf.

        Modification status of the mo in this config change.     # noqa: E501

        :param mod_status: The mod_status of this PolicyAbstractConfigChangeDetailAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "Created", "Modified",
                          "Deleted"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mod_status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mod_status` ({0}), must be one of {1}"  # noqa: E501
                .format(mod_status, allowed_values))

        self._mod_status = mod_status

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
        if not isinstance(other, PolicyAbstractConfigChangeDetailAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyAbstractConfigChangeDetailAllOf):
            return True

        return self.to_dict() != other.to_dict()
