from mongoengine import StringField, ListField

from openapi_server.dbmodels.base_document import BaseDocument  # noqa: E501


class Queue(BaseDocument):
    name = StringField(required=True, unique=True)
    computeId = StringField(required=True, unique=True)
    workflowFiles = ListField(required=True, unique=True)
    workflowInput = StringField(required=True, unique=True)
    submissionType = StringField(required=True, unique=True)

    def to_dict(self):
        doc = self.to_mongo().to_dict()
        return doc
