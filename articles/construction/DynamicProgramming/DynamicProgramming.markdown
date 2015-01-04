
# Dynamic Programming

Key: figure-out what is the right set of sub-problems.

Problem is structured such that the solution to the big problem can be formulated on the assembly of solution to smaller sub-problems.

## Strategy

? start with assuming that you have the N items that form the solution, when walk backwards. Prove that you still have an optimal solution if you remove the (optimal) last item and solve for sub-problem. You then only have two possible worlds: one in which you have the optimal solution, and one in which you do not. ?
  - Q?: why doesn't that work when going forward instead of backwards?

# References

- Stanford Algo II [https://class.coursera.org/algo2-2012-001/lecture]().
- MIT Intro to Algo [http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/]().
