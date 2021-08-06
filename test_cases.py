"""Для юниттестов"""

import unittest
import json
from valid_all import valid_all
from auxiliary_funcs import is_json_valid, clear_data, regex_validation
from cust_exceptions import InputParameterVerificationError, ResultVerificationError, FailRepeatTimesError

valid_json_string_to_parse = '{"name": "Мишка", "email": "mikhail@trunov.ru", "age": 32}'
invalid_json_string_to_parse = '{"name": "Мишка", "email": "fsdafdasfdsa@fdsafsda.ru"}'
invalid_json_output = '{"name": "Мишка", "email": "erterwtre", "age": 32}'


@valid_all(input_validation=is_json_valid, output_validation=regex_validation, default_behavior=clear_data)
def with_defaul(data: str, schema: str) -> str:
    """Функция для тестирования с заданным default_behavior."""
    dict_data = json.loads(data)
    return dict_data['email']


@valid_all(input_validation=is_json_valid, output_validation=regex_validation)
def without_default(data: str, schema: str) -> str:
    """Функция для тестирования с незаданным default_behavior."""
    dict_data = json.loads(data)
    return dict_data['email']


@valid_all(input_validation=is_json_valid, output_validation=regex_validation, on_fail_repeat_times=0)
def zero_repeat_time(data: str, schema: str) -> str:
    """Функция для тестирования с незаданным default_behavior."""
    dict_data = json.loads(data)
    return dict_data['email']


class CheckDecoratorTest(unittest.TestCase):
    """Тестирование декоратора."""

    def test_output(self):
        self.assertEqual(with_defaul(data=valid_json_string_to_parse, schema="schema.json"), "mikhail@trunov.ru")

    def test_input_error(self):
        with self.assertRaises(InputParameterVerificationError):
            with_defaul(data=invalid_json_string_to_parse, schema="schema.json")

    def test_output_error(self):
        with self.assertRaises(ResultVerificationError):
            without_default(data=invalid_json_output, schema="schema.json")
    
    def test_invalid_json(self):
        with self.assertRaises(InputParameterVerificationError):
            with_defaul(data=invalid_json_string_to_parse, schema="schema.json")
    
    def test_zero_repeat_times(self):
        with self.assertRaises(FailRepeatTimesError):
            zero_repeat_time(data=valid_json_string_to_parse, schema="schema.json")
    
    def test_output_with_regex(self):
        self.assertRegex(with_defaul(data=valid_json_string_to_parse, schema="schema.json"), r"[^@]+@[^@]+\.[^@]+")


if __name__ == '__main__':
    unittest.main()
