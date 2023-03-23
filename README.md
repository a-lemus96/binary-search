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

The algorithm is the same for finding the leftmost occurence with the conditions in step 2 reversed. The process of iteratively reducing the search domain in halves leads us, informally speaking, to a running time of $O(\log n)$.

### Non-recursive implementation of binary search
---

### Analyzing balanced BSTs
---

