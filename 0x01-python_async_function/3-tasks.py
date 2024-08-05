#!/usr/bin/env python3
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio Task for wait_random"""
    return asyncio.create_task(wait_random(max_delay))
