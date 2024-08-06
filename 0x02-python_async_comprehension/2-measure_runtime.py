#!/usr/bin/env python3
import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel and measure the total runtime."""
    start_time = time.time()  # Record the start time
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()  # Record the end time
    return end_time - start_time  # Calculate the total runtime
