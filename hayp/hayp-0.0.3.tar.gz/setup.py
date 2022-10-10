import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.3' #Muy importante, deberéis ir cambiando la versión de vuestra librería según incluyáis nuevas funcionalidades
PACKAGE_NAME = 'hayp' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Duver hernandez Cobos, Georffrey Julian Arevalo Prado, Sebastian Yañez Rojas' #Modificar con vuestros datos
DESCRIPTION = 'Librería para analizar redes de petri' #Descripción corta


#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
      'numpy',
      'graphviz',
      ]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    include_package_data=True
)