# -*- coding: utf-8 -*-
# 2018 to present - Copyright Microchip Technology Inc. and its subsidiaries.

# Subject to your compliance with these terms, you may use Microchip software
# and any derivatives exclusively with Microchip products. It is your
# responsibility to comply with third party license terms applicable to your
# use of third party software (including open source software) that may
# accompany Microchip software.

# THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
# EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
# WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR
# PURPOSE. IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL,
# PUNITIVE, INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY
# KIND WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP
# HAS BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
# FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
# ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
# THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.

import os
from helper import (
            connect_to_prototyping_board, get_user_option,
            get_user_manifest, generate_manifest,
            verify_cert_chain, verify_SE_with_random_challenge,
            generate_project_config_h, get_tng_device_cert)
import yaml
import tpds.tp_utils.tp_input_dialog as tp_userinput
from tpds.tp_utils.tp_print import print
from tpds.cloud_connect.azure_connect import AzureConnect
from tpds.certs.cert_utils import get_certificate_CN
from pathlib import Path


class AzureConnectUsecase():
    def __init__(self, boards):
        self.boards = boards
        self.connection = AzureConnect()
        self.element = None

    def generate_or_upload_manifest(self, b=None):
        user_option = get_user_option(b)
        if user_option == 'Upload Manifest':
            self.manifest = get_user_manifest(b)
            assert self.manifest.get('json_file') is not None, \
                'Select valid Manifest file'
            assert self.manifest.get('ca_cert') is not None, \
                'Select valid Manifest CA file'
        else:
            self.__perform_device_connect(b)
            self.manifest = generate_manifest(b)

    def register_device(self, b=None):
        resp_data = self.__azure_login(b)
        assert resp_data == 'Success', f'''Azure login config failed with "{resp_data}"'''

        print('Registering device into azure account...', canvas=b)
        self.connection.register_device_from_manifest(
                        device_manifest=self.manifest.get('json_file'),
                        device_manifest_ca=self.manifest.get('ca_cert'))
        print('Completed...', canvas=b)

    def verify_cert_chain(self, b=None):
        if self.element is None:
            self.__perform_device_connect(b)
        self.device_cert = verify_cert_chain(b)
        if self.device_cert is None:
            raise ValueError('Certificate chain validation is failed')

    def verify_SE_with_random_challenge(self, b=None):
        verify_SE_with_random_challenge(self.device_cert, b)

    def is_cn_supports_azure(self, device_cert, b=None):
        return (' ' not in get_certificate_CN(device_cert))

    def __azure_login(self, b=None):
        with open(self.connection.creds_file) as f:
            azure_credentials = yaml.safe_load(f)
        if all(dict((k, v.strip()) for k, v in azure_credentials.items()).values()):
            self.connection.set_credentials(azure_credentials)
            print(f'Azure IoT Hub: {self.connection.az_hub_name}', canvas=b)
            print(
                f'Azure Subscription: {self.connection.az_subscription_id}',
                canvas=b)
            azure_connect = os.path.join(os.getcwd(), 'azure_connect.h')
            with open(azure_connect, 'w') as f:
                f.write('#ifndef _AZURE_CONNECT_H\n')
                f.write('#define _AZURE_CONNECT_H\n\n')
                f.write('#include "cryptoauthlib.h"\n\n')
                f.write('#ifdef __cplusplus\n')
                f.write('extern "C" {\n')
                f.write('#endif\n\n')
                cloud_endpoint = (
                    f'#define CLOUD_ENDPOINT "{self.connection.az_hub_name}'
                    '.azure-devices.net"\n\n')
                f.write(cloud_endpoint)
                f.write('#ifdef __cplusplus\n')
                f.write('}\n')
                f.write('#endif\n')
                f.write('#endif\n')

            files = [file for file in os.listdir('.') if (os.path.isfile(file) and file.startswith('cust_def'))]
            if not files:
                # create dummy definition files for compilation
                Path('cust_def_1_signer.c').write_text('//Empty file for compilation')
                Path('cust_def_1_signer.h').write_text('//Empty file for compilation')
                Path('cust_def_2_device.c').write_text('//Empty file for compilation')
                Path('cust_def_2_device.h').write_text('//Empty file for compilation')
            return 'Success'
        else:
            msg_box_info = (
                '<font color=#0000ff><b>Invalid Azure account credentials'
                '</b></font><br>'
                '<br>To setup an Azure account, please refer Usecase help guide<br>')
            acc_cred_diag = tp_userinput.TPMessageBox(
                title="Azure account credentials",
                info=msg_box_info)
            acc_cred_diag.invoke_dialog()
            return 'Credentials are unavailable'

    def __perform_device_connect(self, b=None):
        self.element = connect_to_prototyping_board(self.boards, b)
        assert self.element, 'Connection to Board failed'
        device_cert = get_tng_device_cert()
        azure_support = self.is_cn_supports_azure(device_cert, b)
        generate_project_config_h(cert_type='MCHP', address=0x6A, azure_support=azure_support)
        assert azure_support, ((
                'Connected TNG device doesn\'t support Azure.\n'
                'Cert CN contains space(s).'))


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    pass
