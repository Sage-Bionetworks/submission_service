import connexion
import six

from openapi_server.models import ComputeEnv  # noqa: E501
from openapi_server.models import CreateComputeEnvRequest  # noqa: E501
from openapi_server.models import CreateComputeEnvResponse  # noqa: E501
from openapi_server.models import Error  # noqa: E501
from openapi_server.models import ListComputeEnvResponse  # noqa: E501
from openapi_server import util
from openapi_server.core.controllers import compute_controller as controller


def create_compute_env(
    create_compute_env_request
):  # noqa: E501
    """Create a compute environment

    Creates a compute environment # noqa: E501

    :param create_compute_env_request: 
    :type create_compute_env_request: dict | bytes

    :rtype: CreateComputeEnvResponse
    """
    if connexion.request.is_json:
        create_compute_env_request = CreateComputeEnvRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.create_compute_env(
        create_compute_env_request=create_compute_env_request
    )


def delete_compute_env(
    compute_env_id
):  # noqa: E501
    """Delete a compute environment by its ID

    Deletes the compute environment for a given ID # noqa: E501

    :param compute_env_id: The ID of the compute environment
    :type compute_env_id: str

    :rtype: None
    """
    return controller.delete_compute_env(
        compute_env_id=compute_env_id
    )


def get_compute_env(
    compute_env_id
):  # noqa: E501
    """Get a compute env by its ID

    Returns the compute env for a given ID # noqa: E501

    :param compute_env_id: The ID of the compute environment
    :type compute_env_id: str

    :rtype: ComputeEnv
    """
    return controller.get_compute_env(
        compute_env_id=compute_env_id
    )


def list_compute_envs(
    limit=10,
    offset=0
):  # noqa: E501
    """List the available compute environments

    Returns the available compute environments # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: ListComputeEnvResponse
    """
    return controller.list_compute_envs(
        limit=limit,
        offset=offset
    )
