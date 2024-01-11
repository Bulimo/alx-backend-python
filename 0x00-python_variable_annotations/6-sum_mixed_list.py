#!/usr/bin/env python3
""" Module 6-sum_mixed_list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sums the values of the mxd_lst list

    Args:
      - mxd_lst(list): list containing float and int values

    Returns:
      - (float): sum of the list mxd_lst
    """
    sum: float = 0

    for val in mxd_lst:
        sum += val

    return sum
