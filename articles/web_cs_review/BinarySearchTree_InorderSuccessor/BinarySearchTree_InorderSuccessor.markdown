
# CS Interview Question: Binary Search Tree, Find Inorder Successor 

# Question

Given a node from a binary search tree, give the next in-order node.

# Solution

The easiest solution by far would be to go up to the root, then just output all the nodes in an array inorder. Find the node provided in that array, then simply return the next node.

However, the real goal of the question is to do it without the extra array. This is possible by inspecting all possible cases in a BST (in terms of node configurations) and then walk to the next inorder node (if any).

Something that can help tremendously is to picture the recursive nature in tree problems, you are always in on of the following three relationships (where any of the link to child can also be none):

![Solution](../../static/bst_recurse.png)

dext.insertCode('bst_inordersuccessor.py')

The bst.py file (from the dcore repository) allows you to visualize the BST generated:

![bst](../../static/g.dot.png)
