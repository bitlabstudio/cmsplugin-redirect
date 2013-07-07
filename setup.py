import os
from setuptools import setup, find_packages
import cmsplugin_redirect as app


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="cmsplugin-redirect",
    version=app.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, redirect, cms, plugin, placeholder',
    author='Daniel Kaufhold',
    author_email='daniel.kaufhold@bitmazk.com',
    url="https://github.com/bitmazk/cmsplugin-redirect",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=1.4.5',
        'South',
        'django-cms',
    ],
    tests_require=[
        'fabric',
        'factory_boy<2.0.0',
        'django-nose',
        'coverage',
        'django-coverage',
        'mock',
        'django-libs',
        'flake8',
        'ipdb',
    ],
    test_suite='cmsplugin_redirect.tests.runtests.runtests',
)
