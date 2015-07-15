
# The Knapsack Problem

You have a knapsack of size W and a set 'S' of n items of value v and weight w: S = {(v1, w1), (v2, w2), ..., (vn, wn)}. \\(W, vi, wi \in \mathbb{N}\\)

Find the combinations of items in set S that yield the highest combined value whilst having a total weight w <= W.

Assumption(s): all weights are non-negative integers. This is the _unbounded knapsack problem_.

## Brute Force

The simplest way to approach this problem is to just iterate all the possible \\(|\mathcal{P}(S)| = 2^n\\) items combinations (each item can be either in the bad or not in the bag), discard the combinations that do not satisfy the weight constraint and output the item combination that has the maximum value.

However, for values n > 30, this becomes [computationally unfeasible](http://www.grokit.ca/cnt/ComputationallyFeasible/).

## Dynamic Programming (DP) Solution (Tree Approach)

The state of the computation is a set of items not yet in the backpack (I), as well as 'c', the capacity left in the bag (w minus the weight of all items already in the bag). The crux of the DP trick is to notice that you do not need to carry I, but only the items remaining to consider.

Picture the problem with all items S. The cost of solving this using brute-force is \\(O(2^n)\\). If you remove the first item, you can solve that sub-problem in \\(O(2^{n-1})\\) time (do not forget to remove the weight of the item discarded to the problem). If you do this recursively, you end-up with a solution to a set of smaller problems which can be _combined_ into the solution to the complete problem.

Since you can remove n items from S, and that each time you remove an item you change the total weight of the solution, there can be at maximum n*W sub-problems to solve, yielding a DP cost of O(n*W).

### Code: Dynamic Programming Solution (Tree Approach)

dext.insertCode('knapsack.py')

dext.insertCode('k_tiny.in')

dext.insertCode('solutions.txt')

The small and large files can be found [on GitHub](https://github.com/grokit/website_grokit_ca/tree/master/articles/web/KnapsackProblem).

### Limitations of DP Approach

Why does it work only for integer weights?

If you have floating point values for the weight, then the amount of memory you need to hold is not bounded by n*W. Let's say all n items have different floating point weights, it is possible that you never land on the same weight value for a given i.

# Other Approaches

It may be more efficient to use the standard table approach where you build a 2D array for of i / w.

The fastest solution is most likely to use a branch and bound approach.

# References

- [Wikipedia](http://en.wikipedia.org/wiki/Knapsack_problem).
- [Stanford Algo II](https://class.coursera.org/algo2-2012-001/lecture).
  - [Stanford quiz question on knapsack problem](https://class.coursera.org/algo2-2012-001/quiz/attempt?quiz_id=85).
