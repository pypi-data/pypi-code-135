# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wacz_signing']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=38.0.1,<39.0.0',
 'pem>=21.2.0,<22.0.0',
 'pyasn1>=0.4.8,<0.5.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'rfc3161ng>=2.1.3,<3.0.0']

setup_kwargs = {
    'name': 'wacz-signing',
    'version': '0.2.0',
    'description': 'A library for signing and timestamping file hashes',
    'long_description': 'wacz-signing\n============\n\nThis package builds on work by Ilya Kreymer and Webrecorder in\n[authsign](https://github.com/webrecorder/authsign). It is intended\nfor use in WACZ signing (and to a lesser extent, verification), as set\nforth in the Webrecorder Recommendation [WACZ Signing and\nVerification](https://specs.webrecorder.net/wacz-auth/0.1.0/). It is\nan attempt to reduce authsign\'s footprint, and decouple signing from\nany specific web API, authentication, and the process of obtaining key\nmaterial. It also omits the optional cross-signing mechanism specified\nin the recommendation and provided by authsign.\n\nInstallation\n------------\n\nFor regular use, start a virtual environment and install this package\nand its requirements, something like this:\n\n```\npython3 -m venv env\n. env/bin/activate\npip install wacz-signing\n```\n\nUse\n---\n\nThe simplest way to use this system is to provide the environment\nvariables `DOMAIN` and `CERTNAME`, possibly in a `.env` file; the\npackage will then use the key material in\n`/etc/letsencrypt/live/<CERTNAME>/`. (The provision of `DOMAIN` is to\naccommodate the possibility that the domain name we care about is not\nthe one that was originally used to create the cert.) Then, you can\n\n```\n>>> from wacz_signing import signer\n>>> result = signer.sign(\'hello world!\', datetime.utcnow())\n>>> signer.verify(result)\n{\'observer\': [\'mkcert\'], \'software\': \'wacz-signing 0.2.0\', \'timestamp\': \'2022-10-05T19:03:25Z\'}\n```\n\nor\n\n```\n>>> signer.verify_wacz(\'valid_signed_example_1.wacz\')\n{\'observer\': [\'btrix-sign-test.webrecorder.net\'], \'software\': \'authsigner 0.3.0\', \'timestamp\': \'2022-01-18T19:00:12Z\'}\n```\n\n\nYou can also provide cert, key, and timestamper material directly, or\nin alternate files, using environment variables: you MUST provide\n`DOMAIN`; you MUST provide either `CERTNAME` or one of `CERT` and\n`CERTFILE`; if you have set `CERTNAME`, you MUST provide one of `KEY`\nand `KEYFILE`. If you\'re not using Letsencrypt certs, you\'ll need to\nset `CERT_ROOTS`. You may also configure the timestamper with `TS_CERT`\nor `TS_CERTFILE` and `TS_URL` and `TS_ROOTS`. You may additionally\nchange the `CERT_DURATION` from its default of 7 days, and the\n`STAMP_DURATION` from its default of 10 minutes.\n\nYou may want to catch `signer.SigningException`,\n`signer.VerificationException`, and `signer.VerificationFailure`.\n\nFor local development and testing, you\'ll need to install\n[mkcert](https://github.com/FiloSottile/mkcert). To generate certs,\nyou might run\n\n```\nmkcert -cert-file cert.pem -key-file key.pem example.org\ncp cert.pem fullchain.pem\ncat "$(mkcert -CAROOT)/rootCA.pem" >> fullchain.pem\n```\n\nand then set up `.env` like this:\n\n```\nDOMAIN=example.org\nCERTFILE=fullchain.pem\nKEYFILE=key.pem\nCERT_ROOTS=<root CA fingerprint>\n```\n\nwhere you get the value for `CERT_ROOTS` by running\n\n```\nopenssl x509 -noout -in "`mkcert -CAROOT`"/rootCA.pem -fingerprint -sha256 | cut -f 2 -d \'=\' | sed \'s/://g\' | awk \'{print tolower($0)}\'\n```\n\nCertificate management\n----------------------\n\nIf you\'re using Letsencrypt certs, and you want them to be valid for a\nshort duration, say the default of seven days, you would need to force\na renewal after a week, then manually revoke the previous week\'s cert,\nsomething like\n\n```\ncertbot renew --force-renewal --deploy-hook /path/to/deploy-hook-script\n```\n\n(or just put the script in `/etc/letsencrypt/renewal-hooks/deploy/`\n\nwhere the script runs something like\n\n```\ncertbot revoke --cert-path `ls -t /etc/letsencrypt/archive/${CERTNAME}/cert*.pem | head -n 2 | tail -n 1` --reason expiration\n```\n\n(But triple-check this before attempting it in earnest; a correct\nexample may follow.)\n\nUse cases\n---------\n\nThis package could be used in a tiny API, of course; it could also be\nintegrated into a producer of WACZ files, like a future version of\nPerma, which would sign archives internally; it could also be run in a\nlambda, which is why it\'s possible to provide key material directly in\nenvironment variables.\n\nStay tuned for examples of these uses in a later commit.\n',
    'author': 'Ben Steinberg',
    'author_email': 'bsteinberg@law.harvard.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
