#!/usr/bin/env python3
""" Module 7-to_kv """
from typing import Union, Tuple
from math import pow


def to_kv(k: int, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from the passed arguments

    Args:
      - k(int): 1st argument
      - v(int|float): 2nd argument, can be an int or a float

    Returns:
      - (Tuple): A tuple of format(k: v) 
    """
    val: float = pow(v, 2)
    return (str(k), val)
