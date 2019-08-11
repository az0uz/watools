import os
from setuptools import setup

requires=[
    "netCDF4",
    "pyproj",
    "joblib",
    "pycurl", # export PYCURL_SSL_LIBRARY=openssl
    "h5py",
    "pyshp"
]

setup(
    name = "watools",
    packages=['watools'],
    install_requires=requires
)
