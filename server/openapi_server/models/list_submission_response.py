# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.list_response_metadata import ListResponseMetadata
from openapi_server.models.list_response_metadata_links import ListResponseMetadataLinks
from openapi_server.models.list_submission_response_all_of import ListSubmissionResponseAllOf
from openapi_server.models.submission import Submission
from openapi_server import util

from openapi_server.models.list_response_metadata import ListResponseMetadata  # noqa: E501
from openapi_server.models.list_response_metadata_links import ListResponseMetadataLinks  # noqa: E501
from openapi_server.models.list_submission_response_all_of import ListSubmissionResponseAllOf  # noqa: E501
from openapi_server.models.submission import Submission  # noqa: E501

class ListSubmissionResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, links=None, total_results=None, submissions=None):  # noqa: E501
        """ListSubmissionResponse - a model defined in OpenAPI

        :param offset: The offset of this ListSubmissionResponse.  # noqa: E501
        :type offset: int
        :param limit: The limit of this ListSubmissionResponse.  # noqa: E501
        :type limit: int
        :param links: The links of this ListSubmissionResponse.  # noqa: E501
        :type links: ListResponseMetadataLinks
        :param total_results: The total_results of this ListSubmissionResponse.  # noqa: E501
        :type total_results: int
        :param submissions: The submissions of this ListSubmissionResponse.  # noqa: E501
        :type submissions: List[Submission]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': ListResponseMetadataLinks,
            'total_results': int,
            'submissions': List[Submission]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'total_results': 'totalResults',
            'submissions': 'submissions'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
        self._total_results = total_results
        self._submissions = submissions

    @classmethod
    def from_dict(cls, dikt) -> 'ListSubmissionResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ListSubmissionResponse of this ListSubmissionResponse.  # noqa: E501
        :rtype: ListSubmissionResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this ListSubmissionResponse.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this ListSubmissionResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubmissionResponse.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this ListSubmissionResponse.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubmissionResponse.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this ListSubmissionResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubmissionResponse.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this ListSubmissionResponse.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this ListSubmissionResponse.


        :return: The links of this ListSubmissionResponse.
        :rtype: ListResponseMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ListSubmissionResponse.


        :param links: The links of this ListSubmissionResponse.
        :type links: ListResponseMetadataLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def total_results(self):
        """Gets the total_results of this ListSubmissionResponse.

        The total number of results in the result set  # noqa: E501

        :return: The total_results of this ListSubmissionResponse.
        :rtype: int
        """
        return self._total_results

    @total_results.setter
    def total_results(self, total_results):
        """Sets the total_results of this ListSubmissionResponse.

        The total number of results in the result set  # noqa: E501

        :param total_results: The total_results of this ListSubmissionResponse.
        :type total_results: int
        """
        if total_results is None:
            raise ValueError("Invalid value for `total_results`, must not be `None`")  # noqa: E501

        self._total_results = total_results

    @property
    def submissions(self):
        """Gets the submissions of this ListSubmissionResponse.

        An array of queues  # noqa: E501

        :return: The submissions of this ListSubmissionResponse.
        :rtype: List[Submission]
        """
        return self._submissions

    @submissions.setter
    def submissions(self, submissions):
        """Sets the submissions of this ListSubmissionResponse.

        An array of queues  # noqa: E501

        :param submissions: The submissions of this ListSubmissionResponse.
        :type submissions: List[Submission]
        """

        self._submissions = submissions
