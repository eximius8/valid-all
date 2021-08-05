from valid_all import valid_all
from auxiliary_funcs import clear_data, is_json_valid, regex_validation
import json


valid_json_string_to_parse = ""
invalid_json_string_to_parse = ""


@valid_all()
def main(json_data: str) -> str:
    """Основная функция"""
    data = json.loads(json_data)
    return data['name']


if __name__ == '__main__':
    main()