#!/usr/bin/env python3
""" Module 5-sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats

    Args:
      - input_list(list): list of floats

    Returns:
      -(float): sum of the input_list items
    """
    sum: float = 0

    for item in input_list:
        sum += item

    return sum
