"""
Python packaging file for setup tools.
"""

# isort: STDLIB
import os

# isort: THIRDPARTY
import setuptools


def local_file(name):
    """
    Function to obtain the relative path of a filename.
    """
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


README = local_file("README.rst")

with open(local_file("src/dbus_signature_pyparsing/_version.py")) as o:
    exec(o.read())  # pylint: disable=exec-used

setuptools.setup(
    name="dbus-signature-pyparsing",
    version=__version__,  # pylint: disable=undefined-variable
    author="Anne Mulhern",
    author_email="amulhern@redhat.com",
    url="https://github.com/stratis-storage/dbus-signature-pyparsing",
    description="dbus signature parser",
    long_description=open(README, encoding="utf-8").read(),
    platforms=["Linux"],
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["pyparsing"],
    package_dir={"": "src"},
    packages=setuptools.find_packages("src"),
)
