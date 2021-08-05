"""Для юниттестов"""

import unittest
from main import all_ok, main


class CheckDecoratorTest(unittest.TestCase):

    def test_error(self):
        self.assertRaises(main(data=invalid_json_string_to_parse, schema="schema.json"), Exception)