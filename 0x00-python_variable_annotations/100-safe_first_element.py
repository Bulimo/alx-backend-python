#!/usr/bin/env python3
""" Module 100-safe_first_element """
from typing import Any, Sequence, Union, Optional

# The types of the elements of the input are not known


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function to retrieve the first elemnt

    Args:
      -lst(Sequence): A Sequence of items

    Returns:
      - (Any|None): First element, can Any type or None
    """
    if lst:
        return lst[0]
    else:
        return None
