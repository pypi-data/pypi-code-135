# internal
from tier.internal.logging import log
from tier.internal.dependency_graph import DependencyGraph
from tier.internal.tier import Tier


def deps():
    log.debug('tier deps')
    tier = Tier()
    projects = list(reversed(tier.projects()))
    print('.')
    for i, project in enumerate(projects):
        package_name = project.build_system().get_package_name()
        if i < len(projects) - 1:
            print(f'├── {package_name}')
        else:
            print(f'└── {package_name}')
        dependencies = tier.graph.get_internal_dependencies(package_name)
        for j, dependency_name in enumerate(dependencies):
            if j < len(dependencies) - 1:
                print(f'│   ├── {dependency_name}')
            else:
                print(f'│   └── {dependency_name}')
