#!/usr/bin/env python3
"""
Module 4-tasks
Implements alternative wait_n function
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawns wait_random n times with the specified max_delay

    Args:
      -n(int): No of times to spawn wait_random
      - max_delay(int): the delay in wait_random function

    Returns:
      -(list[float]): list of all delays in ascending order
    """
    # create a list of n tasks using task_wait_random
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # use asyncio.gather to run the tasks concurrently and collect the results
    delays = await asyncio.gather(*tasks)

    # return the sorted list of delays
    return sorted(delays)
