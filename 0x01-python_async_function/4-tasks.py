#!/usr/bin/env python3
''' executing multiple coroutines at the same time  '''
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''returns a list of all the delays '''
    lst = [task_wait_random(max_delay) for x in range(n)]
    done = [await task for task in asyncio.as_completed(lst)]
    return done
