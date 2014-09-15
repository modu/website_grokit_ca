
# Google Code Jam: Bullseye

## Question

This is a solution for the [Bullseye](https://code.google.com/codejam/contest/2418487/dashboard) problem from GCJ. Their explanation lacks the mathematic development. 

This is a fairly easy problem if you know that there is a formula that yields the result of a sum:

$$\sum_{ i \mathop =1}^ni = \frac{n(n+1)}{2}$$

If you can express the 'black area' as a sum, then you can reduce this long sum by a single equation. Once you have this, you can binary search the problem space which will yield the answer in O(log(n)) time.

![Solution](../../static/bullseye.jpg)

# Math and Summation

Legend is that a young [Leonhard Euler](http://en.wikipedia.org/wiki/Leonard_Euler) was being pesky in class so he was asked to sum numbers from 1 to 10000. To his teacher's dismay, he came up with the answer very quickly. Euler told his teacher that is was rather easy. Let's say you sum 1 to 10, you can organize the numbers in this way: 

    1    10
    2    9
    3    8
    4    7
    5    6
    6    5
    7    4
    8    3
    9    2
    10   1

Notice that all the rows sum to 11, and organizing the number this way will have every number twice. So the sum will be 10*(row)/2 = 10*11/2. If you replace 10 and 11 with variables, you get the formula seen earlier: n*(1+1)/2.

This begs the questions: if you can reduce sums to an algebraic form, what about sum of powers? It turns out that you can always reduce sum of powers using [Faulhaber's formula](http://en.wikipedia.org/wiki/Faulhaber%27s_formula). So if you ever see a sum of the form:

$$\sum_{k=1}^n k^p = 1^p + 2^p + 3^p + \cdots + n^p$$

... know that you can calculate the result of the sum with a simple formula.

## Code

dext.insertCode('bullseye.py')

