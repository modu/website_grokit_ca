
# CS Interview Question: Binary Search Tree, Find Inorder Successor 

# Question

Given a node frim a binary search tree, give the next in-order node.

# Solution

The easiest solution by far would be to go up to the root not, then just output all the nodes in an array inorder. Find the node provided in that array, then simply return the next node.

However, the real goal of the question is to do it without the extra array. This is possible by inspecting all possible cases in a BST (in terms of node configurations) and then walk to the next inorder node (if any).

dext.insertCode('bst_inordersuccessor.py')

