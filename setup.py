# -*- Mode: Python -*-
"""two1

This tool uses the official PyPa packaging and click recommendations:
https://github.com/pypa/sampleproject
https://packaging.python.org/en/latest/distributing.html
http://click.pocoo.org/4/setuptools/
"""
from setuptools import setup
from setuptools import find_packages
from codecs import open
from os import path
import os

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
                    'arrow',
                    'base58',
                    'pytest',
                    'requests',
                    'simplejson',
                    'sha256',
                    'path.py',
                    'click',
                    'keyring',
                    'tabulate',
                    'mnemonic',
                    'protobuf >= 3.0.0a3',
                    'pyaes'
                    ]

# https://www.python.org/dev/peps/pep-0440/
VERSION=[0,2,1]
# This build number is set by the build environment(Jenkins)
# This is only intended to be used for internal builds or
# development builds.
# Release builds are created manually and the version is
# updated manually in those cases
if os.environ.get("BUILD_NUMBER"):
    VERSION.append("dev"+os.environ.get("BUILD_NUMBER"))

setup(
    name='two1',
    version=".".join([str(n) for n in VERSION]),
    description='Buy and sell anything on the internet with Bitcoin.',
    long_description=long_description,
    url='https://github.com/21dotco/two1',
    author='21,Inc',
    author_email='two1@21.co',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='bitcoin blockchain client server',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['two1', 'two1.lib', 'two1.commands', 'two1.bitcoin', 'two1.mining', 'two1.gen', 
            'two1.wallet', 'two1.crypto','two1.bitcurl', 
            'two1.djangobitcoin.djangobitcoin','two1.djangobitcoin.auth', 
            'two1.djangobitcoin.misc', 
            'two1.djangobitcoin.scipy_aas', 
            'two1.djangobitcoin.static_serve'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires,

    ext_modules=[],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'two1': ['two1-config.json'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('peers', ['data/default-peers.json'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # See: http://stackoverflow.com/a/782984/72994
    # http://click.pocoo.org/4/setuptools/
    entry_points={
        'console_scripts': [
            'two1=two1.cli:main',
            'wallet=two1.wallet.two1_wallet_cli:main'
        ],
    },
)
