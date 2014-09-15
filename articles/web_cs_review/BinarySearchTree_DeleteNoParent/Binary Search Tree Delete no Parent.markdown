
# C++ Interview Question: Binary Search Tree, Delete Node (When Tree has No 'Parent' Nodes)

## Question

Given a binary search tree (BST) with the following node structure:

        class Node
        {
        public:

            Node* left;
            Node* right;
            int value;
        };

Given a value v, delete the associated node (or the first one that is found in the tree if duplicate values).
        
# Code

dext.insertCode('bst_delNoParent.cpp')

# Code Output

dext.insertCode('bst_delNoParent.cpp.out')

# Solution Explained

You need to maintain the fundamental property of the BST: _for any node, all left children are smaller, all right children are bigger_. 

The insight is that once you have located the node to delete (just traverse the tree), you can establish a deletion convention. You can obey the above invariant of BSTs with deleting the node which value comes just before the node to delete (the rightmost node of the left child) or the successor (the leftmost node of the right child). Pick one (in this case we picked the successor). Then you just have to swap the node to delete with the successor, then issue a _deleteMin_ on the right child of the node to delete (which happens to be the node we just swapped).

_deleteMin_ is easy to implement since it cannot have two children (if it did, it would not be a min). Therefore, you just point the parent to the child and delete the node.
