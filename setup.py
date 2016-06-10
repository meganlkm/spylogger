import os
from pip.req import parse_requirements
from pip.download import PipSession
from setuptools import setup, find_packages

BASEDIR = os.path.dirname(os.path.abspath(__file__))
VERSION = open(os.path.join(BASEDIR, 'VERSION')).read().strip()
INSTALL_REQS = parse_requirements('requirements.pip', session=PipSession())

setup(
    name='spylogger',
    version=VERSION,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    description='Python logging for SPS libraries.',
    long_description=open('README.md').read(),
    url='https://github.com/SPSCommerce/spylogger',
    author='meganlkm',
    author_email='mwood@spscommerce.com',
    install_requires=[str(ir.req) for ir in INSTALL_REQS]
)