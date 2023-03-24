# standard library modules
import argparse
import random
from typing import List

# create argument parser obj and parse arguments
parser = argparse.ArgumentParser(description="Find if a value is present in A")
parser.add_argument('-n', default=20, type=int,
                    help="Size of array A")
parser.add_argument('-m', default=20, type=int,
                    help="Upper bound for possible array values [0..m]")
args = parser.parse_args()

def binary_search(A: List, key: int) -> bool:
    """Non recursive binary search function. Uses a while loop instead of
    recursive function calls.
    ---------------------------------------------------------------------------- 
    Args:
        A: list of sorted integers
        key: element to be searched for within the list
    Returns:
        is: boolean value for indicating wheter the element is or not in list"""
    if len(A) == 0:
        return False
    
    # initialize idxs for slicing A
    p = 0
    q = len(A)

    while q - p > 0:
        median = (p + q - 1) // 2
        if A[median] == key:
            return True
        else:
            if key < A[median]:
                q = median # search in left subarray
            else:
                p = median + 1 # search in right subarray

    return False

# create random array and sort it 
A = [random.randint(0, args.m) for _ in range(args.n)]
A.sort()

print(A)
for k in range(args.m + 1):
    b = binary_search(A, k)
    print(f"{k} -> {'T' if b==True else 'F'}")
