# coding: utf-8

"""
    Cloudbreak API

    Cloudbreak is a powerful left surf that breaks over a coral reef, a mile off southwest the island of Tavarua, Fiji. Cloudbreak is a cloud agnostic Hadoop as a Service API. Abstracts the provisioning and ease management and monitoring of on-demand clusters. SequenceIQ's Cloudbreak is a RESTful application development platform with the goal of helping developers to build solutions for deploying Hadoop YARN clusters in different environments. Once it is deployed in your favourite servlet container it exposes a REST API allowing to span up Hadoop clusters of arbitary sizes and cloud providers. Provisioning Hadoop has never been easier. Cloudbreak is built on the foundation of cloud providers API (Amazon AWS, Microsoft Azure, Google Cloud Platform, Openstack), Apache Ambari, Docker lightweight containers, Swarm and Consul. For further product documentation follow the link: <a href=\"http://hortonworks.com/apache/cloudbreak/\">http://hortonworks.com/apache/cloudbreak/</a>

    OpenAPI spec version: 2.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BlueprintParameter(object):
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
        'name': 'str',
        'description': 'str',
        'reference_configuration': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'reference_configuration': 'referenceConfiguration'
    }

    def __init__(self, name=None, description=None, reference_configuration=None):
        """
        BlueprintParameter - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._reference_configuration = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if reference_configuration is not None:
          self.reference_configuration = reference_configuration

    @property
    def name(self):
        """
        Gets the name of this BlueprintParameter.

        :return: The name of this BlueprintParameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BlueprintParameter.

        :param name: The name of this BlueprintParameter.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this BlueprintParameter.

        :return: The description of this BlueprintParameter.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BlueprintParameter.

        :param description: The description of this BlueprintParameter.
        :type: str
        """

        self._description = description

    @property
    def reference_configuration(self):
        """
        Gets the reference_configuration of this BlueprintParameter.

        :return: The reference_configuration of this BlueprintParameter.
        :rtype: str
        """
        return self._reference_configuration

    @reference_configuration.setter
    def reference_configuration(self, reference_configuration):
        """
        Sets the reference_configuration of this BlueprintParameter.

        :param reference_configuration: The reference_configuration of this BlueprintParameter.
        :type: str
        """

        self._reference_configuration = reference_configuration

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
        if not isinstance(other, BlueprintParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
