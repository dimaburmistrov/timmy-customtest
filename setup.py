#!/usr/bin/env python

import os
from setuptools import setup

d = os.path.join(os.path.abspath(os.sep), 'usr', 'share', 'cudet')
d_files = [(os.path.join(d, root), [os.path.join(root, f) for f in files])
           for root, dirs, files in os.walk('rq')]
d_files.append((os.path.join(d), ['cudet-config.yaml', 'rq.yaml']))
d_files += [(os.path.join(d, root), [os.path.join(root, f) for f in files])
            for root, dirs, files in os.walk('db')]

setup(name='python-cudet',
      version='0.1',
      author='Dmitry Sutyagin',
      author_email='f3flight@gmail.com',
      license='Apache2',
      url='https://github.com/toha10/python-cudet',
      long_description=open('README.md').read(),
      packages=["cudet"],
      install_requires=['pyyaml'],
      data_files=d_files,
      include_package_data=True,
      entry_points={'console_scripts':
                    ['cudet=cudet.main:main']})
