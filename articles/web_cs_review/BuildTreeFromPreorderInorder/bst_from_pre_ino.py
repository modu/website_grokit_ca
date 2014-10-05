
import ds.bst as bst

Node = bst.Node

def findLeftmostAInB(A, B):

    T = []

    for a in A:
        i = 0
        for b in B:
            if a == b:
                T.append((a, i))
                break
            i += 1
    
    if len(T) == 0:
        raise Exception("Mismatch")

    T.sort(key= lambda x: x[1])
    return T[0][0]

def findI(A, node):
    i = 0
    for a in A:
        if a == node.value:
            return i
        i += 1
    
    raise Exception("FindI Mismatch")

def build(pre, ino, node):
    iNode = findI(ino, node)
    print('iNode: ' + str(iNode))

    if iNode != 0:
        saL = ino[0:iNode]
        print('saL: ' + str(saL))
        lNode = Node(findLeftmostAInB(saL, pre)) 
        node.left = lNode

        if len(saL) > 1:
            build(saL, ino, lNode) 

    if iNode < len(ino) - 1:
        saR = ino[iNode+1:]
        print('saR: ' + str(saR))
        rNode = Node(findLeftmostAInB(saR, pre))
        node.right = rNode

        if len(saR) > 1:
            build(saR, ino, rNode)

preorder = [7, 10, 4, 3, 1, 2, 8, 11]
inorder = [4, 10, 3, 1, 7, 11, 8, 2]
node0 = Node(preorder[0])

build(preorder, inorder, node0)

