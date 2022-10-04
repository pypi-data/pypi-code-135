from backbone.common import models

from ._factories import *


class SetEntryIngress(cord.Record):
    entry: models.EntryEnvelope = cord.RecordField(models.EntryEnvelope)
    entry_grant: models.SignedSharedEntryGrant = cord.RecordField(models.SignedSharedEntryGrant)


class SetWorkspaceEntryIngress(WorkspaceBound):
    data: SetEntryIngress = cord.RecordField(SetEntryIngress)


class FetchEntryChainIngress(cord.Record):
    path: str = cord.StringField()


class FetchWorkspaceEntryChainIngress(WorkspaceBound):
    data: FetchEntryChainIngress = cord.RecordField(FetchEntryChainIngress)


class FetchEntryChainEgress(cord.Record):
    entry_chain: models.EntryChain = cord.RecordField(models.EntryChain)


class DeleteEntryIngress(cord.Record):
    path: str = cord.StringField()


class DeleteWorkspaceEntryIngress(WorkspaceBound):
    data: DeleteEntryIngress = cord.RecordField(DeleteEntryIngress)


class CreateEntryGrantIngress(cord.Record):
    path: str = cord.StringField()
    entry_grant: models.SignedSharedEntryGrant = cord.RecordField(models.SignedSharedEntryGrant)


class CreateWorkspaceEntryGrantIngress(WorkspaceBound):
    data: CreateEntryGrantIngress = cord.RecordField(CreateEntryGrantIngress)


class ListEntryGrantsIngress(cord.Record):
    path: str = cord.StringField()


class ListWorkspaceEntryGrantsIngress(WorkspaceBound):
    data: ListEntryGrantsIngress = cord.RecordField(ListEntryGrantsIngress)


class ListEntryGrantsEgress(cord.Record):
    parent_chain: models.NamespaceChain = cord.RecordField(models.NamespaceChain)
    entry_grants: typing.List[models.SignedSharedEntryGrant] = cord.ListField(
        cord.RecordField(models.SignedSharedEntryGrant)
    )


class DeleteEntryGrantIngress(cord.Record):
    path: str = cord.StringField()
    recipient = cord.VariantField(models.EntryGrantRecipient)


class DeleteWorkspaceEntryGrantIngress(WorkspaceBound):
    data: DeleteEntryGrantIngress = cord.RecordField(DeleteEntryGrantIngress)
