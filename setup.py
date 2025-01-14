from setuptools import setup, find_packages

setup(
    name='my-python-api',
    version='0.1.0',
    description='A simple Python API project',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(where='app'),
    package_dir={'': 'app'},
    install_requires=[
        # List your project dependencies here
        # 'Flask',
        # 'SQLAlchemy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)