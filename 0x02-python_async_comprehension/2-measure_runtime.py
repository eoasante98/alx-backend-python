#!/usr/bin/env python3
'''
Description: Import async_comprehension and write a measure_runtime coroutine
             that will execute async_comprehension 4 times in parallel using
             asyncio.gather.
             measure_runtime should measure the total runtime and return it.
'''


from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the runtime of async_comprehension executed 4 times in parallel
    '''
    first_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    next_time = time()

    return next_time - first_time
