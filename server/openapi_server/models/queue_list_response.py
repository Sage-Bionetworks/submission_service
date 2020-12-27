# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.list_response_metadata import ListResponseMetadata
from openapi_server.models.list_response_metadata_links import ListResponseMetadataLinks
from openapi_server.models.queue import Queue
from openapi_server.models.queue_list_response_all_of import QueueListResponseAllOf
from openapi_server import util

from openapi_server.models.list_response_metadata import ListResponseMetadata  # noqa: E501
from openapi_server.models.list_response_metadata_links import ListResponseMetadataLinks  # noqa: E501
from openapi_server.models.queue import Queue  # noqa: E501
from openapi_server.models.queue_list_response_all_of import QueueListResponseAllOf  # noqa: E501

class QueueListResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, links=None, queues=None):  # noqa: E501
        """QueueListResponse - a model defined in OpenAPI

        :param offset: The offset of this QueueListResponse.  # noqa: E501
        :type offset: int
        :param limit: The limit of this QueueListResponse.  # noqa: E501
        :type limit: int
        :param links: The links of this QueueListResponse.  # noqa: E501
        :type links: ListResponseMetadataLinks
        :param queues: The queues of this QueueListResponse.  # noqa: E501
        :type queues: List[Queue]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': ListResponseMetadataLinks,
            'queues': List[Queue]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'queues': 'queues'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
        self._queues = queues

    @classmethod
    def from_dict(cls, dikt) -> 'QueueListResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The QueueListResponse of this QueueListResponse.  # noqa: E501
        :rtype: QueueListResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this QueueListResponse.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this QueueListResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this QueueListResponse.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this QueueListResponse.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this QueueListResponse.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this QueueListResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this QueueListResponse.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this QueueListResponse.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this QueueListResponse.


        :return: The links of this QueueListResponse.
        :rtype: ListResponseMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this QueueListResponse.


        :param links: The links of this QueueListResponse.
        :type links: ListResponseMetadataLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def queues(self):
        """Gets the queues of this QueueListResponse.

        An array of queues  # noqa: E501

        :return: The queues of this QueueListResponse.
        :rtype: List[Queue]
        """
        return self._queues

    @queues.setter
    def queues(self, queues):
        """Sets the queues of this QueueListResponse.

        An array of queues  # noqa: E501

        :param queues: The queues of this QueueListResponse.
        :type queues: List[Queue]
        """

        self._queues = queues
