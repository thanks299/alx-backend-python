#!/usr/bin/env python3
'''Task 12's module. Zooms in on an array
'''
from typing import List, Tuple


def zoom_array(lst: List, factor: int = 2) -> List:
    """Zooms in on an array by repeating each element 'factor' times."""
    zoomed_in: List = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
