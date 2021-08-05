"""Для юниттестов"""

import unittest
import json
from valid_all import valid_all
from auxiliary_funcs import is_json_valid, clear_data, regex_validation
from cust_exceptions import InputParameterVerificationError, ResultVerificationError  # FailRepeatTimesError

valid_json_string_to_parse = '{"name": "Мишка", "email": "dsads@dsfsdf.ru", "age": 32}'
invalid_json_string_to_parse = '{"name": "Мишка", "email": "fsdafdasfdsa@fdsafsda.ru"}'
invalid_json_output = '{"name": "Мишка", "email": "erterwtre", "age": 32}'


@valid_all(input_validation=is_json_valid, output_validation=regex_validation, default_behavior=clear_data)
def with_defaul(data: str, schema: str) -> str:
    """Функция для тестирования с заданным default_behavior."""
    dict_data = json.loads(data)
    return dict_data['name']


@valid_all(input_validation=is_json_valid, output_validation=regex_validation)
def without_default(data: str, schema: str) -> str:
    """Функция для тестирования с незаданным default_behavior."""
    dict_data = json.loads(data)
    return dict_data['name']


class CheckDecoratorTest(unittest.TestCase):
    """Тестирование декоратора."""

    def test_input_error(self):
        with self.assertRaises(InputParameterVerificationError):
            with_defaul(data=invalid_json_string_to_parse, schema="schema.json")

    def test_output_error(self):
        with self.assertRaises(ResultVerificationError):
            without_default(data=invalid_json_output, schema="schema.json")
    
    def test_invalid_json(self):
        with self.assertRaises(InputParameterVerificationError):
            with_defaul(data=invalid_json_string_to_parse, schema="schema.json")


if __name__ == '__main__':
    unittest.main()
