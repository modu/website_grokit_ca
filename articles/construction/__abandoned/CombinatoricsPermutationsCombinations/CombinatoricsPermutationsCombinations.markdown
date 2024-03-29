
# Combinatorics Permutations Combinations

http://www.mathsisfun.com/combinatorics/combinations-permutations.html



- python.functools

Set A: [a, b, c, d] of length n. How many different ways to combine those objects?

# Permutations

Allows repetitions

O(n^^n)

## What if Have Less Choices than Objects?

n choose k?
^^ this would eliminate repetitions.

# Combinations

Unique sets -- every letter can be there or not.

O(2^^n)

...or n!?

^^ what if you restrict the number of letters?

If repetitions are allowed: C(n+k+1, k).

http://en.wikipedia.org/wiki/Binomial_coefficient#Combinatorics_and_statistics

# Notes

- All: 
  - unique sets (go down in tree, always use 'one letter ahead'). Link with C(n, k)
    - unique sets, all size (link with 2^n).
  - possibilities (always repeat all elements, stop at given depth). Link with n^n
  - permutations (all elements possible except elements in a parent). Link with n!

# References

- https://www.khanacademy.org/math/algebra2/polynomial_and_rational/binomial_theorem/v/binomial-theorem-and-combinatorics-intuition

- http://www.cplusplus.com/reference/algorithm/next_permutation/
