from django.db import models


class WorkflowManager(models.Manager):
    """工作流Manager"""
    def launch_for(self, document):
        for workflow in document.document_type.workflows.all():
            workflow.launch_for(document)
