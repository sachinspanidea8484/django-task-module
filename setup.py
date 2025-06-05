from setuptools import setup, find_packages

setup(
    name='django-task-module',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Reusable Django Task Management App',
    author='Your Name',
    install_requires=[
        'django>=3.2',
    ],
)
