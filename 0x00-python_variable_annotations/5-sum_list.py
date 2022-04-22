#!/usr/bin/env python3
''' typed annotated function that returns sum of floats '''
from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' function that returns sum of floats in a list
    Args:
        input_list(list): the list of floats
    return: float
    '''
    return sum(input_list)
