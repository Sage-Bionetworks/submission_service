import connexion
import six

from openapi_server.models.create_team_request import CreateTeamRequest  # noqa: E501
from openapi_server.models.create_team_response import CreateTeamResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server import util


def create_team(create_team_request=None):  # noqa: E501
    """Create a Team

    Creates a team for submitting # noqa: E501

    :param create_team_request: 
    :type create_team_request: dict | bytes

    :rtype: CreateTeamResponse
    """
    if connexion.request.is_json:
        create_team_request = CreateTeamRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
