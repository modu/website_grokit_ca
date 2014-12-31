
# Article not completed ... come back later

# @@TODO

- finish article :P

- combinations
- permutations
- given a,b,c and d, how many different combinations with no repetitions?

# Solving Problem By Enumerating All States in the Solution Space (A.K.A. Solving Problems by Searching)

Having a mental model of the solution space is a great step towards finding a solution to the problem. It turns out that a surprising number of problems can be solved by simply:

1. Enumerating all states in the solution space.
2. Evaluating each state with a function that yields whether or not the state is a valid solution to the problem.

The drawback is that it becomes quickly indefeasible as problem get complex because the number of possible states often grows exponentially as a function of the problem size. Nevertheless, this is often a first good step towards having a mental image of the problem. From this exhaustive enumeration of states, it sometimes become obvious that there are shortcuts that can be taken that yield a faster algorithm.

## Base Case: How Many Combinations of m Objects, Each of Which Has n Distinct States?

This is the (mathematically) easiest family of problems to model the state for.

Example problem: locks. There is a safe with m dials. Each dial can be set to a number from 1 to n. What is the total number of combinations that the lock has? (A similar problem is [telephone words](../TelephoneWords)).

If we pick low numbers, let's say 2 dials (m = 2) and each dial has 3 possible numbers (n = 3). Here are the possible dial positions ("states" of the solution space):

        (1, 1)
        (1, 2)
        (1, 3)
        (2, 1)
        (2, 2)
        (2, 3)
        (3, 1)
        (3, 2)
        (3, 3)

... for a |solution space| = 9 possible states. What happens when we increase n or m? Let's say we add a dial (m = 3). This is equivalent to adding a column to the state enumeration above. For each of the possible state (9), there are now another 3 possibilities added by the new dial. This amount to multiplying the number of possible state by 3 for every dial added. Now if we changed the dials to have move possible numbers, then what change is the _base_; for every dial that we add the multiplying factor becomes 4. This leads to the following generalization:

$$\\#dial\\_states^{\\#dials}$$

... or to be more generic:

$$\\#states^{\\#slots}$$

... which is the same as the more compact:

$$n^{m}$$.

I like the "states-slots" image because it leads to a good generic mental picture that can be used for many problems: there are slots (place holders) and each of these slots have a finite number of possible states.

        ----------------------------------
        | slot_1 | slot_2 | ... | slot_n | --> slot increase ==> increase exponent.
        ----------------------------------
        --> #state-per-slot increase ==> increase base of exponent.

Another useful mnemonic is the parallel with binary numbers. It is well known that given a binary number with m digits, there are \\( m^2 \\) possible decimal numbers. Each time a digit is added (a 'slot' is added), the number of decimal numbers representable by that binary number is multiplied by two. If a base n is used instead of a base 2, we fall back on the same \\((n^m)\\) equation.

## (Base Case)++: When Every Choice Removes A Combination From the Remaining Solution Space

Another frequent problem category occurs when **a state cannot be used twice**. For example, let's say you have an apple (1), an orange (2) and a banana (3). You have three meal and eat one fruit per meal. How many combinations can you do?

    Note: 1: apple, 2: orange, 3: banana

    (1, 2, 3)
    (1, 3, 2)
    (2, 1, 3)
    (2, 3, 1)
    (3, 1, 2)
    (3, 2, 1)

... there are 6 different possibilities. Note that this is similar to the "locks problem", except that one a state (fruit) has been picked, it cannot be picked again (therefore, all repeated occurrences such as (1, 1, 1) are removed from the solution space). In order to enumerate more complicated problems, it helps to represent the possible choice with a tree structure for which an object must only be present once for any root-leaf path:

![123TreeNoDuplicate](../../static/SolvingProblemByEnumeratingAllStates_123TreeNoDuplicate.jpg)

Now counting the number of possible states is much easier: there are n objects (n = 3), and every time an object is picked, there are n-1 remaining objects to pick from. Therefore, the number of possible states in the problem is: 3*(3-1)*(3-2) = 6. For a generic number of objects n, this is equivalent to:

$$n!$$.

For our "fruit selection" problem, we can now easily compute the number of state in the problem space: 3! = 6.
