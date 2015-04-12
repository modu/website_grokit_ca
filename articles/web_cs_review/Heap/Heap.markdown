
# C++ Interview Question: Heap

# Question

Implement a [heap data structure](http://en.wikipedia.org/wiki/Heap_(data_structure).

# Notes

Given that for popMax(), you need to remove the root, put the 'last' element of the tree at root and 'bubble down'. For insert, you put an element at the 'last' position in the tree and "bubble up".

- Why is one using bubble up and the other using bubble down? What invariants would it violate if you did it the other way around (e.g. using bubble down in popMax())?

- Can you use the heap to implement a sorting algorithm? What are the advantages / disadvantages compared to quicksort?

- In a BST, the relationship is left / right, in a heap, it is up / down (all nodes under need to be <, does not matter is left or right). 

- Avl balanced tree can be used as a heap. You could also use a linked list, but performance would be awful for obvious reasons.

# Code

dext.insertCode('heap.cpp')

# Code Output

dext.insertCode('heap.cpp.out')
