#!/usr/bin/env python3
""" Module 0-basic_async_syntax """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay

    Args:
      - max_delay (int): maximum value to wait

    Returns:
      (float): the random value generated
    """
    val = random.uniform(0, max_delay)
    await asyncio.sleep(val)
    return val
