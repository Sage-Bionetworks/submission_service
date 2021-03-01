# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.submission_status import SubmissionStatus
from openapi_server import util

from openapi_server.models.submission_status import SubmissionStatus  # noqa: E501

class CreateWorkflowSubmissionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, submitter=None, status=None, workflow=None, workflow_inputs=None):  # noqa: E501
        """CreateWorkflowSubmissionRequest - a model defined in OpenAPI

        :param name: The name of this CreateWorkflowSubmissionRequest.  # noqa: E501
        :type name: str
        :param submitter: The submitter of this CreateWorkflowSubmissionRequest.  # noqa: E501
        :type submitter: str
        :param status: The status of this CreateWorkflowSubmissionRequest.  # noqa: E501
        :type status: SubmissionStatus
        :param workflow: The workflow of this CreateWorkflowSubmissionRequest.  # noqa: E501
        :type workflow: str
        :param workflow_inputs: The workflow_inputs of this CreateWorkflowSubmissionRequest.  # noqa: E501
        :type workflow_inputs: str
        """
        self.openapi_types = {
            'name': str,
            'submitter': str,
            'status': SubmissionStatus,
            'workflow': str,
            'workflow_inputs': str
        }

        self.attribute_map = {
            'name': 'name',
            'submitter': 'submitter',
            'status': 'status',
            'workflow': 'workflow',
            'workflow_inputs': 'workflowInputs'
        }

        self._name = name
        self._submitter = submitter
        self._status = status
        self._workflow = workflow
        self._workflow_inputs = workflow_inputs

    @classmethod
    def from_dict(cls, dikt) -> 'CreateWorkflowSubmissionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateWorkflowSubmissionRequest of this CreateWorkflowSubmissionRequest.  # noqa: E501
        :rtype: CreateWorkflowSubmissionRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateWorkflowSubmissionRequest.

        Name of submission  # noqa: E501

        :return: The name of this CreateWorkflowSubmissionRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateWorkflowSubmissionRequest.

        Name of submission  # noqa: E501

        :param name: The name of this CreateWorkflowSubmissionRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def submitter(self):
        """Gets the submitter of this CreateWorkflowSubmissionRequest.

        Submitter name  # noqa: E501

        :return: The submitter of this CreateWorkflowSubmissionRequest.
        :rtype: str
        """
        return self._submitter

    @submitter.setter
    def submitter(self, submitter):
        """Sets the submitter of this CreateWorkflowSubmissionRequest.

        Submitter name  # noqa: E501

        :param submitter: The submitter of this CreateWorkflowSubmissionRequest.
        :type submitter: str
        """
        if submitter is None:
            raise ValueError("Invalid value for `submitter`, must not be `None`")  # noqa: E501

        self._submitter = submitter

    @property
    def status(self):
        """Gets the status of this CreateWorkflowSubmissionRequest.


        :return: The status of this CreateWorkflowSubmissionRequest.
        :rtype: SubmissionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateWorkflowSubmissionRequest.


        :param status: The status of this CreateWorkflowSubmissionRequest.
        :type status: SubmissionStatus
        """

        self._status = status

    @property
    def workflow(self):
        """Gets the workflow of this CreateWorkflowSubmissionRequest.

        Workflow to run  # noqa: E501

        :return: The workflow of this CreateWorkflowSubmissionRequest.
        :rtype: str
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this CreateWorkflowSubmissionRequest.

        Workflow to run  # noqa: E501

        :param workflow: The workflow of this CreateWorkflowSubmissionRequest.
        :type workflow: str
        """

        self._workflow = workflow

    @property
    def workflow_inputs(self):
        """Gets the workflow_inputs of this CreateWorkflowSubmissionRequest.

        Workflow inputs  # noqa: E501

        :return: The workflow_inputs of this CreateWorkflowSubmissionRequest.
        :rtype: str
        """
        return self._workflow_inputs

    @workflow_inputs.setter
    def workflow_inputs(self, workflow_inputs):
        """Sets the workflow_inputs of this CreateWorkflowSubmissionRequest.

        Workflow inputs  # noqa: E501

        :param workflow_inputs: The workflow_inputs of this CreateWorkflowSubmissionRequest.
        :type workflow_inputs: str
        """

        self._workflow_inputs = workflow_inputs
