# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.create_queue_request import CreateQueueRequest  # noqa: E501
from openapi_server.models.create_queue_response import CreateQueueResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.list_queue_response import ListQueueResponse  # noqa: E501
from openapi_server.models.queue import Queue  # noqa: E501
from openapi_server.test import BaseTestCase


class TestQueueController(BaseTestCase):
    """QueueController integration test stubs"""

    def test_create_queue(self):
        """Test case for create_queue

        Create a queue
        """
        create_queue_request = {
  "submissionType" : "docker",
  "workflowFiles" : [ "workflowFiles", "workflowFiles" ],
  "workflowInput" : "workflowInput",
  "computeId" : "computeId",
  "name" : "name"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/queues',
            method='POST',
            headers=headers,
            data=json.dumps(create_queue_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_queue(self):
        """Test case for delete_queue

        Delete a queue by its ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}'.format(queue_id='queue_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_queue(self):
        """Test case for get_queue

        Get a queue by its ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}'.format(queue_id='queue_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_queues(self):
        """Test case for list_queues

        List the available queues
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
