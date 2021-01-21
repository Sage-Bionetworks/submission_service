import connexion
import six

from openapi_server.models import CreateQueueRequest  # noqa: E501
from openapi_server.models import CreateQueueResponse  # noqa: E501
from openapi_server.models import Error  # noqa: E501
from openapi_server.models import ListQueueResponse  # noqa: E501
from openapi_server.models import Queue  # noqa: E501
from openapi_server import util
from openapi_server.core.controllers import queue_controller as controller


def create_queue(
    create_queue_request
):  # noqa: E501
    """Create a queue

    Creates a queue for storing and running of submissions # noqa: E501

    :param create_queue_request: 
    :type create_queue_request: dict | bytes

    :rtype: CreateQueueResponse
    """
    if connexion.request.is_json:
        create_queue_request = CreateQueueRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.create_queue(
        create_queue_request=create_queue_request
    )


def delete_queue(
    queue_id
):  # noqa: E501
    """Delete a queue by its ID

    Deletes the queue for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str

    :rtype: None
    """
    return controller.delete_queue(
        queue_id=queue_id
    )


def get_queue(
    queue_id
):  # noqa: E501
    """Get a queue by its ID

    Returns the queue for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str

    :rtype: Queue
    """
    return controller.get_queue(
        queue_id=queue_id
    )


def list_queues(
    limit=10,
    offset=0
):  # noqa: E501
    """List the available queues

    Returns the queues # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: ListQueueResponse
    """
    return controller.list_queues(
        limit=limit,
        offset=offset
    )


def update_queue(
    queue_id,
    queue
):  # noqa: E501
    """Update a queue by its ID

    Updates the queue for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param queue: 
    :type queue: dict | bytes

    :rtype: Queue
    """
    if connexion.request.is_json:
        queue = Queue.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.update_queue(
        queue_id=queue_id,
        queue=queue
    )
