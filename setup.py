#!/usr/bin/env python

import os
from setuptools import setup

d = os.path.join(os.path.abspath(os.sep), 'usr', 'share', 'timmy-customtest')
d_files = [(os.path.join(d, root), [os.path.join(root, f) for f in files])
           for root, dirs, files in os.walk('rq')]
d_files.append((os.path.join(d), ['timmy-config-default.yaml', 'rq.yaml']))
d_files += [(os.path.join(d, root), [os.path.join(root, f) for f in files])
            for root, dirs, files in os.walk('db')]

setup(name='timmy-customtest',
      version='1.2.9',
      author='Dmitry Sutyagin',
      author_email='f3flight@gmail.com',
      license='Apache2',
      url='https://github.com/toha10/timmy-customtest',
      long_description=open('README.md').read(),
      packages=["timmy_customtest"],
      install_requires=['pyyaml'],
      data_files=d_files,
      include_package_data=True,
      entry_points={'console_scripts':
                    ['timmy-customtest=timmy_customtest.customtest:main']})
