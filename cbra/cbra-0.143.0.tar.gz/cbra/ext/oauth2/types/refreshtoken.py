# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
import datetime
import secrets
from typing import Any

import pydantic
from ckms.core import parse_spec
from ckms.core import KeySpecification
from ckms.jose import PayloadCodec
from ckms.utils import b64decode

from .iclient import IClient
from .irefreshtoken import IRefreshToken
from .isubject import ISubject


KEY_LENGTH: int = 64


class RefreshToken(pydantic.BaseModel, IRefreshToken):
    id: int | None = None
    sub: int | str
    client_id: str
    secret: str
    created: datetime.datetime
    exchanged: datetime.datetime
    scope: list[str]

    @pydantic.root_validator(pre=True)
    def preprocess(
        cls,
        values: dict[str, Any]
    ) -> dict[str, Any]:
        values.setdefault('secret', secrets.token_urlsafe(KEY_LENGTH))
        return values

    @classmethod
    def new(
        cls,
        client_id: str,
        sub: int | str,
        scope: list[str] | set[str]
    ) -> 'RefreshToken':
        now = datetime.datetime.utcnow()
        return cls.parse_obj({
            'client_id': client_id,
            'sub': sub,
            'secret': secrets.token_urlsafe(KEY_LENGTH),
            'created': now,
            'exchanged': now,
            'scope': scope
        })

    @property
    def key(self) -> KeySpecification:
        return parse_spec({
            'provider': 'local',
            'kty': 'oct',
            'alg': 'HS256',
            'use': 'sig',
            'key': {'cek': b64decode(self.secret)}
        })

    async def get_codec(self) -> PayloadCodec:
        return PayloadCodec(signing_keys=[await self.key])

    async def generate(self, client: IClient, subject: ISubject) -> str | None:
        assert self.id is not None # nosec
        self.exchanged = datetime.datetime.utcnow()
        self.secret = secrets.token_urlsafe(KEY_LENGTH)
        return await client.create_refresh_token(
            codec=await self.get_codec(),
            subject=subject,
            token_id=self.id
        )