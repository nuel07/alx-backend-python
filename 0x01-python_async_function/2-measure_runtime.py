#!/usr/bin/env python3
''' measures the runtim '''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' measures total execution time '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()
    run_time = stop - start
    return run_time / n
