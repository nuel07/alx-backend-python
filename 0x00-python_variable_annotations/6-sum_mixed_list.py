#!/usr/bin/env python3
''' type annotated function of complex types '''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' function that returns sum of list values
    Args:
        mxd_lst(list): the list
    return: float
    '''
    return sum(mxd_lst)
