
# C++ Interview Question: Heap

# Question

Implement a [heap data structure](http://en.wikipedia.org/wiki/Heap_(data_structure)).

# Notes

Given that for popMax(), you need to remove the root, put the 'last' element of the tree at root and 'bubble down'. For insert, you put an element at the 'last' position in the tree and "bubble up".

- Why is one using bubble up and the other using bubble down? What invariants would it violate if you did it the other way around (e.g. using bubble down in popMax())?

- Can you use the heap to implement a sorting algorithm? What are the advantages / disadvantages compared to quicksort?

# Code

dext.insertCode('heap.cpp')

# Code Output

dext.insertCode('heap.cpp.out')
