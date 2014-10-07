
def permut(lset, curr, completeFn):

    if len(lset) == 0:
        completeFn(curr)
        return

    ls2 = lset
    for s in ls2:
        lset.remove(s)
        curr.append(s)
        permut(lset, curr, completeFn)
        curr.remove(s)
        lset.add(s)

permut({'a', 'b', 'c'}, [], lambda x: print("".join(x)))
print('\n------\n')
permut({'a', 'b', 'c', 'd'}, [], lambda x: print("".join(x)))

