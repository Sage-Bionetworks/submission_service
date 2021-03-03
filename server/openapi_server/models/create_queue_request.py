# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class CreateQueueRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, compute_id=None, workflow_files=None, workflow_input=None, submission_type=None):  # noqa: E501
        """CreateQueueRequest - a model defined in OpenAPI

        :param name: The name of this CreateQueueRequest.  # noqa: E501
        :type name: str
        :param compute_id: The compute_id of this CreateQueueRequest.  # noqa: E501
        :type compute_id: str
        :param workflow_files: The workflow_files of this CreateQueueRequest.  # noqa: E501
        :type workflow_files: List[str]
        :param workflow_input: The workflow_input of this CreateQueueRequest.  # noqa: E501
        :type workflow_input: str
        :param submission_type: The submission_type of this CreateQueueRequest.  # noqa: E501
        :type submission_type: str
        """
        self.openapi_types = {
            'name': str,
            'compute_id': str,
            'workflow_files': List[str],
            'workflow_input': str,
            'submission_type': str
        }

        self.attribute_map = {
            'name': 'name',
            'compute_id': 'computeId',
            'workflow_files': 'workflowFiles',
            'workflow_input': 'workflowInput',
            'submission_type': 'submissionType'
        }

        self._name = name
        self._compute_id = compute_id
        self._workflow_files = workflow_files
        self._workflow_input = workflow_input
        self._submission_type = submission_type

    @classmethod
    def from_dict(cls, dikt) -> 'CreateQueueRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateQueueRequest of this CreateQueueRequest.  # noqa: E501
        :rtype: CreateQueueRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateQueueRequest.

        Name of Queue  # noqa: E501

        :return: The name of this CreateQueueRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateQueueRequest.

        Name of Queue  # noqa: E501

        :param name: The name of this CreateQueueRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501
        if name is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._name = name

    @property
    def compute_id(self):
        """Gets the compute_id of this CreateQueueRequest.

        Compute Environment Id  # noqa: E501

        :return: The compute_id of this CreateQueueRequest.
        :rtype: str
        """
        return self._compute_id

    @compute_id.setter
    def compute_id(self, compute_id):
        """Sets the compute_id of this CreateQueueRequest.

        Compute Environment Id  # noqa: E501

        :param compute_id: The compute_id of this CreateQueueRequest.
        :type compute_id: str
        """

        self._compute_id = compute_id

    @property
    def workflow_files(self):
        """Gets the workflow_files of this CreateQueueRequest.

        Workflow/Tool files and templates  # noqa: E501

        :return: The workflow_files of this CreateQueueRequest.
        :rtype: List[str]
        """
        return self._workflow_files

    @workflow_files.setter
    def workflow_files(self, workflow_files):
        """Sets the workflow_files of this CreateQueueRequest.

        Workflow/Tool files and templates  # noqa: E501

        :param workflow_files: The workflow_files of this CreateQueueRequest.
        :type workflow_files: List[str]
        """

        self._workflow_files = workflow_files

    @property
    def workflow_input(self):
        """Gets the workflow_input of this CreateQueueRequest.

        Path to workflow inputs  # noqa: E501

        :return: The workflow_input of this CreateQueueRequest.
        :rtype: str
        """
        return self._workflow_input

    @workflow_input.setter
    def workflow_input(self, workflow_input):
        """Sets the workflow_input of this CreateQueueRequest.

        Path to workflow inputs  # noqa: E501

        :param workflow_input: The workflow_input of this CreateQueueRequest.
        :type workflow_input: str
        """

        self._workflow_input = workflow_input

    @property
    def submission_type(self):
        """Gets the submission_type of this CreateQueueRequest.

        Path to workflow inputs  # noqa: E501

        :return: The submission_type of this CreateQueueRequest.
        :rtype: str
        """
        return self._submission_type

    @submission_type.setter
    def submission_type(self, submission_type):
        """Sets the submission_type of this CreateQueueRequest.

        Path to workflow inputs  # noqa: E501

        :param submission_type: The submission_type of this CreateQueueRequest.
        :type submission_type: str
        """
        allowed_values = ["docker", "file", "workflow", "workflow_inputs"]  # noqa: E501
        if submission_type not in allowed_values:
            raise ValueError(
                "Invalid value for `submission_type` ({0}), must be one of {1}"
                .format(submission_type, allowed_values)
            )

        self._submission_type = submission_type
