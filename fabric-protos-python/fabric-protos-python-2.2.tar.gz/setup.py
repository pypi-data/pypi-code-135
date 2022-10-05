# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fabric_protos_python',
 'fabric_protos_python.common',
 'fabric_protos_python.discovery',
 'fabric_protos_python.gossip',
 'fabric_protos_python.ledger',
 'fabric_protos_python.ledger.queryresult',
 'fabric_protos_python.ledger.rwset',
 'fabric_protos_python.ledger.rwset.kvrwset',
 'fabric_protos_python.msp',
 'fabric_protos_python.orderer',
 'fabric_protos_python.orderer.etcdraft',
 'fabric_protos_python.peer',
 'fabric_protos_python.peer.lifecycle',
 'fabric_protos_python.transientstore']

package_data = \
{'': ['*']}

install_requires = \
['grpclib>=0.4.3,<0.5.0', 'protobuf>=4.21.7,<5.0.0']

setup_kwargs = {
    'name': 'fabric-protos-python',
    'version': '2.2',
    'description': 'Hyperledger Fabric gRPC and Protocol Buffer Bindings for python',
    'long_description': '# fabric-protos-python\nHyperledger Fabric gRPC and Protocol Buffer Bindings for python\n\n## Community\n\nWe welcome contributions to the Hyperledger Fabric project in many forms.\nThere’s always plenty to do! Check the documentation on\n[how to contribute][contributing] to this project for the full details.\n\n- [Hyperledger Community](https://www.hyperledger.org/community)\n- [Hyperledger mailing lists and archives](http://lists.hyperledger.org/)\n- [Hyperledger Chat](http://chat.hyperledger.org/channel/fabric)\n- [Hyperledger Fabric Issue Tracking (JIRA)](https://jira.hyperledger.org/secure/Dashboard.jspa?selectPageId=10104)\n- [Hyperledger Fabric Wiki](https://wiki.hyperledger.org/display/Fabric)\n- [Hyperledger Wiki](https://wiki.hyperledger.org/)\n- [Hyperledger Code of Conduct](https://wiki.hyperledger.org/display/HYP/Hyperledger+Code+of+Conduct)\n\n## License <a name="license"></a>\n\nHyperledger Project source code files are made available under the Apache License, Version 2.0 (Apache-2.0), located in the [LICENSE](LICENSE) file. Hyperledger Project documentation files are made available under the Creative Commons Attribution 4.0 International License (CC-BY-4.0), available at http://creativecommons.org/licenses/by/4.0/.\n\n[contributing]: https://hyperledger-fabric.readthedocs.io/en/latest/CONTRIBUTING.html\n[go]: https://golang.org/\n[grpc]: https://grpc.io/docs/guides/\n[protobuf]: https://github.com/protocolbuffers/protobuf/\n[rocketchat-image]: https://open.rocket.chat/images/join-chat.svg\n[rocketchat-url]: https://chat.hyperledger.org/channel/fabric\n',
    'author': 'Institute of Cryptography of the Faculty of Mathematics and Computer Science at University of Havana',
    'author_email': 'kmilo.denis.glez@yandex.com',
    'maintainer': 'Kmilo Denis González',
    'maintainer_email': 'kmilo.denis.glez@yandex.com',
    'url': 'https://github.com/ic-matcom/fabric-protos-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
