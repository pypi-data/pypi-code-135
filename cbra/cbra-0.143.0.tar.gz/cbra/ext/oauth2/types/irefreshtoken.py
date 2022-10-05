# Copyright (C) 2022 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from .iclient import IClient
from .isubject import ISubject


class IRefreshToken:
    __module__: str = 'cbra.ext.oauth2.types'

    async def generate(self, client: IClient, subject: ISubject) -> str | None:
        """Generate a new refresh token for the given `client`."""
        raise NotImplementedError