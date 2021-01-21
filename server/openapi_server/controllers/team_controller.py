import connexion
import six

from openapi_server.models import CreateTeamRequest  # noqa: E501
from openapi_server.models import CreateTeamResponse  # noqa: E501
from openapi_server.models import Error  # noqa: E501
from openapi_server import util
from openapi_server.core.controllers import team_controller as controller


def create_team(
    create_team_request
):  # noqa: E501
    """Create a Team

    Creates a team for submitting # noqa: E501

    :param create_team_request: 
    :type create_team_request: dict | bytes

    :rtype: CreateTeamResponse
    """
    if connexion.request.is_json:
        create_team_request = CreateTeamRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.create_team(
        create_team_request=create_team_request
    )
