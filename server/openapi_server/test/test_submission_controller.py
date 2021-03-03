# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.create_submission_request import CreateSubmissionRequest  # noqa: E501
from openapi_server.models.create_submission_response import CreateSubmissionResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.list_submission_response import ListSubmissionResponse  # noqa: E501
from openapi_server.models.submission import Submission  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSubmissionController(BaseTestCase):
    """SubmissionController integration test stubs"""

    def test_create_submission(self):
        """Test case for create_submission

        Create a submission
        """
        create_submission_request = null
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}/submissions'.format(queue_id='queue_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(create_submission_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_submission(self):
        """Test case for delete_submission

        Delete a submission by its ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}/submissions/{submission_id}'.format(queue_id='queue_id_example', submission_id='submission_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submission(self):
        """Test case for get_submission

        Get a submission by its ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}/submissions/{submission_id}'.format(queue_id='queue_id_example', submission_id='submission_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_submissions(self):
        """Test case for list_submissions

        List the submitted submissions
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}/submissions'.format(queue_id='queue_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
