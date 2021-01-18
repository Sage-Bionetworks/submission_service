# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.team import Team  # noqa: E501
from openapi_server.models.team_id import TeamId  # noqa: E501
from openapi_server.test import BaseTestCase


class TestTeamController(BaseTestCase):
    """TeamController integration test stubs"""

    def test_create_team(self):
        """Test case for create_team

        Create a Team
        """
        team = {
  "teamId" : "teamId",
  "name" : "name",
  "description" : "description"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/teams',
            method='POST',
            headers=headers,
            data=json.dumps(team),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
