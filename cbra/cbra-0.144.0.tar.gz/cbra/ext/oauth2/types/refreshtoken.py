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
from unimatrix.exceptions import CanonicalException

from .iclient import IClient
from .irefreshtoken import IRefreshToken
from .isubject import ISubject
from .invalidrefreshtoken import InvalidRefreshToken


KEY_LENGTH: int = 64


class RefreshToken(pydantic.BaseModel, IRefreshToken):
    authorization_id: int
    id: int | None = None
    sub: int | str
    client_id: str
    secret: str
    created: datetime.datetime
    exchanged: datetime.datetime
    expires: datetime.datetime | None = None
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
        authorization_id: int,
        client_id: int | str,
        sub: int | str,
        scope: list[str] | set[str]
    ) -> 'RefreshToken':
        now = datetime.datetime.utcnow()
        return cls.parse_obj({
            'authorization_id': authorization_id,
            'client_id': client_id,
            'sub': sub,
            'secret': secrets.token_urlsafe(KEY_LENGTH),
            'created': now,
            'exchanged': now,
            'scope': scope
        })

    @classmethod
    def parse_jwt(
        cls,
        client_id: int | str,
        token: str
    ) -> int:
        try:
            _, jwt = PayloadCodec.introspect(
                token=token,
                accept={"rt+jwt"}
            )
            if jwt is None:
                raise InvalidRefreshToken
            jwt.verify(audience={str(client_id)})
        except (CanonicalException, ValueError, TypeError):
            raise InvalidRefreshToken
        assert jwt.iss is not None # nosec
        return int(jwt.iss)

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
            token_id=self.id,
            expires=self.expires
        )