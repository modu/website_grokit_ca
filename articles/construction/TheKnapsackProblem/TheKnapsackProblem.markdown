
# The Knapsack Problem

You have a knapsack of size w and a set 'S' of n items of value v and weight w: S = {(v1, w1), (v2, w2), ..., (vn, wn)}.

## Brute Force

\\(2^n\\).

## Dynamic Programming Solution (Tree Approach)

The state of the computation is a set of items not yet in the backpack (I), as well as 'c', the capacity left in the bag (w minus the weight of all items already in the bag).

The crux of the DP trick is to notice that you do not need to carry I, but only the items remaining to consider.

? why does it work only for integer weights and non-negative values / weights ?

## Dynamic Programming Solution (Table Approach)

## Dynamic Programming Solution (Branch and Bound Approach)

@@todo

# References

- http://en.wikipedia.org/wiki/Knapsack_problem
- Stanford Algo II [https://class.coursera.org/algo2-2012-001/lecture]().
  - Quiz question on knapsack problem: [https://class.coursera.org/algo2-2012-001/quiz/attempt?quiz_id=85]().
