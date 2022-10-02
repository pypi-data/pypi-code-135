from typing import Dict, Tuple

from colorama import Fore
from johnsnowlabs.py_models.jsl_secrets import LicenseInfos

from johnsnowlabs.py_models.install_info import InstallFolder

from johnsnowlabs.auto_install.softwares import Software

from johnsnowlabs.abstract_base.software_product import AbstractSoftwareProduct

from johnsnowlabs.utils.enums import ProductName
import sys

def check_health(check_install=True, check_health=False, check_licenses=False, check_jars=False):
    # Print status of installations and licenses
    install_status: Dict[AbstractSoftwareProduct:bool] = {}
    health_check: Dict[AbstractSoftwareProduct:bool] = {}
    license_check: Dict[str, Tuple[bool, bool]] = {}
    for product in ProductName:
        if check_install:
            product = Software.for_name(product)
            if not product or not product.pypi_name:
                continue
            install_status[product] = product.check_installed() and product.check_installed_correct_version()
            if not product.check_installed():
                print(f'{product.logo + product.name} is not installed 🚨')
            elif not product.check_installed_correct_version():
                print(
                    f'{product.logo + product.pypi_name + Fore.LIGHTRED_EX}=={product.get_installed_version() + Fore.RESET} '
                    f'is installed but should be {product.pypi_name}=={Fore.LIGHTGREEN_EX + product.latest_version.as_str() + Fore.RESET} 🚨 To fix run:')
                print(
                    f'{Fore.LIGHTGREEN_EX}{sys.executable} -m pip install {product.pypi_name}=={product.latest_version.as_str()} --upgrade{Fore.LIGHTGREEN_EX}')
            else:
                print(f'{product.logo + Fore.LIGHTGREEN_EX + product.pypi_name}=={product.get_installed_version()} '
                      f'is correctly installed! ✅{Fore.RESET}')

        if health_check:
            health_check[product] = product.health_check()

    if check_jars:
        java_folder = InstallFolder.java_folder_from_home()

    if check_licenses:
        # TODO
        jsl_secrets.ocr_validation_logged = True
        jsl_secrets.hc_validation_logged = True
        licenses = LicenseInfos.from_home()
        for file, info in licenses.infos.items():
            # We use '?' to imply user has no access and not print this
            hc_ok, ocr_ok = '?', '?'
            if info.jsl_secrets.HC_SECRET:
                hc_ok = JslSecrets.is_hc_secret_correct_version(info.jsl_secrets.HC_SECRET)
            if info.jsl_secrets.OCR_SECRET:
                ocr_ok = JslSecrets.is_ocr_secret_correct_version(info.jsl_secrets.OCR_SECRET)
            # if hc_ok
            #     print(f'')

            license_check[file] = hc_ok, ocr_ok
