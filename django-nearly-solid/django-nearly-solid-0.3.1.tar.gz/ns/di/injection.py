import inject


def depends(interface: type) -> object:
    return inject.attr(interface)


def get_depend(interface: type) -> object:
    return inject.instance(interface)
