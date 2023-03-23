# Logarithmic Occurence Counter and Binary Search Trees 

This repository contains an implementation of an algorithm for computing the number of occurrences of a particular key value within a sorted array whose elements may be repeated. The complexity of the algorithm is logarithmic in the array size and does not depend on the number of repeated elements.

In addition, this repository includes a non-recursive implementation of the binary search algorithm and a brief analysis of interesting properties for balanced binary search trees (BSTs). So, stay here if you want to know about a cool property that involves the golden ratio and the Fibonacci sequence!

### Counting occurrences
---
Suppose that there is an array $A$ of size $n$ which contains a sorted list of integers that may be repeated or not. The goal is to compute the number of occurrences of a particular key which may be present or not inside the array, and do it in $O(\log n)$ as well as independent from the number of occurrences $m$ of a particular key. We already know that sequentially traversing this array would lead to a running time of $O(n)$. But, what if we use a search algorithm with running time of $O(\log n)$ to find an occurrence and sequentially traverse our algorithm in both directions? Again, this would have a running time of $O(m)$ and it would be $O(n)$ in the worst case, since $m \leq n$.

Despite our previous attempts not meeting the solution constraints, they give us some insight for designing our algorithm. It is important to mention that, for a particular element $a_k$ at index $k$ inside the array, the property

$$
  a_p \leq a_k \leq a_q
$$

holds for every $0 \leq p, q \leq n - 1$. It follows then from this property that if $a_p = a_q$ then it must be the case that

$$
  a_k = a_p = a_q
$$

for $p < k < q$. This allows us to, for a particular key value $v$, find the leftmost $p$ and rightmost $q$ occurrence index values for key $v$, and simply compute the number of occurrences with $c = q - p + 1$. The problem now reduces to finding two index values, if we can find both of these values in $O(\log n)$ time, we would have a running time of $2O(\log n) = O(\log n)$. The problem resembles that of binary search, with a subtle difference: we are not looking for any index, we are looking for the index values that enclose our range of repeated elements.

The search method for finding the rightmost occurrence I propose is briefly described as:
1. Split the array in half by computing the middle index.
2. If the middle value is lower than the key value, search in left subarray. If not, search in the right one.
3. Repeat until you reach a subarray with size 0.

The algorithm is the same for finding the leftmost occurence with the conditions in step 2 reversed. The process of iteratively reducing the search domain in halves leads us, informally speaking, to a running time of $O(\log n)$ and by the previous argument, we say that this conting algorithm runs in $O(\log n)$. Of course, there are some details regarding index tracking and termination conditions I intentionally swept under the rug for the sake of clarity. You can check `count_occurences.py` script where I implemented this solution.

### Running the counting algorithm

The script `count_occurences.py` contains a function called `count_occurrences`, which computes both index values by calling `find_right` and `find_left` functions and substracting their results. The script creates a random sorted array of size `n` with elements ranging from 0 to `m`. It then runs the counting function for each of the `m + 1` elements and displays their number of occurrences. You can run the script by typing `python count_occurrences.py -n=N -m=M` being `N` and `M` parameters of your choice. Here's a screenshot for how the output should look like:

![image](https://user-images.githubusercontent.com/95151624/227092570-73231767-c313-4584-9283-4ffe58f57e74.png)


### Non-recursive implementation of binary search
---
The recursive binary search algorithm may be convenient for code compactness and its elegancy. When we run such a recursive algorithm to search for an occurrence inside an array $A$ of size $n$ with $n$ large we may have memory issues due to the nature of how recursive calls are handled. Everytime we make a neste function call, the algorithm has to stop executing the function you are currently at, save the state of the processor inside the call stack, run the current function, restore the previous processor state so that you can continue executing your first function. In a recursive function, we must consecutively pile up this kind of information for every recursive call until we reach a base case. When $n$ is large, the cost of running this kind of code may become prohibitive.

We can sacrifice some code compactness in order to avoid this memory overhead and write the recursive binary search algorithm using a `while` loop. The script `bin_search.py` contains an implementation of this idea.

### Analyzing balanced BSTs
---

