# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class FileSubmission(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, submission_id=None, submitter=None, file=None):  # noqa: E501
        """FileSubmission - a model defined in OpenAPI

        :param submission_id: The submission_id of this FileSubmission.  # noqa: E501
        :type submission_id: int
        :param submitter: The submitter of this FileSubmission.  # noqa: E501
        :type submitter: str
        :param file: The file of this FileSubmission.  # noqa: E501
        :type file: str
        """
        self.openapi_types = {
            'submission_id': int,
            'submitter': str,
            'file': str
        }

        self.attribute_map = {
            'submission_id': 'submissionId',
            'submitter': 'submitter',
            'file': 'file'
        }

        self._submission_id = submission_id
        self._submitter = submitter
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
    def submission_id(self):
        """Gets the submission_id of this FileSubmission.

        Queue Id  # noqa: E501

        :return: The submission_id of this FileSubmission.
        :rtype: int
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id):
        """Sets the submission_id of this FileSubmission.

        Queue Id  # noqa: E501

        :param submission_id: The submission_id of this FileSubmission.
        :type submission_id: int
        """

        self._submission_id = submission_id

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
