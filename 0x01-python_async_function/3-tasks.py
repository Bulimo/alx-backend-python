#!/usr/bin/env python3
""" Module 3-tasks """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio task

    Args:
      - max_delay(int): maximum delay

    Returns:
      - (asyncio.Task): created task
    """
    return asyncio.create_task(wait_random(max_delay))
