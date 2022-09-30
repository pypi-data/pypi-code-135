# -*- coding: utf-8 -*-
# 2019 to present - Copyright Microchip Technology Inc. and its subsidiaries.

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

from tpds.xml_handler.tflxtls_xml_updates import TFLXTLSXMLUpdates
from tpds.xml_handler.tflxwpc_xml_updates import TFLXWPCXMLUpdates


class XMLProcessing():
    def __new__(self, base_xml='ECC608B_TFLXTLS.xml'):
        if base_xml is None:
            base_xml='ECC608B_TFLXTLS.xml'

        if base_xml in ['ECC608B_TFLXTLS.xml', 'PIC32CMLS60_ECC608.xml']:
            self = TFLXTLSXMLUpdates(base_xml)
        elif base_xml in ['ECC608A-MAH-TFLXWPC.xml']:
            self = TFLXWPCXMLUpdates(base_xml)
        return self


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    pass
