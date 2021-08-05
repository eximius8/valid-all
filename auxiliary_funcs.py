"""Вспомогательные функци для тестирования валидатора валидола(:."""
from jsonschema import validate, exceptions
import json, re


def is_json_valid(data: dict, json_schema = 'schema.json') -> bool:
    """Валидация входных данных.
    
    data - входные данные
    json_schema - путь к файлу с json схемой"""
    with open(json_schema, 'r') as fschema:
        schema = json.loads(fschema.read())
    try:
        validate(instance=data, schema=schema)
        return True
    except exceptions.ValidationError:
        return False    


def clear_data() -> None:
    """Функция вызывается по умолчанию."""
    print("default_behavior чистит что натворила основная функция.")


def regex_validation(validated_str: str, patter = "[^\s]+") -> bool:
    """Функция для валидации выходных параметров."""    
    matched = re.match(patter, validated_str)
    return bool(matched)