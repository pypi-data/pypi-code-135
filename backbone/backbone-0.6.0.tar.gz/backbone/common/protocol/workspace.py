from backbone.common import models

from ._factories import *


class FetchWorkspaceEgress(cord.Record):
    workspace = cord.RecordField(models.SignedWorkspace)
    workspace_grants = cord.ListField(cord.RecordField(models.SignedSharedWorkspaceGrant))


class CreateWorkspaceIngress(cord.Record):
    workspace: models.SignedWorkspace = cord.RecordField(models.SignedWorkspace)
    workspace_grant: models.SignedSharedWorkspaceGrant = cord.RecordField(models.SignedSharedWorkspaceGrant)

    namespace: models.SignedNamespace = cord.RecordField(models.SignedNamespace)
    namespace_grant: models.SignedSharedNamespaceGrant = cord.RecordField(models.SignedSharedNamespaceGrant)


class FetchWorkspaceGrantsEgress(cord.Record):
    grants: typing.List[models.SignedSharedWorkspaceGrant] = cord.ListField(
        cord.RecordField(models.SignedSharedWorkspaceGrant)
    )


class CreateWorkspaceGrantIngress(WorkspaceBound):
    data: models.SignedSharedWorkspaceGrant = cord.RecordField(models.SignedSharedWorkspaceGrant)


class WorkspaceGrantUserReference(cord.Record):
    user_name = cord.StringField()


class FetchWorkspaceGrantIngress(WorkspaceBound):
    data: WorkspaceGrantUserReference = cord.RecordField(WorkspaceGrantUserReference)


class FetchWorkspaceGrantEgress(cord.Record):
    workspace = cord.RecordField(models.SignedWorkspace)
    workspace_grant = cord.RecordField(models.SignedSharedWorkspaceGrant)


class DeleteWorkspaceGrantIngress(WorkspaceBound):
    data: WorkspaceGrantUserReference = cord.RecordField(WorkspaceGrantUserReference)
