#!/usr/bin/env python3
""" Module 0-async_generator.py """
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.

    Returns:
      (float): yielded random number
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
