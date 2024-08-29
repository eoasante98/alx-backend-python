#!/usr/bin/env python3
'''
Description:    Import async_generator from 0-async_generator.py and then write
                a coroutine called async_comprehension that takes no args. The
                coroutine will collect 10 random numbers using an async
                comprehension and then return the 10 random numbers
'''


from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Return list of values yielded by async_genrator'''
    return [value async for value in async_generator()]
