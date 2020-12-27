import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.one_of_docker_submission_file_submission_workflow_submission import OneOfDockerSubmissionFileSubmissionWorkflowSubmission  # noqa: E501
from openapi_server.models.unknownbasetype import UNKNOWN_BASE_TYPE  # noqa: E501
from openapi_server import util


def create_submission(unknown_base_type=None):  # noqa: E501
    """Create a submission

    Creates a submission # noqa: E501

    :param unknown_base_type: 
    :type unknown_base_type: dict | bytes

    :rtype: OneOfDockerSubmissionFileSubmissionWorkflowSubmission
    """
    if connexion.request.is_json:
        unknown_base_type = UNKNOWN_BASE_TYPE.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
