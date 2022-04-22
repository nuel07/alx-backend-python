#!/usr/bin/env python3
''' type annotated function that returns a tuple '''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' returns a tuple of a string and float
    Args:
        k(str): the string
        v(int or float): the number
    return: tuple
    '''
    return (k, v * v)
