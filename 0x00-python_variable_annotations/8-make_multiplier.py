#!/usr/bin/env python3
''' complex type annotated function '''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' function that returns a function '''
    def func(num: float):
        ''' function to be returned '''
        return num * multiplier
    return func
