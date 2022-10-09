from setuptools import setup, find_packages
from os import path as os_path
import guiboweb

this_directory = os_path.abspath(os_path.dirname(__file__))


# 读取文件内容
def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


# 获取依赖
def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(name='guiboweb',
      python_requires='>=1.5',
      version=guiboweb.__version__,
      description='guiboweb description',
      long_description=read_file('README.md'),
      long_description_content_type="text/markdown",
      url='https://github.com/guofei9987/blind_watermark',
      author='guiboweb',
      author_email='guofei9987@foxmail.com',
      license='MIT',
      packages=find_packages(),
      platforms=['linux', 'windows', 'macos'],
      install_requires=['numpy', 'opencv-python', 'PyWavelets'],
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'guiboweb = guiboweb.optparse:main'
          ]
      })
