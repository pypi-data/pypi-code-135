import sys
import os
from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
import sys
import os
import os.path
import configparser
import json
import requests
from li.issue import Issue


class AppWindow():
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        bundle_dir = getattr(
            sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        path_to_dialog_ui = os.path.abspath(
            os.path.join(bundle_dir, 'dialog.ui'))
        self.ui = loader.load(path_to_dialog_ui, None)

        self.directory = os.path.expanduser('~') + '/liquidissuer/'
        self.config_file = self.directory + 'main.conf'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        if not os.path.isfile(self.config_file):
            self.on_btn_config_save_clicked()
        else:
            self.on_btn_config_load_clicked()

        self.ui.btn_create.clicked.connect(self.on_btn_create_clicked_send)
        self.ui.btn_test.clicked.connect(self.on_btn_test_clicked_send)
        self.ui.btn_broadcast.clicked.connect(
            self.on_btn_broadcast_clicked_send)

        self.ui.btn_getaddresses.clicked.connect(
            self.on_btn_getaddresses_clicked_send)
        self.ui.btn_getpubkey.clicked.connect(
            self.on_btn_getpubkey_clicked_send)

        self.ui.btn_proof.clicked.connect(self.on_btn_proof_clicked_send)
        self.ui.btn_register.clicked.connect(self.on_btn_register_clicked_send)
        self.ui.btn_check.clicked.connect(self.on_btn_check_clicked_send)

        self.ui.btn_config_load.clicked.connect(
            self.on_btn_config_load_clicked)
        self.ui.btn_config_save.clicked.connect(
            self.on_btn_config_save_clicked)

        self.ui.btn_create_nft.clicked.connect(
            self.on_btn_create_nft_clicked_send)
        self.ui.btn_test_nft.clicked.connect(self.on_btn_test_clicked_nft_send)
        self.ui.btn_broadcast_nft.clicked.connect(
            self.on_btn_broadcast_clicked_nft_send)

        self.ui.btn_getaddresses_nft.clicked.connect(
            self.on_btn_getaddresses_nft_clicked_send)
        self.ui.btn_getpubkey_nft.clicked.connect(
            self.on_btn_getpubkey_nft_clicked_send)

        self.ui.btn_checkcontract_nft.clicked.connect(
            self.on_btn_checkcontract_nft_clicked_send)

        self.transaction = ''
        self.contract = ''
        self.asset_id = ''

    def on_btn_checkcontract_nft_clicked_send(self):
        url = self.ui.txt_contract_nft.text()
        print(url)
        try:
            r = requests.get(url, allow_redirects=True)
            if r.status_code != 200:
                self.ui.txt_result_nft.setText(
                    f'Wrong contract URL - status code: {r.status_code}.')
                self.ui.repaint()
                return
            payload = r.json()
            self.ui.txt_result_nft.setText(str(payload))
            self.domainNFT = url[8:].split('/')[0]
            self.hashNFT = url[:-5].split('nft-')[1]
            self.ui.btn_create_nft.setEnabled(True)
        except:
            self.ui.txt_result_nft.setText('Wrong contract URL.')
        self.ui.repaint()

    def on_btn_getaddresses_clicked_send(self):
        i = Issue(self.config_file)
        self.ui.txt_asset_address.setText(i.getNewAddress())
        self.ui.txt_token_address.setText(i.getNewAddress())
        self.ui.repaint()

    def on_btn_getaddresses_nft_clicked_send(self):
        i = Issue(self.config_file)
        self.ui.txt_asset_address_nft.setText(i.getNewAddress())
        self.ui.repaint()

    def on_btn_getpubkey_clicked_send(self):
        i = Issue(self.config_file)
        self.ui.txt_pubkey.setText(i.getPubKey())
        self.ui.repaint()

    def on_btn_getpubkey_nft_clicked_send(self):
        i = Issue(self.config_file)
        self.ui.txt_pubkey_nft.setText(i.getPubKey())
        self.ui.repaint()

    def on_btn_create_clicked_send(self):
        i = Issue(self.config_file)
        # get and check elements
        asset_amount = self.ui.spin_amount.value()
        if asset_amount < 0 or asset_amount > 21000000 * 10 ** 8 + 1:
            self.ui.txt_result.setText('Wrong asset amount.')
            self.ui.repaint()
            return
        asset_address = self.ui.txt_asset_address.text()
        if not i.validAddress(asset_address):
            self.ui.txt_result.setText('Wrong asset address.')
            self.ui.repaint()
            return

        token_amount = self.ui.spin_token.value()
        if token_amount > 21000000 * 10**8 + 1:
            self.ui.txt_result.setText('Wrong token amount.')
            self.ui.repaint()
            return
        token_address = ''
        if token_amount > 0:
            token_address = self.ui.txt_token_address.text()
            if not i.validAddress(token_address):
                self.ui.txt_result.setText('Wrong token address.')
                self.ui.repaint()
                return

        prefix = self.ui.txt_prefix.text()
        if len(prefix) > 8:
            self.ui.txt_result.setText('Wrong prefix.')
            self.ui.repaint()
            return

        name = self.ui.txt_name.text()
        if len(name) < 1 or len(name) > 255:
            self.ui.txt_result.setText('Wrong asset name.')
            self.ui.repaint()
            return
        ticker = self.ui.txt_ticker.text()
        if len(ticker) < 3 or len(ticker) > 5:
            self.ui.txt_result.setText('Wrong asset ticker.')
            self.ui.repaint()
            return
        precision = self.ui.spin_precision.value()
        if precision < 0 or precision > 8:
            self.ui.txt_result.setText('Wrong asset precision.')
            self.ui.repaint()
            return
        domain = self.ui.txt_domain.text()
        pubkey = self.ui.txt_pubkey.text()
        confidential = self.ui.check_confidential.isChecked()

        i = Issue(self.config_file)
        res = i.createTx(
            asset_amount / 10 ** (8 - precision),
            asset_address,
            token_amount / 10 ** 8,
            token_address,
            prefix,
            name,
            ticker,
            precision,
            domain,
            pubkey,
            confidential
        )
        self.contract = res['contract']
        self.transaction = res['hex']
        self.asset_id = res['asset_id']
        self.ui.txt_result.setText('Issuance of asset {} with contract \n{}\n READY'.format(
            self.asset_id, str(self.contract)))

        # update registry
        self.domain = self.contract['entity']['domain']
        self.proof = 'Authorize linking the domain name {} to the Liquid asset {}'.format(
            self.domain, self.asset_id)
        self.ui.txt_proof.setText(
            'Create a file on https://{}/.well-known/liquid-asset-proof-{} with content\n{}'.format(self.domain, self.asset_id, self.proof))
        command = {
            'asset_id': self.asset_id,
            'contract': self.contract,
        }
        command_str = json.dumps(
            command, separators=(',', ':'), sort_keys=True)
        self.command = 'curl https://assets.blockstream.info/ --data-raw \'{}\''.format(
            command_str)
        self.ui.txt_register.setText(
            'Execute the following command\n{}'.format(self.command))

        # save logs
        os.mkdir(self.directory + self.asset_id)

        f = open(self.directory + self.asset_id + '/logs.txt', 'a')
        f.write('Issuance of asset {} with contract \n{}\n READY\n'.format(
            self.asset_id, str(self.contract)))
        f.write('Create a file on https://{}/.well-known/liquid-asset-proof-{} with content\n{}\n'.format(
            self.domain, self.asset_id, self.proof))
        f.write('Execute the following command\n{}\n'.format(self.command))
        f.close()

        f = open(self.directory + self.asset_id + '/register.sh', 'a')
        f.write(self.command)
        f.close()

        f = open(self.directory + self.asset_id +
                 '/liquid-asset-proof-' + self.asset_id, 'a')
        f.write(self.proof)
        f.close()

        # enable buttons
        self.ui.btn_test.setEnabled(True)
        self.ui.btn_broadcast.setEnabled(True)
        self.ui.btn_proof.setEnabled(True)
        self.ui.btn_register.setEnabled(True)
        self.ui.btn_check.setEnabled(True)
        self.ui.repaint()

    def on_btn_create_nft_clicked_send(self):
        i = Issue(self.config_file)
        # get and check elements
        asset_amount = self.ui.spin_amount_nft.value()
        if asset_amount < 0 or asset_amount > 21000000 * 10 ** 8 + 1:
            self.ui.txt_result_nft.setText('Wrong asset amount.')
            self.ui.repaint()
            return
        asset_address = self.ui.txt_asset_address_nft.text()
        if not i.validAddress(asset_address):
            self.ui.txt_result_nft.setText('Wrong asset address.')
            self.ui.repaint()
            return
        token_amount = 0
        token_address = ''
        prefix = '77'
        name = self.ui.txt_name_nft.text()
        if len(name) < 1 or len(name) > 255:
            self.ui.txt_result_nft.setText('Wrong asset name.')
            self.ui.repaint()
            return
        ticker = self.ui.txt_ticker_nft.text()
        if len(ticker) < 3 or len(ticker) > 5:
            self.ui.txt_result_nft.setText('Wrong asset ticker.')
            self.ui.repaint()
            return
        precision = 0
        domain = self.ui.txt_domain_nft.text()
        pubkey = self.ui.txt_pubkey_nft.text()
        confidential = False

        domain = self.ui.txt_domain_nft.text()
        pubkey = self.ui.txt_pubkey_nft.text()

        i = Issue(self.config_file)
        res = i.createTxNFT(
            asset_amount / 10 ** (8 - precision),
            asset_address,
            name,
            ticker,
            precision,
            domain,
            pubkey,
            confidential,
            self.domainNFT,
            self.hashNFT
        )
        self.contract = res['contract']
        self.transaction = res['hex']
        self.asset_id = res['asset_id']
        self.ui.txt_result_nft.setText('Issuance of asset {} with contract \n{}\n READY'.format(
            self.asset_id, str(self.contract)))

        # update registry
        self.domain = self.contract['entity']['domain']
        self.proof = 'Authorize linking the domain name {} to the Liquid asset {}'.format(
            self.domain, self.asset_id)
        self.ui.txt_proof.setText(
            'Create a file on https://{}/.well-known/liquid-asset-proof-{} with content\n{}'.format(self.domain, self.asset_id, self.proof))
        command = {
            'asset_id': self.asset_id,
            'contract': self.contract,
        }
        command_str = json.dumps(
            command, separators=(',', ':'), sort_keys=True)
        self.command = 'curl https://assets.blockstream.info/ --data-raw \'{}\''.format(
            command_str)
        self.ui.txt_register.setText(
            'Execute the following command\n{}'.format(self.command))

        # save logs
        os.mkdir(self.directory + self.asset_id)

        f = open(self.directory + self.asset_id + '/logs.txt', 'a')
        f.write('Issuance of asset {} with contract \n{}\n READY\n'.format(
            self.asset_id, str(self.contract)))
        f.write('Create a file on https://{}/.well-known/liquid-asset-proof-{} with content\n{}\n'.format(
            self.domain, self.asset_id, self.proof))
        f.write('Execute the following command\n{}\n'.format(self.command))
        f.close()

        f = open(self.directory + self.asset_id + '/register.sh', 'a')
        f.write(self.command)
        f.close()

        f = open(self.directory + self.asset_id +
                 '/liquid-asset-proof-' + self.asset_id, 'a')
        f.write(self.proof)
        f.close()

        # enable buttons
        self.ui.btn_test_nft.setEnabled(True)
        self.ui.btn_broadcast_nft.setEnabled(True)
        self.ui.btn_proof.setEnabled(True)
        self.ui.btn_register.setEnabled(True)
        self.ui.btn_check.setEnabled(True)
        self.ui.repaint()

    def on_btn_test_clicked_send(self):
        i = Issue(self.config_file)
        res = i.testTx(self.transaction)
        self.ui.txt_result.setText(str(res))
        self.ui.repaint()

        # save in logs
        f = open(self.directory + self.asset_id + '/logs.txt', 'a')
        f.write('Testing\n' + str(res) + '\n')
        f.close()

    def on_btn_broadcast_clicked_send(self):
        i = Issue(self.config_file)
        res = i.sendTx(self.transaction)
        self.ui.txt_result.setText(str(res))
        self.ui.btn_test.setEnabled(False)
        self.ui.btn_broadcast.setEnabled(False)
        self.ui.repaint()

        # save in logs
        f = open(self.directory + self.asset_id + '/logs.txt', 'a')
        f.write('Broadcast\n' + str(res) + '\n')
        f.close()

    def on_btn_test_clicked_nft_send(self):
        i = Issue(self.config_file)
        res = i.testTx(self.transaction)
        self.ui.txt_result_nft.setText(str(res))
        self.ui.repaint()

        # save in logs
        f = open(self.directory + self.asset_id + '/logs.txt', 'a')
        f.write('Testing\n' + str(res) + '\n')
        f.close()

    def on_btn_broadcast_clicked_nft_send(self):
        i = Issue(self.config_file)
        res = i.sendTx(self.transaction)
        self.ui.txt_result_nft.setText(str(res))
        self.ui.btn_test_nft.setEnabled(False)
        self.ui.btn_broadcast_nft.setEnabled(False)
        self.ui.repaint()

        # save in logs
        f = open(self.directory + self.asset_id + '/logs.txt', 'a')
        f.write('Broadcast\n' + str(res) + '\n')
        f.close()

    def on_btn_register_clicked_send(self):
        Issue(self.config_file)
        res = os.popen(self.command).read()
        self.ui.txt_check.setText(str(res))
        self.ui.repaint()

    def on_btn_proof_clicked_send(self):
        i = Issue(self.config_file)
        if (i.check_website(self.domain, self.asset_id)):
            website = 'valid website'
        else:
            website = 'invalid website'
        self.ui.txt_check.setText(website)
        self.ui.repaint()

    def on_btn_check_clicked_send(self):
        i = Issue(self.config_file)
        registryURL = 'https://assets.blockstream.info/'
        buf = 'NOT FOUND IN THE ASSET REGISTRY!!!'
        resp = requests.get(url=registryURL, verify=True)
        assets = resp.json()
        for asset in assets.keys():
            if asset == self.asset_id:
                contract = json.dumps(
                    assets[asset]['contract'], separators=(',', ':'), sort_keys=True)
                sha256_c = hashlib.sha256()
                sha256_c.update(contract.encode('ascii'))
                contract_hash = sha256_c.hexdigest()

                prev_tx = assets[asset]['issuance_prevout']['txid']
                prev_vout = assets[asset]['issuance_prevout']['vout']
                issuance_txid = assets[asset]['issuance_txin']['txid']
                issuance_vin = assets[asset]['issuance_txin']['vin']
                domain = assets[asset]['contract']['entity']['domain']

                if (i.check_contract(prev_tx, prev_vout, contract_hash, asset)):
                    contract = 'valid contract'
                else:
                    contract = 'invalid contract'

                if (i.check_tx(issuance_txid, issuance_vin, asset, False)):
                    tx = 'valid transaction'
                else:
                    tx = 'invalid transaction'

                if (i.check_website(domain, asset)):
                    website = 'valid website'
                else:
                    website = 'invalid website'

                buf = '{} has {}, {} and {}.\n'.format(
                    asset, contract, tx, website)

        self.ui.txt_check.setText(buf)
        self.ui.repaint()

    def on_btn_config_load_clicked(self):
        config = configparser.RawConfigParser()
        config.read(self.config_file)
        self.ui.txt_LIQUID_host.setText(config.get('LIQUID', 'host'))
        self.ui.txt_LIQUID_port.setText(config.get('LIQUID', 'port'))
        self.ui.txt_LIQUID_username.setText(config.get('LIQUID', 'username'))
        self.ui.txt_LIQUID_password.setText(config.get('LIQUID', 'password'))
        self.ui.txt_LIQUID_wallet.setText(config.get('LIQUID', 'wallet'))
        self.ui.txt_LIQUID_passphrase.setText(
            config.get('LIQUID', 'passphrase'))
        self.ui.repaint()

    def on_btn_config_save_clicked(self):
        file = open(self.config_file, 'w+')
        file.write('[LIQUID]'+'\n')
        file.write('host: '+self.ui.txt_LIQUID_host.text()+'\n')
        file.write('port: '+self.ui.txt_LIQUID_port.text()+'\n')
        file.write('username: '+self.ui.txt_LIQUID_username.text()+'\n')
        file.write('password: '+self.ui.txt_LIQUID_password.text()+'\n')
        file.write('wallet: '+self.ui.txt_LIQUID_wallet.text()+'\n')
        file.write('passphrase: ' +
                   self.ui.txt_LIQUID_passphrase.text()+'\n'+'\n')
        file.close()
        self.ui.repaint()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.ui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.ui.show()
    sys.exit(app.exec_())
