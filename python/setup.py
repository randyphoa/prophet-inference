# Copyright (c) Randy Phoa

# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os.path
import platform
import sys
import os

from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    install_requires = f.read().splitlines()

setup(
    name='fbprophet-inference',
    version='0.6.1',
    description='An inference only fork of Prophet (Python only)',
    url='https://facebook.github.io/prophet/',
    author='Randy Phoa <randyphoa@outlook.com>',
    author_email='randyphoa@outlook.com',
    license='MIT',
    packages=find_packages(),
    setup_requires=[
    ],
    install_requires=install_requires,
    python_requires='>=3',
    zip_safe=True,
    include_package_data=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    long_description="An inference only fork of Prophet (Python only)"
)
