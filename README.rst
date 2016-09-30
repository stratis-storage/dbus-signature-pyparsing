A Parser for a D-Bus Signature
==============================

A parser for a dbus signature.

Introduction
------------

This module contains a parser for dbus signatures constructed using the
pyparsing library (http://pyparsing.wikispaces.com/).

The grammar follows the informal specifications at
https://dbus.freedesktop.org/doc/dbus-specification.html.
This grammar is a very simple one, parsable by an LL(1) parser.

The grammar has undergone significant testing using the Hypothesis testing
library (http://hypothesis.works/).

Usage and Implementation Hints
------------------------------

Usage of the library to verify that a string is a signature is fairly
straightforward::

   >>> from dbus_signature_pyparsing import Parser
   >>> parser = Parser()
   >>> parser.PARSER.parseString("a(qy)", parseAll=True)

If parseString() does not raise a pyparsing exception, the argument string
is a valid signature.

Note that the empty string is a valid signature. Thus, it is important to
require that the parser parse the entire string by setting the parseAll
parameter to True. If parseAll is False, which is the default, the parser
can always parse the empty string, and every string will be parsed and verified
to be a valid signature.

The Parser object exposes all its sub-parsers as instance attributes.
The PARSER attribute is the top-level parser, suitable for parsing general
signatures. The COMPLETE attribute parses what is defined in the
informal specification as a "single complete type". The CODE attribute is
equivalent to the specification's "type code".

The parser is easily used either by delegation or by inheritance. Each
sub-parser attribute is a ParserElement; consequently each sub-parser supports
the addParseAction() method. To customize the basic parser to return a
particular value as a result of having parsed a signature invoke the
addParseAction() method on each appropriate sub-parser with an appropriately
chosen method. The modified parser should then return the desired value when
the parseString() method is invoked on a valid signature string.
For further assistance, consult pyparsing's extensive documentation at
http://pyparsing.wikispaces.com/ and https://pythonhosted.org/pyparsing/.
