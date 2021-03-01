import connexion
from mongoengine.errors import DoesNotExist, NotUniqueError
import six

from openapi_server.models.create_queue_request import CreateQueueRequest  # noqa: E501
from openapi_server.models.create_queue_response import CreateQueueResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.list_queue_response import ListQueueResponse  # noqa: E501
from openapi_server.models.queue import Queue  # noqa: E501
from openapi_server import util


def create_queue(queue_id):  # noqa: E501
    """Create a queue

    Creates a queue for storing and running of submissions # noqa: E501

    :param create_queue_request: 
    :type create_queue_request: dict | bytes

    :rtype: CreateQueueResponse
    """
    res = None
    status = None
    try:
        try:
            create_queue_request = CreateQueueRequest.from_dict(
                connexion.request.get_json()
            )
            print(create_queue_request)
            # DbPatient(
            #     resourceName=resource_name,
            #     fhirStoreName=store_name,
            #     identifier=patient_id,
            #     gender=patient_create_request.gender
            # ).save()
            # patient_resource_name = "%s/fhir/Patient/%s" % \
            #     (store_name, patient_id)
            # res = PatientCreateResponse(name=patient_resource_name)
            # status = 201
        except NotUniqueError as error:
            status = 409
            res = Error("Conflict", status, str(error))
    except Exception as error:
        status = 500
        res = Error("Internal error", status, str(error))
    return res, status


def delete_queue(queue_id):  # noqa: E501
    """Delete a queue by its ID

    Deletes the queue for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str

    :rtype: None
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

    :rtype: ListQueueResponse
    """
    return 'do some magic!'
