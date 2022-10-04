from backbone.common import models

from ._factories import *


class CreateNamespaceIngress(cord.Record):
    namespace: models.SignedNamespace = cord.RecordField(models.SignedNamespace)
    namespace_grant: models.SignedSharedNamespaceGrant = cord.RecordField(models.SignedSharedNamespaceGrant)


class CreateWorkspaceNamespaceIngress(WorkspaceBound):
    data: CreateNamespaceIngress = cord.RecordField(CreateNamespaceIngress)


class FetchNamespaceChainIngress(cord.Record):
    path: str = cord.StringField()


class FetchWorkspaceNamespaceChainIngress(WorkspaceBound):
    data: FetchNamespaceChainIngress = cord.RecordField(FetchNamespaceChainIngress)


class FetchNamespaceChainEgress(cord.Record):
    namespace_chain: models.NamespaceChain = cord.RecordField(models.NamespaceChain)


class ListNamespaceChildrenIngress(cord.Record):
    path: str = cord.StringField()


class ListWorkspaceNamespaceChildrenIngress(WorkspaceBound):
    data: ListNamespaceChildrenIngress = cord.RecordField(ListNamespaceChildrenIngress)


class ListNamespaceChildrenEgress(cord.Record):
    parent_chain: models.NamespaceChain = cord.RecordField(models.NamespaceChain)
    namespaces: typing.List[models.SignedNamespace] = cord.ListField(cord.RecordField(models.SignedNamespace))
    entries: typing.List[models.SignedEntry] = cord.ListField(cord.RecordField(models.SignedEntry))


class DeleteNamespaceIngress(cord.Record):
    path: str = cord.StringField()


class DeleteWorkspaceNamespaceIngress(WorkspaceBound):
    data: DeleteNamespaceIngress = cord.RecordField(DeleteNamespaceIngress)


class CreateNamespaceGrantIngress(cord.Record):
    path: str = cord.StringField()
    namespace_grant: models.SignedSharedNamespaceGrant = cord.RecordField(models.SignedSharedNamespaceGrant)


class CreateWorkspaceNamespaceGrantIngress(WorkspaceBound):
    data: CreateNamespaceGrantIngress = cord.RecordField(CreateNamespaceGrantIngress)


class ListNamespaceGrantsIngress(cord.Record):
    path: str = cord.StringField()


class ListWorkspaceNamespaceGrantsIngress(WorkspaceBound):
    data: ListNamespaceGrantsIngress = cord.RecordField(ListNamespaceGrantsIngress)


class ListNamespaceGrantsEgress(cord.Record):
    parent_chain: models.NamespaceChain = cord.RecordField(models.NamespaceChain)
    namespace_grants: typing.List[models.SignedSharedNamespaceGrant] = cord.ListField(
        cord.RecordField(models.SignedSharedNamespaceGrant)
    )


class DeleteNamespaceGrantIngress(cord.Record):
    path: str = cord.StringField()
    recipient = cord.VariantField(models.NamespaceGrantRecipient)


class DeleteWorkspaceNamespaceGrantIngress(WorkspaceBound):
    data: DeleteNamespaceGrantIngress = cord.RecordField(DeleteNamespaceGrantIngress)
