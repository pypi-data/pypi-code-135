from ._containers import *
from .entry import EntryEnvelope
from .entry_grant import SignedSharedEntryGrant
from .namespace_chain import NamespaceChain


class EntryChain(cord.Record):
    namespace_chain: NamespaceChain = cord.RecordField(NamespaceChain)
    entry: EntryEnvelope = cord.RecordField(EntryEnvelope)
    entry_grant: SignedSharedEntryGrant = cord.RecordField(SignedSharedEntryGrant)
