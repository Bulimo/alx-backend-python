#!/usr/bin/env python3
""" Module 8-make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returnsa another function

    Args:
      - multiplier(float): Argument to the function

    Returns:
      - (Callable): function that takes a float and multiples by multiplier
    """
    def fun(mult: float) -> float:
        """
        Returns mult * multiplier
        """
        return mult * multiplier

    return fun
