import os
import shutil
import sys
from cement.utils.version import get_version_banner
from ..core.version import get_version
from cement import Controller, ex
from ..utils.utils import CommandError

VERSION_BANNER = """
Build and Deploy with Kluff %s
%s
""" % (get_version(), get_version_banner())


class AppSetup(Controller):
    class Meta:
        label = 'items'
        stacked_type = 'embedded'
        stacked_on = 'base'

    def _default(self):
        """Default action if no sub-command is passed."""

        self.app.args.print_help()

    @ex(
        help='create plugin',
        arguments=[
            (['plugin_name'], 
                            {'help': 'plugin name'}
            ),

            ( ['--language'],
                            {'help': 'Backend language i.e Python, Go, Javascript'}
            ),
        ],
    )
    def create(self):
        plugin_name = self.app.pargs.plugin_name
        language = self.app.pargs.language or 'python'
        self.app.log.info(f'creating plugin {plugin_name} using language {language}')
        try:
            templates = self.app.config.get('kluff', 'templates')
            print(templates)
            sys.exit()
            backend_template = os.path.join(templates, language)
            frontend_template = os.path.join(templates, 'react')
            apps_path = self.app.config.get('kluff', 'apps')
            target_backend_app = os.path.join(apps_path, plugin_name, 'backend')
            target_frontend_app = os.path.join(apps_path, plugin_name, 'frontend')
            shutil.copytree(backend_template, target_backend_app, dirs_exist_ok=True)
            shutil.copytree(frontend_template, target_frontend_app, dirs_exist_ok=True)
        except OSError as e:
            raise CommandError(e)


    @ex(
        help='run plugin',
        arguments=[
        (['plugin_name'], 
                        {'help': 'plugin name'}
        ),
        ],
        )
    def run(self):
        plugin_name = self.app.pargs.plugin_name
        self.app.log.info(f'running plugin {plugin_name}')
        try:
            self.app.log.info('running backend...')
            apps_dir = self.app.config.get('kluff', 'apps')
            backend = os.path.join(apps_dir, plugin_name, 'backend')
            frontend = os.path.join(apps_dir, plugin_name, 'frontend')
            backend_docker_file = os.path.join(backend, 'Dockerfile')
            
            os.system(f'cd {backend} && docker build -t {plugin_name} . -f {backend_docker_file}')
            os.system(f'docker stop {plugin_name}')
            os.system(f'docker run -it -p 5000:5000 -d {plugin_name}')

            os.system(f'cd {frontend}')
            os.system('yarn install && yarn stop && yarn start')

        except OSError as e:
            raise CommandError(e)
    
    @ex(
        help='deploy plugin',
        arguments=[
        (['plugin_name'], 
                        {'help': 'plugin name'}
        ),
        ],
        )
    def deploy(self):
        plugin_name = self.app.pargs.plugin_name
        self.app.log.info(f'deploying plugin: {plugin_name}')
        try:
            os.system(f'cd {plugin_name}')
            os.system('git push')
        except OSError as e:
            raise CommandError(e)
