# standard library imports import argparse
import argparse
import random
from typing import List

# create argument parser obj and parse arguments
parser = argparse.ArgumentParser(description="Count key ocurrences in an array")
parser.add_argument('-n', default=20, type=int,
                    help="Size of array A")
parser.add_argument('-m', default=20, type=int,
                    help="Upper bound for possible array values [0..m]")
args = parser.parse_args()


def find_right(A: List, key: int, p, q) -> int:
    while (q - p) > 0:
        median = ((q - 1) + p) // 2
        # test middle element
        if A[median] > key:
            # search left
            q = median
        else:
            # search right
            p = median + 1

    return q

def find_left(A: List, key: int, p, q) -> int:
    while (q - p) > 0:
        median = ((q - 1) + p) // 2
        # test middle element
        if A[median] < key:
            # search right
            p = median + 1
        else:
            # search left
            q = median
    
    return p

def count_occurrences(A: List, key: int) -> int:
    """Given a sorted array A of elements that may be repeated, compute the
    number of occurrences of a given key. The algorithm was designed s.t. the 
    complexity of the algorithm is logarithmic in the array size and does not
    depend on the number of repeated elements.
    ----------------------------------------------------------------------------
    Args:
        A: array of sorted integers
        key: element for counting the number of occurrences
    Returns:
        count: number of occurences of key in array A"""
    # explore right side of the subarray
    kmax = find_right(A, key, p=0, q=len(A))
    # explore left side of the subarray
    kmin = find_left(A, key, p=0, q=len(A))
    count = kmax - kmin

    return count


# create random array and sort it
A = [random.randint(0, args.m) for _ in range(args.n)]
A.sort()

print(A)
for k in range(args.m + 1):
    print(f"{k} -> {count_occurrences(A, k)}")
