# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.compute_env_id import ComputeEnvId  # noqa: E501
from openapi_server.models.compute_env_list_response import ComputeEnvListResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.one_of_wes_compute_env import OneOfWesComputeEnv  # noqa: E501
from openapi_server.models.one_of_wes_compute_env_response import OneOfWesComputeEnvResponse  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server.test import BaseTestCase


class TestComputeController(BaseTestCase):
    """ComputeController integration test stubs"""

    def test_create_compute_env(self):
        """Test case for create_compute_env

        Create a compute environment
        """
        unknown_base_type = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/computeEnvs',
            method='POST',
            headers=headers,
            data=json.dumps(unknown_base_type),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_compute_env(self):
        """Test case for delete_compute_env

        Delete a compute environment by its ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/computeEnvs/{compute_env_id}'.format(compute_env_id='compute_env_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_compute_env(self):
        """Test case for get_compute_env

        Get a compute env by its ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/computeEnvs/{compute_env_id}'.format(compute_env_id='compute_env_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_compute_envs(self):
        """Test case for list_compute_envs

        List the available compute environments
        """
        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/computeEnvs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
