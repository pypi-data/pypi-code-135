#    MIT License - Valerio Vaccaro 2019-2022
#    Based on open source code

import configparser
from li.bitcoin_rpc_class import RPCHost
import json
import re
import struct
import requests
import hashlib
import sha256


class Issue:

    def __init__(self, configFile):
        self.configFile = configFile
        self.explorerURL = 'https://blockstream.info/liquid/api/tx/'

        config = configparser.RawConfigParser()
        config.read(self.configFile)

        rpcHost = config.get('LIQUID', 'host')
        rpcPort = config.get('LIQUID', 'port')
        rpcUser = config.get('LIQUID', 'username')
        rpcPassword = config.get('LIQUID', 'password')
        rpcPassphrase = config.get('LIQUID', 'passphrase')
        serverURL = 'http://' + rpcUser + ':' + \
            rpcPassword + '@'+rpcHost+':' + str(rpcPort)

        self.host = RPCHost(serverURL)

        if (len(rpcPassphrase) > 0):
            result = self.host.call('walletpassphrase', rpcPassphrase, 60)

    def getNewAddress(self):
        try:
            address = self.host.call('getnewaddress')
            return address
        except:
            return

    def getPubKey(self):
        try:
            address = self.host.call('getnewaddress')
            pubkey = self.host.call('getaddressinfo', address)['pubkey']
            return pubkey
        except:
            return

    def validAddress(self, address):
        try:
            res = self.host.call('getaddressinfo', address)
            if 'scriptPubKey' in res:
                return True
            else:
                return False
        except:
            return False

    def testTx(self, tx):
        return self.host.call('testmempoolaccept', [tx])

    def sendTx(self, tx):
        return self.host.call('sendrawtransaction', tx)

    def createTx(self,
                 asset_amount,
                 asset_address,
                 token_amount,
                 token_address,
                 prefix,
                 name,
                 ticker,
                 precision,
                 domain,
                 pubkey,
                 confidential
                 ):
        res = {}
        base = self.host.call('createrawtransaction', [], [{'data': prefix}])
        funded = self.host.call('fundrawtransaction', base, {
                                'feeRate': 0.00000300})
        decoded = self.host.call('decoderawtransaction', funded['hex'])
        prev_tx = decoded['vin'][0]['txid']
        prev_vout = decoded['vin'][0]['vout']

        for nonce in range(1, 256*256*256*256*256*256*256*256*256*256*256*256):

            contract_obj = {'name': name, 'ticker': ticker, 'precision': precision, 'entity': {
                'domain': domain}, 'issuer_pubkey': pubkey, 'nonce': str(nonce), 'version': 0}
            contract = json.dumps(
                contract_obj, separators=(',', ':'), sort_keys=True)

            sha256_c = hashlib.sha256()
            sha256_c.update(contract.encode('ascii'))
            contract_hash = sha256_c.hexdigest()

            a_pre = bytes.fromhex(
                prev_tx)[::-1].hex() + struct.pack('<L', int(prev_vout)).hex()
            sha256_d1 = hashlib.sha256()
            sha256_d2 = hashlib.sha256()
            sha256_d1.update(bytes.fromhex(a_pre))
            sha256_d2.update(sha256_d1.digest())
            a = sha256_d2.hexdigest()
            b = a + contract_hash

            sha256_m = sha256.sha256()
            sha256_m.update(bytes.fromhex(b))
            (midstate, num) = sha256_m.state
            merkle = midstate.hex()

            c = merkle + '0000000000000000000000000000000000000000000000000000000000000000'

            sha256_m = sha256.sha256()
            sha256_m.update(bytes.fromhex(c))
            (midstate, num) = sha256_m.state
            merkle = midstate[::-1].hex()

            if re.match(r'^'+prefix, merkle):
                break

        contract_hash_rev = bytes.fromhex((contract_hash))[::-1].hex()

        if token_amount > 0:
            rawissue = self.host.call('rawissueasset', funded['hex'], [{'asset_amount': asset_amount, 'asset_address': asset_address,
                                      'token_amount': token_amount, 'token_address': token_address, 'blind': confidential, 'contract_hash': contract_hash_rev}])
        else:
            rawissue = self.host.call('rawissueasset', funded['hex'], [
                                      {'asset_amount': asset_amount, 'asset_address': asset_address, 'blind': confidential, 'contract_hash': contract_hash_rev}])

        blind = self.host.call('blindrawtransaction',
                               rawissue[0]['hex'], True, [], False)
        signed = self.host.call('signrawtransactionwithwallet', blind)
        res['prevout'] = f'{prev_tx}:{prev_vout}'
        res['contract'] = contract_obj
        res['hex'] = signed['hex']
        res['asset_id'] = merkle
        return res

    def createTxNFT(self,
                    asset_amount,
                    asset_address,
                    name,
                    ticker,
                    precision,
                    domain,
                    pubkey,
                    confidential,
                    domainNFT,
                    hashNFT
                    ):
        res = {}
        base = self.host.call('createrawtransaction', [], [{'data': '4E4654'}])
        funded = self.host.call('fundrawtransaction', base, {
                                'feeRate': 0.00000300})
        decoded = self.host.call('decoderawtransaction', funded['hex'])
        prev_tx = decoded['vin'][0]['txid']
        prev_vout = decoded['vin'][0]['vout']

        contract_obj = {
            'name': name,
            'ticker': ticker,
            'precision': precision,
            'entity': {'domain': domain},
            'issuer_pubkey': pubkey,
            'nft': {'domain': domainNFT, 'hash': hashNFT},
            'version': 0,
        }
        contract = json.dumps(
            contract_obj, separators=(',', ':'), sort_keys=True)

        sha256_c = hashlib.sha256()
        sha256_c.update(contract.encode('ascii'))
        contract_hash = sha256_c.hexdigest()

        a_pre = bytes.fromhex(prev_tx)[::-1].hex() + \
            struct.pack('<L', int(prev_vout)).hex()
        sha256_d1 = hashlib.sha256()
        sha256_d2 = hashlib.sha256()
        sha256_d1.update(bytes.fromhex(a_pre))
        sha256_d2.update(sha256_d1.digest())
        a = sha256_d2.hexdigest()
        b = a + contract_hash

        sha256_m = sha256.sha256()
        sha256_m.update(bytes.fromhex(b))
        (midstate, num) = sha256_m.state
        merkle = midstate.hex()

        c = merkle + '0000000000000000000000000000000000000000000000000000000000000000'

        sha256_m = sha256.sha256()
        sha256_m.update(bytes.fromhex(c))
        (midstate, num) = sha256_m.state
        merkle = midstate[::-1].hex()

        contract_hash_rev = bytes.fromhex((contract_hash))[::-1].hex()

        rawissue = self.host.call('rawissueasset', funded['hex'], [
                                  {'asset_amount': asset_amount, 'asset_address': asset_address, 'blind': confidential, 'contract_hash': contract_hash_rev}])

        blind = self.host.call('blindrawtransaction',
                               rawissue[0]['hex'], True, [], False)
        signed = self.host.call('signrawtransactionwithwallet', blind)
        res['prevout'] = f'{prev_tx}:{prev_vout}'
        res['contract'] = contract_obj
        res['hex'] = signed['hex']
        res['asset_id'] = merkle
        return res

    def check_tx(self, issuance_txid, issuance_vin, asset, explorer):
        if (explorer):
            resp = requests.get(url=self.explorerURL +
                                issuance_txid, verify=True)
            issuance = resp.json()
            c = issuance['vin'][issuance_vin]['issuance']['asset_entropy'] + \
                '0000000000000000000000000000000000000000000000000000000000000000'

            sha256_m = sha256.sha256()
            sha256_m.update(bytes.fromhex(c))
            (midstate, num) = sha256_m.state
            asset_id = midstate[::-1].hex()
        else:
            issuance = self.host.call('getrawtransaction', issuance_txid, 1)
            asset_id = issuance['vin'][issuance_vin]['issuance']['asset']

        return asset_id == asset

    def check_contract(self, prev_tx, prev_vout, contract_hash, asset):
        a_pre = bytes.fromhex(prev_tx)[::-1].hex() + \
            struct.pack('<L', int(prev_vout)).hex()
        sha256_d1 = hashlib.sha256()
        sha256_d2 = hashlib.sha256()
        sha256_d1.update(bytes.fromhex(a_pre))
        sha256_d2.update(sha256_d1.digest())
        a = sha256_d2.hexdigest()
        b = a + contract_hash

        merkle = wally.hex_from_bytes(
            wally.sha256_midstate(wally.hex_to_bytes(b)))
        c = merkle + '0000000000000000000000000000000000000000000000000000000000000000'

        sha256_m = sha256.sha256()
        sha256_m.update(bytes.fromhex(c))
        (midstate, num) = sha256_m.state
        asset_id = midstate[::-1].hex()

        return asset_id == asset

    def check_website(self, domain, asset):
        asserURL = 'https://'+domain+'/.well-known/liquid-asset-proof-'+asset
        try:
            resp = requests.get(url=asserURL, verify=True)
        except:
            return False
        if (re.match(r'^.*'+domain+'.*'+asset, resp.text)):
            return True
        else:
            return False
