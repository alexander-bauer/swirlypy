#!/usr/bin/env python3

import subprocess, os
from distutils.core import setup

print("Obtaining version... ", end="")
version = subprocess.check_output(["git", "describe", "--dirty=+"],
        universal_newlines=True)
print(version)

setup(name='swirlypy',
        version=version,
        description='Python courseware',
        author='Alexander Bauer',
        author_email='sasha@crofter.org',
        url='https://github.com/SashaCrofter/swirlypy',
        scripts=['swirlypy/utils/swirlytool'],
        packages=['swirlypy', 'swirlypy.questions']
        )
