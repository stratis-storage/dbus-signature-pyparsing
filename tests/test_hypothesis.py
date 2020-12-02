# Copyright 2016 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Hypothesis-based tests of signature parsing.
"""

# isort: STDLIB
import unittest
from os import sys

# isort: THIRDPARTY
from hypothesis import given, settings

# isort: FIRSTPARTY
from hs_dbus_signature import dbus_signatures

# isort: LOCAL
from dbus_signature_pyparsing import Parser

settings.register_profile("tracing", deadline=None)
if sys.gettrace() is not None:
    settings.load_profile("tracing")


class ParseTestCase(unittest.TestCase):
    """
    Test parsing various signatures.
    """

    _PARSER = Parser()

    @given(dbus_signatures())
    @settings(max_examples=50, deadline=None)
    def test_parsing(self, signature):
        """
        Test that parsing is always succesful on valid strings.
        """
        self.assertIsNotNone(self._PARSER.PARSER.parseString(signature, parseAll=True))
