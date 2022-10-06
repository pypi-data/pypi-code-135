from setuptools import setup, find_packages

setup(
    name="silvair-uart-decoder",
    version="0.1.0",
    packages=find_packages(),
    license='MIT',
    entry_points={
        "console_scripts": [
            "uart-decoder=silvair_uart_decoder.main:main",
            "generate_uart_decoder_extension=silvair_uart_decoder.main:generate_saleae_extension"
        ]
    },
    url='https://github.com/SilvairGit/silvair-uart-decoder',
    include_package_data=True,
    author="Silvair",
    author_email="support@silvair.com",
    description="Tool for decoding Silvair UART protocol.",
    install_requires=["construct", "crcmod"],
    tests_require=["pytest"],
)
