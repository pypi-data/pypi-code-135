from PySide2 import QtWidgets
from PySide2.QtUiTools import QUiLoader
import sys
import os
import os.path
from woc.write import Write
import configparser


class AppWindow():
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        bundle_dir = getattr(
            sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        path_to_dialog_ui = os.path.abspath(
            os.path.join(bundle_dir, 'dialog.ui'))
        self.ui = loader.load(path_to_dialog_ui, None)

        self.directory = os.path.expanduser('~')+'/.woc/'
        self.config_file = self.directory+'main.conf'
        self.ui.combo_chain.selected = 0
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        if not os.path.isfile(self.config_file):
            self.on_btn_config_save_clicked()
        else:
            self.on_btn_config_load_clicked()
        self.ui.btn_write.clicked.connect(self.on_btn_write_clicked_send)
        self.ui.btn_config_load.clicked.connect(
            self.on_btn_config_load_clicked)
        self.ui.btn_config_save.clicked.connect(
            self.on_btn_config_save_clicked)

    def on_btn_write_clicked_send(self):
        print(self)
        try:
            mytext = self.ui.txt_message.text()
            chain = self.ui.combo_chain.currentText()
            text = "Writing on " + chain + " the following string:\n"
            text = text + mytext + "\n"
            write = Write(self.config_file, chain)
            tx = write.sendTx(mytext)
            text = text + "Result on transaction: " + str(tx) + "\n"
            self.ui.txt_result.setText(text)

            self.ui.repaint()

        except Exception as e:
            self.ui.txt_result.setText("ERROR: ", e)

            self.ui.repaint()

    def on_btn_config_load_clicked(self):
        config = configparser.RawConfigParser()
        config.read(self.config_file)
        self.ui.txt_BTC_host.setText(config.get('BTC', 'host'))
        self.ui.txt_BTC_port.setText(config.get('BTC', 'port'))
        self.ui.txt_BTC_username.setText(config.get('BTC', 'username'))
        self.ui.txt_BTC_password.setText(config.get('BTC', 'password'))
        self.ui.txt_BTC_wallet.setText(config.get('BTC', 'wallet'))
        self.ui.txt_BTC_passphrase.setText(config.get('BTC', 'passphrase'))
        self.ui.txt_tBTC_host.setText(config.get('tBTC', 'host'))
        self.ui.txt_tBTC_port.setText(config.get('tBTC', 'port'))
        self.ui.txt_tBTC_username.setText(config.get('tBTC', 'username'))
        self.ui.txt_tBTC_password.setText(config.get('tBTC', 'password'))
        self.ui.txt_tBTC_wallet.setText(config.get('tBTC', 'wallet'))
        self.ui.txt_tBTC_passphrase.setText(config.get('tBTC', 'passphrase'))
        self.ui.txt_LTC_host.setText(config.get('LTC', 'host'))
        self.ui.txt_LTC_port.setText(config.get('LTC', 'port'))
        self.ui.txt_LTC_username.setText(config.get('LTC', 'username'))
        self.ui.txt_LTC_password.setText(config.get('LTC', 'password'))
        self.ui.txt_LTC_wallet.setText(config.get('LTC', 'wallet'))
        self.ui.txt_LTC_passphrase.setText(config.get('LTC', 'passphrase'))
        self.ui.txt_tLTC_host.setText(config.get('tLTC', 'host'))
        self.ui.txt_tLTC_port.setText(config.get('tLTC', 'port'))
        self.ui.txt_tLTC_username.setText(config.get('tLTC', 'username'))
        self.ui.txt_tLTC_password.setText(config.get('tLTC', 'password'))
        self.ui.txt_tLTC_wallet.setText(config.get('tLTC', 'wallet'))
        self.ui.txt_tLTC_passphrase.setText(config.get('tLTC', 'passphrase'))
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
        file.write('[BTC]'+'\n')
        file.write('host: '+self.ui.txt_BTC_host.text()+'\n')
        file.write('port: '+self.ui.txt_BTC_port.text()+'\n')
        file.write('username: '+self.ui.txt_BTC_username.text()+'\n')
        file.write('password: '+self.ui.txt_BTC_password.text()+'\n')
        file.write('wallet: '+self.ui.txt_BTC_wallet.text()+'\n'+'\n')
        file.write('passphrase: '+self.ui.txt_BTC_passphrase.text()+'\n'+'\n')
        file.write('[tBTC]'+'\n')
        file.write('host: '+self.ui.txt_tBTC_host.text()+'\n')
        file.write('port: '+self.ui.txt_tBTC_port.text()+'\n')
        file.write('username: '+self.ui.txt_tBTC_username.text()+'\n')
        file.write('password: '+self.ui.txt_tBTC_password.text()+'\n')
        file.write('wallet: '+self.ui.txt_tBTC_wallet.text()+'\n'+'\n')
        file.write('passphrase: '+self.ui.txt_tBTC_passphrase.text()+'\n'+'\n')
        file.write('[LTC]'+'\n')
        file.write('host: '+self.ui.txt_LTC_host.text()+'\n')
        file.write('port: '+self.ui.txt_LTC_port.text()+'\n')
        file.write('username: '+self.ui.txt_LTC_username.text()+'\n')
        file.write('password: '+self.ui.txt_LTC_password.text()+'\n')
        file.write('wallet: '+self.ui.txt_LTC_wallet.text()+'\n'+'\n')
        file.write('passphrase: '+self.ui.txt_LTC_passphrase.text()+'\n'+'\n')
        file.write('[tLTC]'+'\n')
        file.write('host: '+self.ui.txt_tLTC_host.text()+'\n')
        file.write('port: '+self.ui.txt_tLTC_port.text()+'\n')
        file.write('username: '+self.ui.txt_tLTC_username.text()+'\n')
        file.write('password: '+self.ui.txt_tLTC_password.text()+'\n')
        file.write('wallet: '+self.ui.txt_tLTC_wallet.text()+'\n'+'\n')
        file.write('passphrase: '+self.ui.txt_tLTC_passphrase.text()+'\n'+'\n')
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
    main()
