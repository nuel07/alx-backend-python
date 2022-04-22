#!/usr/bin/env python3
''' type annotated function that returns floored float'''
import math


def floor(n: float) -> int:
    ''' function that returns floor of a float
    Args:
        n(float): the float value
    return: float
    '''
    return math.floor(n)
