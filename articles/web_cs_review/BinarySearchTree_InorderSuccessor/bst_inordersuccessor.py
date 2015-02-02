
import random

import dcore.cs.bst as bst

def smallest(node):
    if node.left is None:
        return node
    else:
        return smallest(node.left)

def firstRightParent(node):
    if node.parent is None:
        return None

    if node.parent.left == node:
        return node.parent
    else:
        return firstRightParent(node.parent) 

def getInorderNext(n):
    if n.right is not None:
        return smallest(n.right)

    return firstRightParent(n)

if __name__ == '__main__':
    nTest = 10000
    for i in range(0, nTest):
        tree = bst.buildRandomBST(35)
        treeArray = tree.asInorderArray()

        pos = random.randint(0, len(treeArray) - 1)
        n = tree.getNodeFromValue(treeArray[pos])

        nn = getInorderNext(n)

        if len(treeArray) == pos + 1:
            assert nn is None
        else:
            #print('Returned, actual answer:', nn.value, treeArray[pos + 1])
            assert nn.value == treeArray[pos + 1]
