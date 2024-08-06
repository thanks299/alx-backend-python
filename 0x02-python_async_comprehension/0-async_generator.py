#!/usr/bin/env python3
"""Task 0 module
"""
import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """Asynchronously generate a sequence of random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
