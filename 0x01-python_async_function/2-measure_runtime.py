#!/usr/bin/env python3
""" Module 2-measure_runtime """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay)

    Args:
      - n(int): number of tasks called in wait_n
      - max_delay(int): the maximum delay time to wait in wait_n

    Returns:
      (float): total_time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
