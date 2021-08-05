"""Для юниттестов"""

import unittest
from main import all_ok, main
from cust_exceptions import (FailRepeatTimesError,
    InputParameterVerificationError, 
    ResultVerificationError)

valid_json_string_to_parse = '{"name": "Мишка", "email": "dsads@dsfsdf.ru", "age": 32}'
invalid_json_string_to_parse = '{"name": "Мишка", "email": "fsdafdasfdsa@fdsafsda.ru"}'
invalid_json_output = '{"name": "Мишка", "email": "erterwtre", "age": 32}'

class CheckDecoratorTest(unittest.TestCase):

    def test_error(self):
        with self.assertRaises(InputParameterVerificationError):
            main(data=invalid_json_string_to_parse, schema="schema.json")

if __name__ == '__main__':
    unittest.main()