#!/usr/bin/env python3
"""Task 1 module
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns
    a list of all the delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted_delays(delays)


def sorted_delays(delays: List[float]) -> List[float]:
    """
    Returns a sorted list of delays.

    Args:
        delays (List[float]): List of delays.

    Returns:
        List[float]: Sorted list of delays.
    """
    if len(delays) <= 1:
        return delays
    pivot = delays[len(delays) // 2]
    left = [x for x in delays if x < pivot]
    middle = [x for x in delays if x == pivot]
    right = [x for x in delays if x > pivot]
    return sorted_delays(left) + middle + sorted_delays(right)
