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
    name='fbprophet_inference',
    version='0.7',
    description='An inference only fork of Prophet (Python only)',
    url='https://github.com/randyphoa/prophet-inference',
    author='Randy Phoa',
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
    long_description="This is an inference only fork of Prophet for Python. The primary purpose of this package is to deploy a Prophet model in a light weight environment for the purpose of inference/prediction. This implementation does not require heavy dependencies such as pystan(Stan) and Cython which requires a C/C++ compiler. It is a purely Python based and does not require additional binaries."
)
