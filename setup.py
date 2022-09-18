
from setuptools import setup

setup(name='shelly',
    version='0.1',
    description='Shelly device libary via HTTP API',
    url='https://github.com/trulede/shelly',
    author='Timothy Rule',
    license='MIT',
    packages=['shelly'],
    install_requires=[
        'requests',
    ],
    zip_safe=False)