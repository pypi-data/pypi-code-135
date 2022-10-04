from backbone.common import models

from ._factories import *


class FetchSelfEgress(cord.Record):
    user: models.SignedUser = cord.RecordField(models.SignedUser)


class CreateUserIngress(cord.Record):
    user: models.SignedUser = cord.RecordField(models.SignedUser)


class UpdateUserIngress(cord.Record):
    user: models.SignedUser = cord.RecordField(models.SignedUser)
