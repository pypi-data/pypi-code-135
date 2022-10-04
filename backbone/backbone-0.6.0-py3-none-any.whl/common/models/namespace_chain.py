from ._containers import *
from .namespace import SignedNamespace
from .namespace_grant import SignedSharedNamespaceGrant
from .workspace import SignedWorkspace
from .workspace_grant import SignedSharedWorkspaceGrant


class NamespaceChain(cord.Record):
    workspace: SignedWorkspace = cord.RecordField(SignedWorkspace)
    workspace_grant: typing.Optional[SignedSharedWorkspaceGrant] = cord.OptionalField(
        cord.RecordField(SignedSharedWorkspaceGrant)
    )
    namespaces: typing.List[SignedNamespace] = cord.ListField(cord.RecordField(SignedNamespace))
    namespace_grants: typing.List[SignedSharedNamespaceGrant] = cord.ListField(
        cord.RecordField(SignedSharedNamespaceGrant)
    )
