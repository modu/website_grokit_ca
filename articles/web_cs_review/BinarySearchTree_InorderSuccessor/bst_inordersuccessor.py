
import dcore.ds.bst as bst


def firstLeftChildUp(n):
    while not bst.BST.isLeftChild(n, n.parent):
        n = n.parent
        if n is None:
            return None
    return n 

def getInorderNext(n):
    if n.parent is None:
        if n.right is None:
            return None
        return bst.BST.leftmostChild(n.right)
    elif not bst.BST.isLeftChild(n, n.parent):
        return bst.BST.leftmostChild(n.right)
    else:
        if n.right is not None:
            return bst.BST.leftmostChild(n.right)
        else:
            return firstLeftChildUp(n.parent)

tree = bst.buildRandomBST()
treeArray = tree.asInorderArray()
print(treeArray)

n = tree.getNodeFromValue(treeArray[ int(len(treeArray) / 2)])
print(n)

nn = getInorderNext(n)
print(nn)


