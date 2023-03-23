# standard library modules
from typing import List

def binary_search(A: List, key: int) -> int:
    """Non recursive binary search function. Uses a while loop instead of
    recursive function calls.
    ---------------------------------------------------------------------------- 
    Args:
        A: list of sorted integers
        key: element to be searched for within the list
    Returns:
        idx: list index where the first occurence was found. Returns None if key
             is not present"""
    if len(A) == 0:
        return None
    
    # initialize idxs for slicing A
    p = 0
    q = len(A)

    while len(A[p: q]) > 0:
        median = (p + q - 1) // 2
        if A[median] == key:
            return median
        else:
            if key < A[median]:
                q = median # search in left subarray
            else:
                p = median + 1 # search in right subarray

    return None
