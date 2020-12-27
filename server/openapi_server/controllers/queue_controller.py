import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.queue import Queue  # noqa: E501
from openapi_server.models.queue_list_response import QueueListResponse  # noqa: E501
from openapi_server import util


def create_queue(queue=None):  # noqa: E501
    """Create a queue

    Creates a queue for storing and running of submissions # noqa: E501

    :param queue: 
    :type queue: dict | bytes

    :rtype: Queue
    """
    if connexion.request.is_json:
        queue = Queue.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_queue(queue_id):  # noqa: E501
    """Delete a queue by its ID

    Deletes the queue for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str

    :rtype: Queue
    """
    return 'do some magic!'


def get_queue(queue_id):  # noqa: E501
    """Get a queue by its ID

    Returns the queue for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str

    :rtype: Queue
    """
    return 'do some magic!'


def list_queues(limit=None, offset=None):  # noqa: E501
    """List the available queues

    Returns the queues # noqa: E501

    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: QueueListResponse
    """
    return 'do some magic!'


def update_queue(queue_id, queue=None):  # noqa: E501
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
    return 'do some magic!'
