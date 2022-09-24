from setuptools import setup

setup(
    name='pflib',
    version='0.1',
    description='Simple library for send metric into pushgateway',
    url='https://github.com/OldTyT/pflib',
    install_requires=["urllib3"],
    packages=['pflib'],
)
