#!/usr/bin/env python3
'''Task 11's module. Safely get a value from a dictionary'''

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')  # Type variable for the default value


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    '''Safely retrieve a value from a dictionary or return a default value'''
    if key in dct:
        return dct[key]
    else:
        return default
