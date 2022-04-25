#!/usr/bin/env python3
''' An async generator '''
import random
import asyncio


async def async_generator() -> float:
    ''' yields a random number between 0 and 10 '''
    for x in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
