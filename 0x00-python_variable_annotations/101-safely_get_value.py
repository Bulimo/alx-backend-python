#!/usr/bin/env python3
""" Module 101-safely_get_value.py """

from typing import TypeVar, Mapping, Any, Optional, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Union[T, None]) -> Union[Any, T]:
    """
     Safely retrieves value associated with the specified key from a dict.

    Parameters:
    - dct (Mapping[Any, T]): The dictionary to retrieve the value from.
    - key (Any): The key to look up in the dictionary.
    - default (T): The default value to return if the key is not present.

    Returns:
    Union[T, Any]: The value or the default value if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
