import connexion
import six

from openapi_server.models import CreateSubmissionResponse  # noqa: E501
from openapi_server.models import Error  # noqa: E501
from openapi_server.models import ListSubmissionResponse  # noqa: E501
from openapi_server.models import OneOfCreateDockerSubmissionRequestCreateFileSubmissionRequestCreateWorkflowSubmissionRequest  # noqa: E501
from openapi_server.models import OneOfDockerSubmissionFileSubmissionWorkflowSubmission  # noqa: E501
from openapi_server.models import SubmissionStatus2  # noqa: E501
from openapi_server.models import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util
from openapi_server.core.controllers import submission_controller as controller


def create_submission(
    queue_id,
    unknown_base_type
):  # noqa: E501
    """Create a submission

    Creates a submission # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: CreateSubmissionResponse
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.create_submission(
        queue_id=queue_id,
        unknown_base_type=unknown_base_type
    )


def delete_submission(
    queue_id,
    submission_id
):  # noqa: E501
    """Delete a submission by its ID

    Deletes the submission for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: None
    """
    return controller.delete_submission(
        queue_id=queue_id,
        submission_id=submission_id
    )


def get_submission(
    queue_id,
    submission_id
):  # noqa: E501
    """Get a submission by its ID

    Returns the submission for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: OneOfDockerSubmissionFileSubmissionWorkflowSubmission
    """
    return controller.get_submission(
        queue_id=queue_id,
        submission_id=submission_id
    )


def get_submission_status(
    queue_id,
    submission_id
):  # noqa: E501
    """Get a submission&#39;s status

    Returns the submission&#39;s status for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: SubmissionStatus2
    """
    return controller.get_submission_status(
        queue_id=queue_id,
        submission_id=submission_id
    )


def list_submissions(
    queue_id,
    limit=10,
    offset=0
):  # noqa: E501
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
    return controller.list_submissions(
        queue_id=queue_id,
        limit=limit,
        offset=offset
    )


def update_submission(
    queue_id,
    submission_id,
    unknown_base_type
):  # noqa: E501
    """Update a submission by its ID

    Updates the submission for a given ID # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str
    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: OneOfDockerSubmissionFileSubmissionWorkflowSubmission
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.update_submission(
        queue_id=queue_id,
        submission_id=submission_id,
        unknown_base_type=unknown_base_type
    )
