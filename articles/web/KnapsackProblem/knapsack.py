"""
Knapsack problem.

Solution for problem as stated in https://class.coursera.org/algo2-2012-001/quiz/attempt?quiz_id=85.

# TODO

- Use the 2D array method and compare performance.
- Use branch and bound and compare performance.
"""

import copy


def readProblem(filename):
    fh = open(filename)
    currWeight, n = [int(x) for x in fh.readline().strip().split(' ')]

    I = []
    for i in range(n):
        X = [(int(x), int(y)) for x, y in [fh.readline().strip().split(' ')]]
        I.append(X[0])

    return (currWeight, I)


def recurse(i, I, S, currWeight, memo):

    if memo.get((i, currWeight)) is not None:
        return memo[(i, currWeight)]

    if i == len(I):
        return 0

    if currWeight - I[i][1] >= 0:
        cPick = recurse(i + 1, I, S, currWeight - I[i][1], memo)
        cPick += I[i][0]
    else:
        cPick = -int(1e20)

    S.remove(i)
    cNoPick = recurse(i + 1, I, S, currWeight, memo)
    S.add(i)

    if cNoPick >= cPick:
        sol = cNoPick
    else:
        sol = cPick

    memo[(i, currWeight)] = sol

    return sol


def solve(I, W):
    S = set(range(len(I)))
    return recurse(0, I, S, W, {})

#filename = 'knapsack_large.in'
#filename = 'knapsack_small.in'
filename = 'k_tiny.in'

W, I = readProblem(filename)

s = solve(I, W)
print(s)

