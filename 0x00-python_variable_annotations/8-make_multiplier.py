#!/usr/bin/env python3
'''
Description:    takes a float multiplier as argument and returns a
                function that multiplies a float by the multiplier
Argument:       multitplier: float
'''


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return function that multiplies float by multiplier'''
    return lambda x: x * multiplier
