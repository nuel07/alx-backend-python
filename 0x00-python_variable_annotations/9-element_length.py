#!/usr/bin/env python3
''' function to be type annotated '''
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' function that returns list '''
    return [(i, len(i)) for i in lst]
