import inspect
import os
from importlib import import_module

class ImproperlyConfigured(Exception): pass

try:
    from .app_utils import import_string, module_has_submodule
except ImportError:
    from app_utils import import_string, module_has_submodule
    
APPS_MODULE_NAME = "service_nodes"


"""
plan for configuring the registry

Apps -> repositories
ServiceNode -> Class, can be overridden
ResourceNode -> Class, can be overridden, child to ServiceNode
--------------------------------

The OverrideClasses that are in this repository,
    - added by default to the registry

CustomClasses which will be pip installed
    - dynamic import
    - ServiceNode creation
--------------------------------
what i'll need:
    - AbstractResourceNode
    - AbstractServiceNode
    - ResourceNode, ResourceNodeFactory
    - ServiceNode, ServiceNodeFactory
--------------------------------
plan:
    - do the balcony service nodes first
    - then do the custom nodes, packaging, template repository
    -     
    
--------------------------------
notes:
    - keep the app_ready feature, it might help
    - 


"""



