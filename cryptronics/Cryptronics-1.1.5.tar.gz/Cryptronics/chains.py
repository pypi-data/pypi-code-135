# Litecoin dep's
from litecoinutils.keys import PrivateKey
from litecoinutils.setup import setup

# Tron dep's
from tronapi import Tron


class Litecoin(object):
    def __init__(
        self,
        address: str,
        port: int,
        username: str = None,
        password: str = None
    ):
        setup('mainnet')
        # self.PROXY = NodeProxy(
        #     rpcuser=username,
        #     rpcpassword=password,
        #     host=address,
        #     port=port
        # )

    def generate_wallet(self):
        priv = PrivateKey()
        pub = priv.get_public_key()
        return [priv.to_wif(), pub.get_address().to_string()]


class Binance(object):
    pass


class Doge(object):
    pass


class Xmr(object):
    pass


class TronChain(object):
    def __init__(
        self,
        full_node: str = None,
        solidity_node: str = None,
        event_server: str = None
    ):
        """Initial

        Args:
            full_node (str, optional): Full trx node address
            solidity_node (str, optional): Full solidity node address
            event_server (str, optional): Event server address
        """
        self.FULL_NODE = full_node
        self.SOLIDITY_NODE = solidity_node
        self.EVENT_SERVER = event_server
        self.TRON = Tron(
            full_node=full_node,
            solidity_node=solidity_node,
            event_server=event_server
        )

    def generate_account(self):
        account = self.TRON.create_account
        return {
            'public': account.public_key,
            'private': account.private_key
        }

    def send(
        self,
        to: str,
        amount: float
    ):
        pass


if __name__ == '__main__':
    # ltc = Litecoin(address='127.0.0.1', port=1234)
    # private, public = ltc.generate_wallet()
    # print(f"Private: {private}")
    # print(f"Public: {public}")

    full_node = 'https://api.trongrid.io'
    solidity_node = 'https://api.trongrid.io'
    event_server = 'https://api.trongrid.io'

    trx = TronChain()
    account = trx.generate_account()
    print(account)
