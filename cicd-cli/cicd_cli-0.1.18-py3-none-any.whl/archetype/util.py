from pydoc import locate

from cicd.archetype import dropwizard, pip, node, store_backend, docker

archetypes = {
    'dropwizard': dropwizard.Dropwizard,
    'pip': pip.Pip,
    'node': node.Node,
    'store-backend': store_backend.StoreBackend,
    'docker': docker.Docker,
}


def get_archetypes():
    return archetypes.keys()


def get_archetype(archetype, application_name, config):
    archetype_clazz = archetypes[archetype]
    return archetype_clazz(application_name, config)


def get_attr(archetype, method):
    archetype_clazz = locate(archetypes[archetype])
    return getattr(archetype_clazz, method)
