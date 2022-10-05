# *--------------------------------------------------------------*
# | _    _      _ _        _____       _____ _           _       |
# || |  | |    (_) |      |  _  |     /  __ \ |         (_)      |
# || |  | |_ __ _| |_ ___ | | | |_ __ | /  \/ |__   __ _ _ _ __  |
# || |/\| | '__| | __/ _ \| | | | '_ \| |   | '_ \ / _` | | '_ \ |
# |\  /\  / |  | | ||  __/\ \_/ / | | | \__/\ | | | (_| | | | | ||
# | \/  \/|_|  |_|\__\___| \___/|_| |_|\____/_| |_|\__,_|_|_| |_||
# *--------------------------------------------------------------*
# |                   Write on chain - 2018-2022                 |
# *--------------------------------------------------------------*
#    MIT License - Valerio Vaccaro 2018-2022
#    Based on open source code

import configparser
from woc.bitcoin_rpc_class import RPCHost


class Write:

    def __init__(self, configFile, chain):
        self.chain = chain
        self.configFile = configFile

    def sendTx(self, text):
        self.text = text

        config = configparser.RawConfigParser()
        config.read(self.configFile)

        if (self.chain == 'LIQUID'):
            rpcHost = config.get('LIQUID', 'host')
            rpcPort = config.get('LIQUID', 'port')
            rpcUser = config.get('LIQUID', 'username')
            rpcPassword = config.get('LIQUID', 'password')
            rpcPassphrase = config.get('LIQUID', 'passphrase')
            serverURL = 'http://' + rpcUser + ':' + \
                rpcPassword + '@'+rpcHost+':' + str(rpcPort)
        elif (self.chain == 'BTC'):
            rpcHost = config.get('BTC', 'host')
            rpcPort = config.get('BTC', 'port')
            rpcUser = config.get('BTC', 'username')
            rpcPassword = config.get('BTC', 'password')
            rpcWallet = config.get('BTC', 'wallet')
            rpcPassphrase = config.get('BTC', 'passphrase')
            serverURL = 'http://' + rpcUser + ':' + rpcPassword + \
                '@'+rpcHost+':' + str(rpcPort)+'/wallet/' + rpcWallet
        elif (self.chain == 'tBTC'):
            rpcHost = config.get('tBTC', 'host')
            rpcPort = config.get('tBTC', 'port')
            rpcUser = config.get('tBTC', 'username')
            rpcPassword = config.get('tBTC', 'password')
            rpcWallet = config.get('tBTC', 'wallet')
            rpcPassphrase = config.get('tBTC', 'passphrase')
            serverURL = 'http://' + rpcUser + ':' + rpcPassword + \
                '@'+rpcHost+':' + str(rpcPort)+'/wallet/' + rpcWallet
        elif (self.chain == 'LTC'):
            rpcHost = config.get('LTC', 'host')
            rpcPort = config.get('LTC', 'port')
            rpcUser = config.get('LTC', 'username')
            rpcPassword = config.get('LTC', 'password')
            rpcWallet = config.get('LTC', 'wallet')
            rpcPassphrase = config.get('LTC', 'passphrase')
            serverURL = 'http://' + rpcUser + ':' + rpcPassword + \
                '@'+rpcHost+':' + str(rpcPort)+'/wallet/' + rpcWallet
        elif (self.chain == 'tLTC'):
            rpcHost = config.get('tLTC', 'host')
            rpcPort = config.get('tLTC', 'port')
            rpcUser = config.get('tLTC', 'username')
            rpcPassword = config.get('tLTC', 'password')
            rpcWallet = config.get('tLTC', 'wallet')
            rpcPassphrase = config.get('tLTC', 'passphrase')
            serverURL = 'http://' + rpcUser + ':' + rpcPassword + \
                '@'+rpcHost+':' + str(rpcPort)+'/wallet/' + rpcWallet
        else:
            print("ERROR: unknow chain ")

        print(self.chain)

        host = RPCHost(serverURL)

        print(
            '............[Write On Chain: passphrase].................................')
        if (len(rpcPassphrase) > 0):
            result = host.call('walletpassphrase', rpcPassphrase, 60)
            print(result)

        print(
            '............[Write On Chain: input]......................................')
        data = self.text.encode('utf_8').hex()
        print(data)

        print(
            '............[Write On Chain: createrwatransaction].......................')
        raw_transaction = host.call('createrawtransaction', [], {"data": data})
        print(raw_transaction)

        print(
            '............[Write On Chain: fundrawtransaction].........................')
        raw_transaction_funded = host.call(
            'fundrawtransaction', raw_transaction)
        print(raw_transaction_funded)

        if (self.chain == 'LIQUID'):
            print(
                '............[Write On Chain: blindrawtransaction].........................')
            raw_transaction_funded = host.call(
                'blindrawtransaction', raw_transaction_funded['hex'])
            print(raw_transaction_funded)

        print(
            '............[Write On Chain: signrawtransaction].........................')
        if ((self.chain == 'BTC') or (self.chain == 'tBTC')):
            signed_transaction = host.call(
                'signrawtransactionwithwallet', raw_transaction_funded['hex'])
        elif ((self.chain == 'LTC') or (self.chain == 'tLTC')):
            signed_transaction = host.call(
                'signrawtransaction', raw_transaction_funded['hex'])
        elif (self.chain == 'LIQUID'):
            signed_transaction = host.call(
                'signrawtransactionwithwallet', raw_transaction_funded)
        print(signed_transaction)

        print(
            '............[Write On Chain: sendrawtransaction].........................')
        transaction = host.call('sendrawtransaction',
                                signed_transaction['hex'])
        print(transaction)

        print(
            '............[Write On Chain: END]........................................')
        return transaction
