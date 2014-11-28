
# C++ Interview Question: Permutations Of A String

Given a string (e.g: "abc"), generate all possible strings that can be obtained by switching the positions of the letters.

## Discussion

Note that this is equivalent to the slightly more wonky: given a set of letters of length n, output all n-tuples that can be formed by combining those letters (without repetitions).

## Code

dext.insertCode('permutations_of_set.py')

### Output 

dext.insertCode('permutations_of_set.py.out')

# A Little bit of Math

For a n-tuple, the first letter has n free choices, the second n-1 and so forth. You end up with a total of n! possible strings.

# A More Difficult Alternative, M-tuples Allowing Repetitions

Would it be difficult to change the problem to generate all m-tuple from the set of n letters (m >= n) if repetitions are allowed?

