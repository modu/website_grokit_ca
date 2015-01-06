
import ds.bst as bst

tree = bst.buildRandomBST(10)
print(tree.asInorderArray())


def visit(n):
    print(n.value)


def ino(root, visitFn=visit):
    root.vl = False
    root.vc = False
    S = [root]

    while len(S) > 0:
        n = S.pop()

        if n.vl == False:
            n.vl = True
            S.append(n)
            if n.left is not None:
                n.left.vl = False
                n.left.vc = False
                S.append(n.left)

        elif n.vc == False:
            n.vc = True
            visitFn(n)

            if n.right is not None:
                n.right.vl = False
                n.right.vc = False
                S.append(n.right)

ino(tree.root)
