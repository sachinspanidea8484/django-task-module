from setuptools import setup, find_packages

setup(
    name='django-task-module',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.2',
    ],
)
