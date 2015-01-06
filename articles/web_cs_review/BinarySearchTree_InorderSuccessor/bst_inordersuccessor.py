
import random

import dcore.ds.bst as bst


def firstLeftChildUp(n):
    if n.parent is None:
        return None
    while not bst.BST.isLeftChild(n, n.parent):
        n = n.parent
        if n is None or n.parent is None:
            return None
    return n.parent


def getInorderNext(n):
    if n.parent is None:
        if n.right is None:
            return None
        return bst.BST.leftmostChild(n.right)
    elif bst.BST.isLeftChild(n, n.parent):
        if n.right is None:
            return n.parent
        return bst.BST.leftmostChild(n.right)
    else:
        if n.right is not None:
            return bst.BST.leftmostChild(n.right)
        else:
            return firstLeftChildUp(n.parent)

if __name__ == '__main__':
    nTest = 1
    for i in range(0, nTest):
        tree = bst.buildRandomBST(35)
        tree.toGraph()
        treeArray = tree.asInorderArray()
        print(treeArray)

        pos = random.randint(0, len(treeArray) - 1)
        n = tree.getNodeFromValue(treeArray[pos])
        print(n)

        nn = getInorderNext(n)
        print(nn)

        if len(treeArray) == pos + 1:
            assert nn is None
        else:
            assert nn.value == treeArray[pos + 1]
