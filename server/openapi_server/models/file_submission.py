# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.submission_status import SubmissionStatus
from openapi_server.openapi import util


class FileSubmission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, id=None, submitter=None, queue_id=None, status=None, file=None):  # noqa: E501
        """FileSubmission - a model defined in OpenAPI

        :param name: The name of this FileSubmission.  # noqa: E501
        :type name: str
        :param id: The id of this FileSubmission.  # noqa: E501
        :type id: int
        :param submitter: The submitter of this FileSubmission.  # noqa: E501
        :type submitter: str
        :param queue_id: The queue_id of this FileSubmission.  # noqa: E501
        :type queue_id: str
        :param status: The status of this FileSubmission.  # noqa: E501
        :type status: SubmissionStatus
        :param file: The file of this FileSubmission.  # noqa: E501
        :type file: str
        """
        self.openapi_types = {
            'name': str,
            'id': int,
            'submitter': str,
            'queue_id': str,
            'status': SubmissionStatus,
            'file': str
        }

        self.attribute_map = {
            'name': 'name',
            'id': 'id',
            'submitter': 'submitter',
            'queue_id': 'queueId',
            'status': 'status',
            'file': 'file'
        }

        self._name = name
        self._id = id
        self._submitter = submitter
        self._queue_id = queue_id
        self._status = status
        self._file = file

    @classmethod
    def from_dict(cls, dikt) -> 'FileSubmission':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileSubmission of this FileSubmission.  # noqa: E501
        :rtype: FileSubmission
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this FileSubmission.

        Name of submission  # noqa: E501

        :return: The name of this FileSubmission.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSubmission.

        Name of submission  # noqa: E501

        :param name: The name of this FileSubmission.
        :type name: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this FileSubmission.

        Submission Id  # noqa: E501

        :return: The id of this FileSubmission.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileSubmission.

        Submission Id  # noqa: E501

        :param id: The id of this FileSubmission.
        :type id: int
        """

        self._id = id

    @property
    def submitter(self):
        """Gets the submitter of this FileSubmission.

        Submitter name  # noqa: E501

        :return: The submitter of this FileSubmission.
        :rtype: str
        """
        return self._submitter

    @submitter.setter
    def submitter(self, submitter):
        """Sets the submitter of this FileSubmission.

        Submitter name  # noqa: E501

        :param submitter: The submitter of this FileSubmission.
        :type submitter: str
        """

        self._submitter = submitter

    @property
    def queue_id(self):
        """Gets the queue_id of this FileSubmission.

        Queue Id  # noqa: E501

        :return: The queue_id of this FileSubmission.
        :rtype: str
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id):
        """Sets the queue_id of this FileSubmission.

        Queue Id  # noqa: E501

        :param queue_id: The queue_id of this FileSubmission.
        :type queue_id: str
        """

        self._queue_id = queue_id

    @property
    def status(self):
        """Gets the status of this FileSubmission.


        :return: The status of this FileSubmission.
        :rtype: SubmissionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FileSubmission.


        :param status: The status of this FileSubmission.
        :type status: SubmissionStatus
        """

        self._status = status

    @property
    def file(self):
        """Gets the file of this FileSubmission.

        File to submit to challenge  # noqa: E501

        :return: The file of this FileSubmission.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this FileSubmission.

        File to submit to challenge  # noqa: E501

        :param file: The file of this FileSubmission.
        :type file: str
        """

        self._file = file
