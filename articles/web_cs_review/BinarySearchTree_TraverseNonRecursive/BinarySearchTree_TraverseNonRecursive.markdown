
# C++ Interview Question: Binary Search Tree, Traverse without Recursion

# Question

Given a binary search tree (BST) with the following node structure:

        class Node
        {
        public:

            Node* left;
            Node* right;
            int value;
        };

- Write code to navigate the tree in [preorder, postorder and inorder](http://en.wikipedia.org/wiki/Tree_traversal) **non-recursively**.

- For more basic BST questions, see [BinarySearchTree](/cnt/BinarySearchTree).

## References (in Order of Awesomeness)

- [Sedgewick's Algorithms book's website, chapter on BST](http://algs4.cs.princeton.edu/32bst/).
- [BST Wikipedia](http://en.wikipedia.org/wiki/Binary_search_tree).

# Solution(s)

# Code

dext.insertCode('bst_norecurse.cpp')

# Code Output

dext.insertCode('bst_norecurse.cpp.out')

## Explanation

**inorderTraversal_NoRecurse** is especially tricky. Non-recursive inorder traversal is very unnatural.

A way to think of this solution is that it is the same thing as the recursive solution, except that we use the stack to remember what would be stored in the _recursion stack_. Let's say you have the following tree:

       7
      / \
     3   10
     
... in the recursive code, you would have: {recurse left, print value, recurse right}. Since recurse left is picked first, the *stack pointer* will bring you back to 'print value' when the rest of the call is done. In the non-recursive mode, we store the node in the following order: {10, 7*, 3},  with 7 having a flag that it has already been touched (next time around print the value). This is the equivalent of recursing on node 3, then when it is done visit 7 without recursing and recurse in 10. The stack with a flag can be seen as just a clever way to simulate recursive behavior.

<a href="http://web.cs.wpi.edu/~cs2005/common/iterative.inorder">It is actually possible to do this without adding extra data (besides the stack).</a>

