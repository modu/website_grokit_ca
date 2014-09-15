
# C++ Interview Question: Factorial

**Implement the factorial function**.
    
- What is the approximate order of growth of this function?
    - Approximately for what input 'x' will you get an overflow if using 32 bit uint to compute?

- How can you detect overflow?

# Solution
    
## Approximate Order of Growth of Factorial

The factorial of n is the computation of: n(n-1)(n-2)(n-2)...(1) 'n' times. The conventional math definition is:

$$n!=\prod_{k=1}^n k \!$$

If you upper-bound that by approximating with n(n)(n)...(n) >= n(n-1)(n-2)(n-2)...(1). You can then upper-bound \\(n!\\) by \\(n^n\\).

### Approximately for what Input 'x' will you get an Overflow if Using 32 bit uint to Compute?

So let's say that you use C++ unsigned int to computer factorial. You know that the maximum value you can represent with the 32-bit integer is \\(2^{32}\\). So what you are asking yourself is the solution to: \\( n^{n} = 2^{32} \\). Taking the logarithm of n on both side doesn't help much. What you can do to approximate the answer is fix the base to two. \\( 2^{n} = 2^{32} \\) when n = 32 obviously. Since in n! the base is much larger (32), you know that the answer is n << 32. Now, if you use n = 8. You can see that as \\( 8^{8} = {2^{3}}^{8} = 2^{24} \\). So you know that 8 is fine. Using 16: \\( 16^{16} = {2^{4}}^{16} = 2^{64} \\). So 16 is too large. We have a pretty good ballpark number of somewhere between factorial(8) and factorial(16) you will overflow a 32 bit uint. The actual answer is 13:

        n   n!
        0   1
        1   1
        2   2
        3   6
        4   24
        5   120
        6   720
        7   5040
        8   40320
        9   362880
        10  3628800
        11  39916800
        12  479001600
        13  6227020800
        14  87178291200

        ==>
        factorial(12) = 479001600
        2^32          = 4294967296
        factorial(13) = 6227020800

## How to Detect Overflow

This is more tricky than it seems. 

- You can implement multiplication by x as x additions. This is of course slower but you will catch all overflows.

- You can check the CPU register for overflow (in C#, the 'checked' operand allows you to do that).

- Some compilers allow you go get a signal when there is an overflow (e.g: gcc -> -ftrapv).

- Can compute the logarithm of the numbers to multiply (that gives you the number of 0s)
    - Something very similar and more legit would be to count the number of 0 (in base 2 or 10). You can tell if it will overflow (or be 'very close to overflow') then by rounding to the next base-X number.

## Integer Arithmetic for Arbitrary Large Numbers

If you implement a number primitive which is mapped to an arbitrary, expendable set of bits, then you can always return the correct result without having to worry about overflow.

@@implement

## Importance of n! in Combinatorics

n! is the number of possible permutations of n different objects. For example, if you have the set: {a, b, c}, you can organize it in the following orders:
    
    {a, b, c}
    {a, c, b}
    {b, a, c}
    {b, c, a}
    {c, a, b}
    {c, b, a}
    
You have 6 possible orders, this is equal to the factorial of the size of your set (3! = 6). This is easy to see why if you think of the possibles in the terms of putting an item in a box. You begin with 3 empty boxes:

    {}{}{}

Now, when you choose the item for the first box, you have three choices: {a, b, c}. Your 3 possible choices are picking {a, b or c}.

    {a}{}{}
    
    {b}{}{}
    
    {c}{}{}

Now, when you select the second item, you only have **2** choices left:

    {a}{b}{}
    {a}{c}{}
    
    {b}{a}{}
    {b}{c}{}
    
    {c}{a}{}
    {c}{b}{}
    
... and the next step you only have one choice. Therefore, the first step you have 3 choices. Each of these choice can fork into two choices. The number of possibilities is therefore (3)x(2)x(1) = 3!

# Code

dext.insertCode('factorial.cpp')

# Code Output

dext.insertCode('factorial.cpp.out')
