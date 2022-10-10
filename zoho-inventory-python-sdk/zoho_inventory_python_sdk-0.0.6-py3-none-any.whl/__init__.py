from ._version import get_versions
from .client import Client
from .base_client import BaseClient
from .oauth_manager import OAuthManager
from .oauth import OAuth
from .utils import load_configuration, load_zoho_configuration, load_oauth_configuration, read_json_file, \
    demand_configuration
from .resources.currencies import Currencies
from .resources.taxexemptions import TaxExemptions
from .resources.taxauthorities import TaxAuthorities
from .resources.bills import Bills
from .resources.bundles import Bundles
from .resources.compositeitems import CompositeItems
from .resources.contactpersons import ContactPersons
from .resources.contacts import Contacts
from .resources.itemgroups import ItemGroups
from .resources.items import Items

from .resources.salesorders import SalesOrders
from .resources.shipmentorders import ShipmentOrders

from .aws import *

__version__ = get_versions()['version']
del get_versions
