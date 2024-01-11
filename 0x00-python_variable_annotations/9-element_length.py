#!/usr/bin/env python3
""" Module 9-element_length """
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of each element in the given list.

    Parameters:
      - lst (Iterable[Sequence]): The list of sequence items.

    Returns:
      - (List[Tuple[Sequence, int]]): A list of tuples of
        each element and its length.
     """
    return [(i, len(i)) for i in lst]
