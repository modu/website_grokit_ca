
# Computationally Feasible

Given problem x, *can you compute the answer*? Is it feasible to brute-force the answer?

This is easy to answer experimentally. If I define computable as something that I can run on my laptop in under 1 minutes with a slow language (Python):

    --------------------
    Loop 2^24 in 1.30s
    Loop 2^25 in 2.60s
    Loop 2^26 in 5.21s
    Loop 2^27 in 10.54s
    Loop 2^28 in 20.83s
    Loop 2^29 in 41.72s
    --------------------
    Loop 10^1 in 0.00s
    Loop 10^2 in 0.00s
    Loop 10^3 in 0.00s
    Loop 10^4 in 0.00s
    Loop 10^5 in 0.01s
    Loop 10^6 in 0.08s
    Loop 10^7 in 0.78s
    Loop 10^8 in 7.93s
    Loop 10^9 in 78.62s
    --------------------

So there it is, above 2^30 or 10^9 operations your computer runs in serious trouble.

We can scale the result above in order to get the results in terms of *years*:
    
    1 year:      ~ 10^14 ~= 2^46
    10 years:    ~ 10^15 ~= 2^49
    100 years:   ~ 10^16 ~= 2^52

**Conclusion**: if napkin-calculations reveal that your problem needs less than 10^9 operations, you can easily brute-force your way through it.
    
## Code Used to Generate Data

dext.insertCode('computationally_feasible.py')

## Real-Life Implication

I was solving the [Equal Sums](https://code.google.com/codejam/contest/1836486/dashboard#s=p2&a=2) problem of Google Code Jam. Looking at the numbers limit, it seemed like it was feasible to brute-force through all 1, 2 and 3-tuples. This is a O(n^3) algorithm with n == 500. Since it is ~10^8 operations, we know that we should be able to reasonably brute-force this. Now, I suggest that you read the math section of the problem in order to understand why this is likely to work (but not guaranteed -- if they had a set where only >= 6-tuples could be solution then I would never have been able to prove that no solution can be found). But our questions is different: **how long is it going to take to go through all the possible 3-tuples** and how does it match with the result we have above.

    All 2-tuples (500^2 ~= 10^5): 00.66 secs
    All 3-tuples (500^3 ~= 10^8): 20.57 secs

Now, we should not be surprised that it takes more time than our estimate in the first section: in this problem we do MUCH more every iteration. The fudge factor is from ~60 to ~2.5. Also, as we slow down as we go which is expected because we have an ever-expanding dictionary that keeps track of all the answers in memory. But the ~10^8 limit as what is feasible to brute-force in a few seconds remains!

Given the constraints we did not have to solve the problem; brute force was enough!
    
## Equal Sums All 3-Tuples Brute Force Solution

dext.insertCode('equal_sums_bruteforce.py')
