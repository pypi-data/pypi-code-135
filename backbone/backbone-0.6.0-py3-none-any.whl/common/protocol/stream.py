from backbone.common import models

from ._factories import *


class PublishStreamIngressData(cord.Record):
    data: typing.List[models.SignedSharedStreamBytes] = cord.ListField(cord.RecordField(models.SignedSharedStreamBytes))


class PublishStreamIngress(StreamBound):
    data: PublishStreamIngressData = cord.RecordField(PublishStreamIngressData)


class PublishWorkspaceStreamIngress(WorkspaceBound):
    data: PublishStreamIngress = cord.RecordField(PublishStreamIngress)


class ConsumeStreamIngressMetadata(cord.Record):
    shared: bool = cord.BooleanField()
    batch: int = cord.UnsignedIntegerField()


class ConsumeStreamIngress(StreamBound):
    data: ConsumeStreamIngressMetadata = cord.RecordField(ConsumeStreamIngressMetadata)


class ConsumeWorkspaceStreamIngress(WorkspaceBound):
    data: ConsumeStreamIngress = cord.RecordField(ConsumeStreamIngress)


class ConsumeStreamEgress(cord.Record):
    data: typing.List[models.SignedSharedStreamBytes] = cord.ListField(cord.RecordField(models.SignedSharedStreamBytes))
