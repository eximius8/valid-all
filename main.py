"""Основной модуль."""
from valid_all import valid_all
from auxiliary_funcs import clear_data, is_json_valid, regex_validation
import json


@valid_all(input_validation=is_json_valid, output_validation=regex_validation, default_behavior=clear_data)
def all_ok(data: str, schema: str) -> str:
    """Основная функция."""
    dict_data = json.loads(data)
    return dict_data['name']


@valid_all(input_validation=is_json_valid, output_validation=regex_validation, default_behavior=clear_data)
def main(data: str, schema: str) -> str:
    """Основная функция."""
    dict_data = json.loads(data)
    return dict_data['name']


if __name__ == '__main__':
    pass
    # all_ok(data=valid_json_string_to_parse, schema="schema.json")
    # main(data=invalid_json_output, schema="schema.json")
