# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['manim_meshes',
 'manim_meshes.delaunay',
 'manim_meshes.models',
 'manim_meshes.models.data_models',
 'manim_meshes.models.manim_models']

package_data = \
{'': ['*'], 'manim_meshes': ['data/models/*', 'shaders/mesh/*']}

install_requires = \
['ManimPango>=0.4.1,<0.5.0',
 'decorator>=5.0.9,<6.0.0',
 'manim>=0.16.0,<0.17.0',
 'manimgl>=1.6.1,<2.0.0',
 'moderngl',
 'numpy',
 'trimesh>=3.12.5,<4.0.0']

entry_points = \
{'manim.plugins': ['manim_meshes = module:object.attr']}

setup_kwargs = {
    'name': 'manim-meshes',
    'version': '0.0.8a0',
    'description': 'rendering 2D and 3D Meshes with manim for displaying and educational Purposes.',
    'long_description': '[![Python Test and Lint](https://github.com/bmmtstb/manim-meshes/actions/workflows/python_ci_test.yaml/badge.svg)](https://github.com/bmmtstb/manim-meshes/actions/workflows/python_ci_test.yaml) [![CodeQL](https://github.com/bmmtstb/manim-meshes/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/bmmtstb/manim-meshes/actions/workflows/codeql-analysis.yml)\n# Manim for Meshes\n\n> ⚠️ not fully optimal - but fine for smaller meshes\n> \n> Manim and the OpenGL renderer are not really friends right now, therefore most of the code runs terribly slow for larger meshes. In Addition to the small educational meshes we present a faster mesh that uses a custom shader but this requires manipulating the manim library.\n>\n> Stay tuned or feel free to assist. Either here or directly in the manim OpenGL part. Not necessarily everything is a Bézier curve... \n\nManim-Trimeshes implements manim functionalities for different types of meshes using either basic node-face data structures or by importing meshes from the python [trimesh](https://pypi.org/project/trimesh/ "trimesh on pypi") library.\n\nIt is mainly developed as a Project for Interactive Graphics Systems Group (GRIS) at TU Darmstadt University, but is made publicly available for everyone interested in rendering and animating meshes.\n\n## Installation\n\nManim-meshes has been published to [pypi](https://pypi.org/project/manim-meshes/) and therefore can be easily installed using:\n\n``pip install manim-meshes``\n\n## Usage\n\n``from manim_meshes import *``\n\nWhile executing a commandline manim script, make sure to set the `--renderer=opengl` flag, the Cairo renderer will ins most cases not work.\n\nThe basic `ManimMesh` and `Manim2DMesh` from `manim_models/basic_mesh` can currently only be used for smaller meshes (<1k Nodes), because it is dependent on the manim internal shaders which are not really implemented optimally. This type of mesh can be easily used for 2D and smaller 3D explanatory videos, not for high resolution rendering. Both these classes should give manim-functionalities like shift, rotate and scale. But due to the sheer amount of MObject functions we can not implement all of them, so make sure the renderer has overwritten the method you are trying to use if something does not look right.\n\nThe `TriangleManim2DMesh` from `triangle_mesh` implements further functions that are only reasonable for two-dimensional triangle meshes. (e.g. Delaunay) This was designed for educational purposes. There is also a package\n`delaunay` containing multiple useful functions regarding delaunay triangulations, e.g. Voronoi diagrams, checking the delaunay criterion or a divide & conquer algorithm.\n\nThe more advanced `FastManimMesh` from `opengl_mesh` uses a custom shader which needs to be inserted into the base manim implementation at this time! But therefore it can render enormous meshes fast. Sadly rendering is kind of everything this renderer is capable of at the moment.\n\nAll these Mesh-Renders reference a mesh based on the `Mesh`-Class, in `data_models`, which should implement a multitude of basic Mesh-functions.\n\n## Example\n\n![Static image of a cone, to show the rendering capabilities](docs/images/ConeScene_v0.16.0.post0.png)\n\nWith active poetry venv Run one of the minimal test examples: `manim --renderer=opengl tests/test_scene.py ConeScene`.\n\nMultiple other examples can be found in the `tests/test_scene.py` file.\n\n[![see the PyramidScene for basic manim mesh uses](docs/images/PyramidScene.png)](https://user-images.githubusercontent.com/1500595/193240449-5978f46f-68b0-4d08-bf37-4ff1fea54f28.mp4)\n\nThe general procedure is like in manim, create a class with a construct method. Then create and add the instance of the renderable mesh you like to use. This mesh will receive the real node-face mesh and manipulate it. \nYou can shift (translate) and scale the whole mesh or single vertices. Additionally most of the manim functions are available as coloring single objects. Somehow Rotate does not work, because it only updates the copy of the rotation and therefore our own mesh class does not get updated.\n\n### Parameters\nAs parameters got a little overwhelming, there are a few default parameters for the meshes in `params.py`. You just need to pass kwargs that you want to change while creating the mesh.\n\n## Development\nIn PyCharm set `./src/`-folder as project sources root and `./tests/`-folder as tests sources root if necessary.\n\nInstall poetry according to your likings.\n\nActivate the poetry venv: `cd ./manim_meshes/`, then `poetry shell`\n\nInstall: `poetry install`\nIf you get errors, it is possible that you have to pip install `pycairo` and or `manimpango` manually (globally?), depending on your setup. Make sure to run `poetry install` until there are no more errors!\n\nAfter updating packages make sure to update poetry and your git .lock file: `poetry update`\n\nIf you implemented some features, update version using the matching poetry command: `poetry version prerelease|patch|minor|major`\nSee the Poetry [Documentation](https://python-poetry.org/docs/cli/#version).\nIf the CI works properly, Publishing to pypi on master branch is automatically, it can be done manually with the correct privileges: `poetry publish --build`. Don\'t hesitate to contact any of the developers or open issues.\n\n### Debugging\nLike with basic manim, create an executable Python file with something around:\n\n```python\nfrom tests.test_scene import SnapToGridScene\nif __name__ == "__main__":\n    scene = SnapToGridScene()\n    scene.render()\n```\n\nThen debug the file and place breakpoints as expected. May not work with the "renderer=opengl" flag that is necessary for some scripts. Please update this example if you found out how to do it.\n',
    'author': 'Brizar',
    'author_email': 'martin.steinborn@stud.tu-darmstadt.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bmmtstb/manim-meshes',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<3.9.0',
}


setup(**setup_kwargs)
