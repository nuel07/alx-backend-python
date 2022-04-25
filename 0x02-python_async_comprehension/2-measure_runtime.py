#!/usr/bin/env python3
''' measures runtime '''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure total runtime and return it '''
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    stop = time.perf_counter()
    return stop - start
