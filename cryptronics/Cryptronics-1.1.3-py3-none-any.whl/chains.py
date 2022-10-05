from litecoinutils.proxy import NodeProxy
from litecoinutils.keys import PrivateKey
from litecoinutils.setup import setup


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


if __name__ == '__main__':
    ltc = Litecoin(address='127.0.0.1', port=1234)
    private, public = ltc.generate_wallet()
    print(f"Private: {private}")
    print(f"Public: {public}")
