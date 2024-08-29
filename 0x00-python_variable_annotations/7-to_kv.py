#!/usr/bin/env python3
'''
Description:    takes a string and an integer as arg and
                returns a tuple
Argument:       k: str
                v: Union[int, float]
'''


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return tuple consisting of k and the square of v'''
    return (k, v * v)
