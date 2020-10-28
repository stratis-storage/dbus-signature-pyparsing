#!/usr/bin/python

"""
Invoke pylint with pre-selected options.
"""

# isort: STDLIB
import argparse
import subprocess
import sys

arg_map = {
    "check.py": [
        "--reports=no",
        "--disable=I",
        "--msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}'",
    ],
    "setup.py": [
        "--reports=no",
        "--disable=I",
        "--msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}'",
    ],
    "src/dbus_signature_pyparsing": [
        "--reports=no",
        "--disable=I",
        "--msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}'",
    ],
    "tests": [
        "--reports=no",
        "--msg-template='{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}'",
    ],
}


def get_parser():
    """
    Generate an appropriate parser.

    :returns: an argument parser
    :rtype: `ArgumentParser`
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "package", choices=arg_map.keys(), help="designates the package to test"
    )
    return parser


def get_command(namespace):
    """
    Get the pylint command for these arguments.

    :param `Namespace` namespace: the namespace
    """
    return ["pylint", namespace.package] + arg_map[namespace.package]


def main():
    """
    The main method
    """
    args = get_parser().parse_args()
    return subprocess.call(get_command(args), stdout=sys.stdout)


if __name__ == "__main__":
    sys.exit(main())
