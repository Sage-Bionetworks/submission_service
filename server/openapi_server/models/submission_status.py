# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SubmissionStatus(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status=None, number_of_runs=None):  # noqa: E501
        """SubmissionStatus - a model defined in OpenAPI

        :param status: The status of this SubmissionStatus.  # noqa: E501
        :type status: str
        :param number_of_runs: The number_of_runs of this SubmissionStatus.  # noqa: E501
        :type number_of_runs: int
        """
        self.openapi_types = {
            'status': str,
            'number_of_runs': int
        }

        self.attribute_map = {
            'status': 'status',
            'number_of_runs': 'numberOfRuns'
        }

        self._status = status
        self._number_of_runs = number_of_runs

    @classmethod
    def from_dict(cls, dikt) -> 'SubmissionStatus':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubmissionStatus of this SubmissionStatus.  # noqa: E501
        :rtype: SubmissionStatus
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this SubmissionStatus.

        Submission status  # noqa: E501

        :return: The status of this SubmissionStatus.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubmissionStatus.

        Submission status  # noqa: E501

        :param status: The status of this SubmissionStatus.
        :type status: str
        """
        allowed_values = ["RECEIVED", "SUBMITTED", "EVALUATION_IN_PROGRESS", "INVALID", "ACCEPTED", "REJECTED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def number_of_runs(self):
        """Gets the number_of_runs of this SubmissionStatus.

        Number of times submission has been executed  # noqa: E501

        :return: The number_of_runs of this SubmissionStatus.
        :rtype: int
        """
        return self._number_of_runs

    @number_of_runs.setter
    def number_of_runs(self, number_of_runs):
        """Sets the number_of_runs of this SubmissionStatus.

        Number of times submission has been executed  # noqa: E501

        :param number_of_runs: The number_of_runs of this SubmissionStatus.
        :type number_of_runs: int
        """

        self._number_of_runs = number_of_runs