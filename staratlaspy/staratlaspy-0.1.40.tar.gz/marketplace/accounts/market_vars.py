import typing
from dataclasses import dataclass
from base64 import b64decode
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
import borsh_construct as borsh
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from anchorpy.borsh_extension import BorshPubkey
from ..program_id import PROGRAM_ID


class MarketVarsJSON(typing.TypedDict):
    update_authority_master: str
    bump: int


@dataclass
class MarketVars:
    discriminator: typing.ClassVar = b"\xff\x8e\x86\x198\x01\xdb|"
    layout: typing.ClassVar = borsh.CStruct(
        "update_authority_master" / BorshPubkey, "bump" / borsh.U8
    )
    update_authority_master: PublicKey
    bump: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.Optional["MarketVars"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp["result"]["value"]
        if info is None:
            return None
        if info["owner"] != str(PROGRAM_ID):
            raise ValueError("Account does not belong to this program")
        bytes_data = b64decode(info["data"][0])
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[PublicKey],
        commitment: typing.Optional[Commitment] = None,
    ) -> typing.List[typing.Optional["MarketVars"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["MarketVars"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != PROGRAM_ID:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "MarketVars":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = MarketVars.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            update_authority_master=dec.update_authority_master,
            bump=dec.bump,
        )

    def to_json(self) -> MarketVarsJSON:
        return {
            "update_authority_master": str(self.update_authority_master),
            "bump": self.bump,
        }

    @classmethod
    def from_json(cls, obj: MarketVarsJSON) -> "MarketVars":
        return cls(
            update_authority_master=PublicKey(obj["update_authority_master"]),
            bump=obj["bump"],
        )
