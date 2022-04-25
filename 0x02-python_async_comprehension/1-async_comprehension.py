#!/usr/bin/env python3
''' An async Comprehension '''
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Function that return a list of 10 random numbers '''
    lst = [x async for x in async_generator()]
    return lst
