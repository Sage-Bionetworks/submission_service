import connexion
import six

from openapi_server.models.create_submission_request import CreateSubmissionRequest  # noqa: E501
from openapi_server.models.create_submission_response import CreateSubmissionResponse  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.list_submission_response import ListSubmissionResponse  # noqa: E501
from openapi_server.models.submission import Submission  # noqa: E501
from openapi_server import util


def create_submission(queue_id, create_submission_request=None):  # noqa: E501
    """Create a submission

    Creates a submission # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param create_submission_request: 
    :type create_submission_request: dict | bytes

    :rtype: CreateSubmissionResponse
    """
    if connexion.request.is_json:
        create_submission_request = CreateSubmissionRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_submission(queue_id, submission_id):  # noqa: E501
    """Delete a submission by its ID

    Deletes the submission for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: None
    """
    return 'do some magic!'


def get_submission(queue_id, submission_id):  # noqa: E501
    """Get a submission by its ID

    Returns the submission for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: Submission
    """
    return 'do some magic!'


def list_submissions(queue_id, limit=None, offset=None):  # noqa: E501
    """List the submitted submissions

    Returns the submissions from a queue # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param limit: Maximum number of results returned
    :type limit: int
    :param offset: Index of the first result that must be returned
    :type offset: int

    :rtype: ListSubmissionResponse
    """
    return 'do some magic!'
