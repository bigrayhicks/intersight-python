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


class VmediaMapping(object):
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
        'authentication_protocol': 'str',
        'device_type': 'str',
        'host_name': 'str',
        'is_password_set': 'bool',
        'mount_options': 'str',
        'mount_protocol': 'str',
        'password': 'str',
        'remote_file': 'str',
        'remote_path': 'str',
        'username': 'str',
        'volume_name': 'str'
    }

    attribute_map = {
        'authentication_protocol': 'AuthenticationProtocol',
        'device_type': 'DeviceType',
        'host_name': 'HostName',
        'is_password_set': 'IsPasswordSet',
        'mount_options': 'MountOptions',
        'mount_protocol': 'MountProtocol',
        'password': 'Password',
        'remote_file': 'RemoteFile',
        'remote_path': 'RemotePath',
        'username': 'Username',
        'volume_name': 'VolumeName'
    }

    def __init__(self, authentication_protocol='none', device_type='cdd', host_name=None, is_password_set=None, mount_options=None, mount_protocol='nfs', password=None, remote_file=None, remote_path=None, username=None, volume_name=None):
        """
        VmediaMapping - a model defined in Swagger
        """

        self._authentication_protocol = None
        self._device_type = None
        self._host_name = None
        self._is_password_set = None
        self._mount_options = None
        self._mount_protocol = None
        self._password = None
        self._remote_file = None
        self._remote_path = None
        self._username = None
        self._volume_name = None

        if authentication_protocol is not None:
          self.authentication_protocol = authentication_protocol
        if device_type is not None:
          self.device_type = device_type
        if host_name is not None:
          self.host_name = host_name
        if is_password_set is not None:
          self.is_password_set = is_password_set
        if mount_options is not None:
          self.mount_options = mount_options
        if mount_protocol is not None:
          self.mount_protocol = mount_protocol
        if password is not None:
          self.password = password
        if remote_file is not None:
          self.remote_file = remote_file
        if remote_path is not None:
          self.remote_path = remote_path
        if username is not None:
          self.username = username
        if volume_name is not None:
          self.volume_name = volume_name

    @property
    def authentication_protocol(self):
        """
        Gets the authentication_protocol of this VmediaMapping.
        Type of Authentication protocol when CIFS is used for communication with the remote server  

        :return: The authentication_protocol of this VmediaMapping.
        :rtype: str
        """
        return self._authentication_protocol

    @authentication_protocol.setter
    def authentication_protocol(self, authentication_protocol):
        """
        Sets the authentication_protocol of this VmediaMapping.
        Type of Authentication protocol when CIFS is used for communication with the remote server  

        :param authentication_protocol: The authentication_protocol of this VmediaMapping.
        :type: str
        """
        allowed_values = ["none", "ntlm", "ntlmi", "ntlmv2", "ntlmv2i", "ntlmssp", "ntlmsspi"]
        if authentication_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `authentication_protocol` ({0}), must be one of {1}"
                .format(authentication_protocol, allowed_values)
            )

        self._authentication_protocol = authentication_protocol

    @property
    def device_type(self):
        """
        Gets the device_type of this VmediaMapping.
        Type of remote Virtual Media device  

        :return: The device_type of this VmediaMapping.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """
        Sets the device_type of this VmediaMapping.
        Type of remote Virtual Media device  

        :param device_type: The device_type of this VmediaMapping.
        :type: str
        """
        allowed_values = ["cdd", "hdd"]
        if device_type not in allowed_values:
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def host_name(self):
        """
        Gets the host_name of this VmediaMapping.
        IP address or hostname of the remote server  

        :return: The host_name of this VmediaMapping.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this VmediaMapping.
        IP address or hostname of the remote server  

        :param host_name: The host_name of this VmediaMapping.
        :type: str
        """

        self._host_name = host_name

    @property
    def is_password_set(self):
        """
        Gets the is_password_set of this VmediaMapping.

        :return: The is_password_set of this VmediaMapping.
        :rtype: bool
        """
        return self._is_password_set

    @is_password_set.setter
    def is_password_set(self, is_password_set):
        """
        Sets the is_password_set of this VmediaMapping.

        :param is_password_set: The is_password_set of this VmediaMapping.
        :type: bool
        """

        self._is_password_set = is_password_set

    @property
    def mount_options(self):
        """
        Gets the mount_options of this VmediaMapping.
        Mount options for the Virtual Media mapping. The field can be left blank or filled in a comma separated list with the following options.\\n For NFS, supported options are ro, rw, nolock, noexec, soft, port=VALUE, timeo=VALUE, retry=VALUE.\\n For CIFS, supported options are soft, nounix, noserverino, guest.\\n For HTTP/HTTPS, the only supported option is noauto.  

        :return: The mount_options of this VmediaMapping.
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """
        Sets the mount_options of this VmediaMapping.
        Mount options for the Virtual Media mapping. The field can be left blank or filled in a comma separated list with the following options.\\n For NFS, supported options are ro, rw, nolock, noexec, soft, port=VALUE, timeo=VALUE, retry=VALUE.\\n For CIFS, supported options are soft, nounix, noserverino, guest.\\n For HTTP/HTTPS, the only supported option is noauto.  

        :param mount_options: The mount_options of this VmediaMapping.
        :type: str
        """

        self._mount_options = mount_options

    @property
    def mount_protocol(self):
        """
        Gets the mount_protocol of this VmediaMapping.
        Protocol to use to communicate with the remote server  

        :return: The mount_protocol of this VmediaMapping.
        :rtype: str
        """
        return self._mount_protocol

    @mount_protocol.setter
    def mount_protocol(self, mount_protocol):
        """
        Sets the mount_protocol of this VmediaMapping.
        Protocol to use to communicate with the remote server  

        :param mount_protocol: The mount_protocol of this VmediaMapping.
        :type: str
        """
        allowed_values = ["nfs", "cifs", "http", "https"]
        if mount_protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `mount_protocol` ({0}), must be one of {1}"
                .format(mount_protocol, allowed_values)
            )

        self._mount_protocol = mount_protocol

    @property
    def password(self):
        """
        Gets the password of this VmediaMapping.
        Password associated with the username  

        :return: The password of this VmediaMapping.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this VmediaMapping.
        Password associated with the username  

        :param password: The password of this VmediaMapping.
        :type: str
        """

        self._password = password

    @property
    def remote_file(self):
        """
        Gets the remote_file of this VmediaMapping.
        Name of the remote file. It should be of .img format for HDD Virtual Media mapping and .iso format for CDD Virtual Media mapping.  

        :return: The remote_file of this VmediaMapping.
        :rtype: str
        """
        return self._remote_file

    @remote_file.setter
    def remote_file(self, remote_file):
        """
        Sets the remote_file of this VmediaMapping.
        Name of the remote file. It should be of .img format for HDD Virtual Media mapping and .iso format for CDD Virtual Media mapping.  

        :param remote_file: The remote_file of this VmediaMapping.
        :type: str
        """

        self._remote_file = remote_file

    @property
    def remote_path(self):
        """
        Gets the remote_path of this VmediaMapping.
        Path to the location of the image on the remote server. Preferred format is /path/.  

        :return: The remote_path of this VmediaMapping.
        :rtype: str
        """
        return self._remote_path

    @remote_path.setter
    def remote_path(self, remote_path):
        """
        Sets the remote_path of this VmediaMapping.
        Path to the location of the image on the remote server. Preferred format is /path/.  

        :param remote_path: The remote_path of this VmediaMapping.
        :type: str
        """

        self._remote_path = remote_path

    @property
    def username(self):
        """
        Gets the username of this VmediaMapping.
        Username to log in to the remote server  

        :return: The username of this VmediaMapping.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this VmediaMapping.
        Username to log in to the remote server  

        :param username: The username of this VmediaMapping.
        :type: str
        """

        self._username = username

    @property
    def volume_name(self):
        """
        Gets the volume_name of this VmediaMapping.
        Identity of the image for Virtual Media mapping   

        :return: The volume_name of this VmediaMapping.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """
        Sets the volume_name of this VmediaMapping.
        Identity of the image for Virtual Media mapping   

        :param volume_name: The volume_name of this VmediaMapping.
        :type: str
        """

        self._volume_name = volume_name

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
        if not isinstance(other, VmediaMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
