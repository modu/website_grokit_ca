"""
Knapsack problem.

Solution for problem as stated in https://class.coursera.org/algo2-2012-001/quiz/attempt?quiz_id=85.

# TODO

- Able to trace-back the path.
- Use the 2D array method and compare performance.
- Use branch and bound and compare performance.  
"""

import copy

def readProblem(filename):
    fh = open(filename)
    W, n = [int(x) for x in fh.readline().strip().split(' ')]

    I = []
    for i in range(n):
        X = [x for x in fh.readline().strip().split(' ')]
        X[0] = int(X[0])
        X[1] = int(X[1])
        I.append( X )

    return (W, I)

def recurse(i, I, S, W, memo):

    if memo.get((i, W)) is not None:
        return memo[(i, W)]

    if i == len(I):
        return 0, []

    if W - I[i][1] >= 0:
        cPick, pathP = recurse(i+1, I, S, W - I[i][1], memo)
        cPick += I[i][0]
        # The pathP and such are not necessary to solve the problem, it is there so that we can check the path.
        pathP = copy.copy(pathP)
        pathP.append(i)
    else:
        cPick = -int(1e20)

    S.remove(i)
    cNoPick, pathNp = recurse(i+1, I, S, W, memo)
    S.add(i)

    if cNoPick >= cPick:
        sol = [cNoPick, pathNp]
    else:
        sol = [cPick, pathP]

    memo[(i, W)] = sol

    return sol

def solve(I, W):
    S = set(range(len(I)))
    return recurse(0, I, S, W, {})

filename = 'knapsack_large.in'
#filename = 'knapsack_small.in'
#filename = 'k_tiny.in'

W, I = readProblem(filename)

s = solve(I, W)
print(s)

t = 0
for p in s[1]:
    print('%i: %s' % (p, I[p]))
    t += I[p][0]
print('Total: %i.' % t)
