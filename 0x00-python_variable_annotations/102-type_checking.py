#!/usr/bin/env python3
""" 102-type_checking """
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zooms in on each element of the input tuple
    by repeating each element a specified number of times.

    Parameters:
    - lst (Tuple[int]): The input tuple containing integers.
    - factor (int): factor to repeat (default is 2).

    Returns:
    Tuple[int]: List containing each element repeated
      according to the specified factor.
    """
    zoomed_in = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
