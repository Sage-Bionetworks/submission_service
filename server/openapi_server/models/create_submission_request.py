# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.create_docker_submission_request import CreateDockerSubmissionRequest
from openapi_server.models.create_file_submission_request import CreateFileSubmissionRequest
from openapi_server.models.create_workflow_submission_request import CreateWorkflowSubmissionRequest
from openapi_server.models.docker_submission_docker import DockerSubmissionDocker
from openapi_server.models.submission_status import SubmissionStatus
from openapi_server import util

from openapi_server.models.create_docker_submission_request import CreateDockerSubmissionRequest  # noqa: E501
from openapi_server.models.create_file_submission_request import CreateFileSubmissionRequest  # noqa: E501
from openapi_server.models.create_workflow_submission_request import CreateWorkflowSubmissionRequest  # noqa: E501
from openapi_server.models.docker_submission_docker import DockerSubmissionDocker  # noqa: E501
from openapi_server.models.submission_status import SubmissionStatus  # noqa: E501

class CreateSubmissionRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, submitter=None, status=None, docker=None, file=None, workflow=None, workflow_inputs=None):  # noqa: E501
        """CreateSubmissionRequest - a model defined in OpenAPI

        :param name: The name of this CreateSubmissionRequest.  # noqa: E501
        :type name: str
        :param submitter: The submitter of this CreateSubmissionRequest.  # noqa: E501
        :type submitter: str
        :param status: The status of this CreateSubmissionRequest.  # noqa: E501
        :type status: SubmissionStatus
        :param docker: The docker of this CreateSubmissionRequest.  # noqa: E501
        :type docker: DockerSubmissionDocker
        :param file: The file of this CreateSubmissionRequest.  # noqa: E501
        :type file: str
        :param workflow: The workflow of this CreateSubmissionRequest.  # noqa: E501
        :type workflow: str
        :param workflow_inputs: The workflow_inputs of this CreateSubmissionRequest.  # noqa: E501
        :type workflow_inputs: str
        """
        self.openapi_types = {
            'name': str,
            'submitter': str,
            'status': SubmissionStatus,
            'docker': DockerSubmissionDocker,
            'file': str,
            'workflow': str,
            'workflow_inputs': str
        }

        self.attribute_map = {
            'name': 'name',
            'submitter': 'submitter',
            'status': 'status',
            'docker': 'docker',
            'file': 'file',
            'workflow': 'workflow',
            'workflow_inputs': 'workflowInputs'
        }

        self._name = name
        self._submitter = submitter
        self._status = status
        self._docker = docker
        self._file = file
        self._workflow = workflow
        self._workflow_inputs = workflow_inputs

    @classmethod
    def from_dict(cls, dikt) -> 'CreateSubmissionRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CreateSubmissionRequest of this CreateSubmissionRequest.  # noqa: E501
        :rtype: CreateSubmissionRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this CreateSubmissionRequest.

        Name of submission  # noqa: E501

        :return: The name of this CreateSubmissionRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSubmissionRequest.

        Name of submission  # noqa: E501

        :param name: The name of this CreateSubmissionRequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def submitter(self):
        """Gets the submitter of this CreateSubmissionRequest.

        Submitter name  # noqa: E501

        :return: The submitter of this CreateSubmissionRequest.
        :rtype: str
        """
        return self._submitter

    @submitter.setter
    def submitter(self, submitter):
        """Sets the submitter of this CreateSubmissionRequest.

        Submitter name  # noqa: E501

        :param submitter: The submitter of this CreateSubmissionRequest.
        :type submitter: str
        """
        if submitter is None:
            raise ValueError("Invalid value for `submitter`, must not be `None`")  # noqa: E501

        self._submitter = submitter

    @property
    def status(self):
        """Gets the status of this CreateSubmissionRequest.


        :return: The status of this CreateSubmissionRequest.
        :rtype: SubmissionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateSubmissionRequest.


        :param status: The status of this CreateSubmissionRequest.
        :type status: SubmissionStatus
        """

        self._status = status

    @property
    def docker(self):
        """Gets the docker of this CreateSubmissionRequest.


        :return: The docker of this CreateSubmissionRequest.
        :rtype: DockerSubmissionDocker
        """
        return self._docker

    @docker.setter
    def docker(self, docker):
        """Sets the docker of this CreateSubmissionRequest.


        :param docker: The docker of this CreateSubmissionRequest.
        :type docker: DockerSubmissionDocker
        """
        if docker is None:
            raise ValueError("Invalid value for `docker`, must not be `None`")  # noqa: E501

        self._docker = docker

    @property
    def file(self):
        """Gets the file of this CreateSubmissionRequest.

        File to submit to challenge  # noqa: E501

        :return: The file of this CreateSubmissionRequest.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CreateSubmissionRequest.

        File to submit to challenge  # noqa: E501

        :param file: The file of this CreateSubmissionRequest.
        :type file: str
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def workflow(self):
        """Gets the workflow of this CreateSubmissionRequest.

        Workflow to run  # noqa: E501

        :return: The workflow of this CreateSubmissionRequest.
        :rtype: str
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this CreateSubmissionRequest.

        Workflow to run  # noqa: E501

        :param workflow: The workflow of this CreateSubmissionRequest.
        :type workflow: str
        """

        self._workflow = workflow

    @property
    def workflow_inputs(self):
        """Gets the workflow_inputs of this CreateSubmissionRequest.

        Workflow inputs  # noqa: E501

        :return: The workflow_inputs of this CreateSubmissionRequest.
        :rtype: str
        """
        return self._workflow_inputs

    @workflow_inputs.setter
    def workflow_inputs(self, workflow_inputs):
        """Sets the workflow_inputs of this CreateSubmissionRequest.

        Workflow inputs  # noqa: E501

        :param workflow_inputs: The workflow_inputs of this CreateSubmissionRequest.
        :type workflow_inputs: str
        """

        self._workflow_inputs = workflow_inputs