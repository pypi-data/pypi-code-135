from setuptools import setup, find_packages


# VERSION = '0.1'
# DESCRIPTION = "Wrapper for Zoho API operations; migration, automations, 
# etc."


# setup(

VERSION = '0.1'
DESCRIPTION = "Wrapper for Zoho API operations; migration, automations,  etc."
LONG_DESCRIPTION = "Initially began as a pet project, the ZohoSolutionsSuite \
	seeks to bring the ease of use that Deluge offers to endpoints, to other apps as well!"


setup(
	name="ZohoSolutionsSuite",
	version=VERSION,
	author="Dylan Garrett",
	author_email="dylan.g@zohocorp.com",
	description=DESCRIPTION,
	long_description=LONG_DESCRIPTION,
	packages=find_packages(),
	keywords=['zoho', 'crm', 'api', 'tools', 'migration']
)