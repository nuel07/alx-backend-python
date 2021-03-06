#!/usr/bin/env python3
''' my first asynchronous coroutine '''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    ''' asynchronous routine that waits for a random delay '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
