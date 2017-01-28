from setuptools import setup, find_packages

README = 'use mako templating in your YAML files'

requires = [
        'pyyaml',
        'mako',
        ]

setup(name='yaml-mako',
      version='0.1.1',
      description=README,
      long_description=README,
      url='https://github.com/haarcuba/yaml_mako',
      classifiers=[
          "Programming Language :: Python",
      ],
      author='Yoav Kleinberger',
      author_email='haarcuba@gmail.com',
      keywords='yaml, mako, templating',
      packages=find_packages(),
      py_modules = [ "yaml_mako" ],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
