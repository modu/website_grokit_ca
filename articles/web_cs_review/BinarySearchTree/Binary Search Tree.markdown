
# C++ Interview Question: Binary Search Tree

## Question

Given a binary search tree (BST) with the following node structure:

        class Node
        {
        public:

            Node* left;
            Node* right;
            Node* parent;
            int value;
        };

- Write code that allows to build a BST given a set of values to insert.
    - Write code that allows to check if the BST is valid.

- Write code to delete a node given its _value_.
        
- Write code to navigate the tree in [preorder, postorder and inorder](http://en.wikipedia.org/wiki/Tree_traversal):
    - Do all three recursively.
    - Would it be harder to implement non-recursively?

- Navigate the tree using breadth first search (BFS).

- For all the tree traversal mentioned above, what is the space complexity?

- Whats is the average complexity of (for random inputs):
    - Adding a node?
    - Retrieving a node?
    - Deleting a node?

- Can you think of degenerate but valid BST for which the above time complexity are not accurate?

- Compare a BST with a heap, why is a heap better if you want to keep track of max / mins?

## Advanced Problems

- Write code to navigate the tree in [preorder, postorder and inorder](http://en.wikipedia.org/wiki/Tree_traversal) **non-recursively**.
    - See [BinarySearchTree_TraverseNonRecursive](/cnt/BinarySearchTree_TraverseNonRecursive).

## References

- [Sedgewick's Algorithms book's website, chapter on BST](http://algs4.cs.princeton.edu/32bst/).
- [BST Wikipedia](http://en.wikipedia.org/wiki/Binary_search_tree).

# Code

dext.insertCode('bst.cpp')

# Code Output

dext.insertCode('bst.cpp.out')

## Understanding the Recursive Nature of the Tree

Considering all edges can exist or not, a node can only be in two configurations:

               p
              /
             /
            a
           / \
          /   \
         lc   rc

or:

          p
           \
            \
             a
            / \
           /   \
          lc   rc

... that is, a node can either have a parent or not, a left or right child or not, and the parent can either be a left or a right parent.

The parent-child relationship is recursive. This has the following interesting properties:

    - When walking up from a node to a root, the current node is _smaller than every right parent_ and _bigger than every left parent_. This can be inferred directly by the parent child relationship that every node in the left child subtree is smaller than the current node. So, as you walk up as a left child, you _must_ be smaller than the parent node.

    - If a node has both a right parent and a right child, both are larger than the current node and the right child is smaller than the right parent. This is because the right child is to the left of the right parent, therefore smaller.

## Node Deletion

You need to maintain the fundamental property of the BST: _for any node, all left children are smaller, all right children are bigger_. 

After locating the node to delete, it is a matter of stitching the tree back together. The way to do it is to find a node in the tree that you can _switch_ with the node to delete so that the fundamental property of BST mentioned above is still obeyed.

## Notes

- Inorder traversal always yield the nodes in sorted order.

