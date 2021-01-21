import connexion
import six

from openapi_server.models import CreateRunRequest  # noqa: E501
from openapi_server.models import CreateRunResponse  # noqa: E501
from openapi_server.models import Error  # noqa: E501
from openapi_server.models import Log  # noqa: E501
from openapi_server.models import Run  # noqa: E501
from openapi_server import util
from openapi_server.core.controllers import execution_controller as controller


def cancel_submission_run(
    queue_id,
    run_id,
    submission_id,
    body
):  # noqa: E501
    """Cancels a submission&#39;s run

    Cancels the submission&#39;s run for a given run ID. This is dependant on how the compute environment cancels runs. # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param run_id: The ID of the run
    :type run_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str
    :param body: 
    :type body: 

    :rtype: None
    """
    return controller.cancel_submission_run(
        queue_id=queue_id,
        run_id=run_id,
        submission_id=submission_id,
        body=body
    )


def delete_submission_run(
    queue_id,
    run_id,
    submission_id
):  # noqa: E501
    """Delete a submission run

    Deletes the run for a submission # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param run_id: The ID of the run
    :type run_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: None
    """
    return controller.delete_submission_run(
        queue_id=queue_id,
        run_id=run_id,
        submission_id=submission_id
    )


def get_submission_run(
    queue_id,
    run_id,
    submission_id
):  # noqa: E501
    """Get a submission run

    Returns the run for a submission # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param run_id: The ID of the run
    :type run_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: Run
    """
    return controller.get_submission_run(
        queue_id=queue_id,
        run_id=run_id,
        submission_id=submission_id
    )


def get_submission_run_log(
    queue_id,
    run_id,
    submission_id
):  # noqa: E501
    """Get a submission&#39;s run logs

    Returns the submission&#39;s logs for a given run ID. This is dependant on how the compute environment returns logs. # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param run_id: The ID of the run
    :type run_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str

    :rtype: Log
    """
    return controller.get_submission_run_log(
        queue_id=queue_id,
        run_id=run_id,
        submission_id=submission_id
    )


def run_submission(
    queue_id,
    submission_id,
    create_run_request
):  # noqa: E501
    """Executes a submission

    Executes a submission # noqa: E501

    :param queue_id: The ID of the queue
    :type queue_id: str
    :param submission_id: The ID of the submission
    :type submission_id: str
    :param create_run_request: 
    :type create_run_request: dict | bytes

    :rtype: CreateRunResponse
    """
    if connexion.request.is_json:
        create_run_request = CreateRunRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return controller.run_submission(
        queue_id=queue_id,
        submission_id=submission_id,
        create_run_request=create_run_request
    )
