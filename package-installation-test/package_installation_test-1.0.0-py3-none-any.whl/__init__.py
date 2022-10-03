__version__ = '1.0.0'


from pathlib import Path


def home():
    return Path(__file__).parent


def main():
    print(f'Version {__version__} of {__package__} successfully installed.')
    print(f'The source code is in {home()}.')
