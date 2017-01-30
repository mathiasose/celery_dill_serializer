import os

from setuptools import setup

VERSION = '0.1.3'


def readme(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


def requirements(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return list(line.strip() for line in f.readlines() if line.strip() != '')


setup(
    name='celery_dill_serializer',
    packages=['celery_dill_serializer'],
    version=VERSION,
    description='Dill serializer for Celery 4.0+',
    long_description=readme('README.rst'),
    author='Mathias Ose',
    author_email='mathias.ose@gmail.com',
    url='https://github.com/mathiasose/celery_dill_serializer',
    download_url='https://github.com/mathiasose/celery_dill_serializer/releases/tag/{}'.format(VERSION),
    install_requires=requirements('requirements.txt'),
    keywords=['celery', 'dill', 'serialization'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
)
