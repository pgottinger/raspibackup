from setuptools import setup

import os

setup(
    name='RaspiBackup',
    version='0.1',
    description='Django front-end for doing backups using rsync on the Raspberry Pi',
    author='Peter Gottinger',
    url='https://github.com/pgottinger/raspibackup',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=[
        'raspibackup',
    ],
     classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)