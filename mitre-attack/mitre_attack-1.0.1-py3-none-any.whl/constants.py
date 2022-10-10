import os
import tempfile

GIT_REPO_URL = os.getenv('MITRE_CTI_GIT_REPO_URL', 'https://github.com/mitre/cti.git')
GIT_REPO_PATH = os.getenv('MITRE_CTI_GIT_REPO_PATH', os.path.join(tempfile.gettempdir(), 'mitre/cti'))

ENTERPRISE = 'enterprise'
MOBILE = 'mobile'
ICS = 'ics'

DOMAINS = [ENTERPRISE, MOBILE, ICS]

LOCAL_FILE_PATHS_BY_DOMAIN = dict([
    (domain, os.path.join(GIT_REPO_PATH, '{}-attack/{}-attack.json'.format(domain, domain))) for domain in DOMAINS
])

DEFAULT_MITRE_VERSION = "1.0"

#: STIX 2.x data types.
ATTACK_PATTERN = 'attack-pattern'
COURSE_OF_ACTION = 'course-of-action'
DATA_COMPONENT = 'x-mitre-data-component'
DATA_SOURCE = 'x-mitre-data-source'
IDENTITY = 'identity'
INTRUSION_SET = 'intrusion-set'
MALWARE = 'malware'
MARKING_DEFINITION = 'marking-definition'
MATRIX = 'x-mitre-matrix'
RELATIONSHIP = 'relationship'
TACTIC = 'x-mitre-tactic'
TOOL = 'tool'
