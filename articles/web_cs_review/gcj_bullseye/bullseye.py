# solved small, large!

import math

filename = 'tiny.in'
filename = 'A-small-practice.in'
filename = 'A-large-practice.in'

fh = open(filename, 'r')

nCases = int(fh.readline())


def getRadius(r, a):
    return r + 1 * a


def areaBlack(r, nCircles):
    """
    http://en.wikipedia.org/wiki/Faulhaber%27s_formula
    http://en.wikipedia.org/wiki/Square_pyramidal_number
    http://en.wikipedia.org/wiki/Summation
    """
    return nCircles * (2 * r + 2 * nCircles - 1)


def howManyCircles(r, mm2Paint):

    nMin = 1
    nMax = 1e20

    while True:

        evPos = int(nMin + (nMax - nMin) / 2)
        area = areaBlack(r, evPos)

        if area <= mm2Paint and areaBlack(r, evPos + 1) > mm2Paint:
            break

        if area > mm2Paint:
            nMax = evPos - 1
        else:
            nMin = evPos + 1

    return evPos


def howManyCirclesSlow(r, mm2Paint):

    mm2T = 0
    a = 1
    while mm2T <= mm2Paint:

        ra = getRadius(r, a)

        if a == 1:
            mm2T += ra ** 2 - r ** 2
        else:
            ra_ = getRadius(r, a - 1)
            mm2T += ra ** 2 - ra_ ** 2

        a += 2

    rv = (a - 1) / 2 - 1

    if rv > 0:
        return rv
    return 0

S = []
for i in range(0, nCases):
    rv = fh.readline().strip()
    r, t = [int(v) for v in rv.split(' ')]

    nCirc = howManyCircles(r, t)

    st = 'Case #%i: %i' % (i + 1, nCirc)
    print(st)
    S.append(st)

fh = open(filename.replace('.in', '.out'), 'w')
fh.write("\n".join(S))
fh.close()
