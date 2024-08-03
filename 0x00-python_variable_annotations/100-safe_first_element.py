#!/usr/bin/env python3
'''Task 10's module.
'''
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a sequence or None if the sequence is empty
    '''
    if lst:
        return lst[0]
    else:
        return None
