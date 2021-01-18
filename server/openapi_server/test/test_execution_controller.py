# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.run import Run  # noqa: E501
from openapi_server.models.run_id import RunId  # noqa: E501
from openapi_server.test import BaseTestCase


class TestExecutionController(BaseTestCase):
    """ExecutionController integration test stubs"""

    def test_delete_submission_run(self):
        """Test case for delete_submission_run

        Delete a submission run
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}/submissions/{submission_id}/runs/{run_id}'.format(queue_id='queue_id_example', run_id='run_id_example', submission_id='submission_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_submission_run(self):
        """Test case for get_submission_run

        Get a submission run
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}/submissions/{submission_id}/runs/{run_id}'.format(queue_id='queue_id_example', run_id='run_id_example', submission_id='submission_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_run_submission(self):
        """Test case for run_submission

        Executes a submission
        """
        run = {
  "data" : "data",
  "dataVersion" : "dataVersion"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/queues/{queue_id}/submissions/{submission_id}/runs'.format(queue_id='queue_id_example', submission_id='submission_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(run),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
