import connexion
import six

from openapi_server.models.compute_env import ComputeEnv  # noqa: E501
from openapi_server.models.create_compute_env_request import CreateComputeEnvRequest  # noqa: E501
from openapi_server.models.create_compute_env_response import CreateComputeEnvResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.list_compute_env_response import ListComputeEnvResponse  # noqa: E501
from openapi_server import util


def create_compute_env(create_compute_env_request=None):  # noqa: E501
    """Create a compute environment

    Creates a compute environment # noqa: E501

    :param create_compute_env_request: 
    :type create_compute_env_request: dict | bytes

    :rtype: CreateComputeEnvResponse
    """
    if connexion.request.is_json:
        create_compute_env_request = CreateComputeEnvRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_compute_env(compute_env_id):  # noqa: E501
    """Delete a compute environment by its ID

    Deletes the compute environment for a given ID # noqa: E501

    :param compute_env_id: The ID of the compute environment
    :type compute_env_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_compute_env(compute_env_id):  # noqa: E501
    """Get a compute env by its ID

    Returns the compute env for a given ID # noqa: E501

    :param compute_env_id: The ID of the compute environment
    :type compute_env_id: str

    :rtype: ComputeEnv
    """
    return 'do some magic!'


def list_compute_envs(limit=None, offset=None):  # noqa: E501
    """List the available compute environments

    Returns the available compute environments # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: ListComputeEnvResponse
    """
    return 'do some magic!'
