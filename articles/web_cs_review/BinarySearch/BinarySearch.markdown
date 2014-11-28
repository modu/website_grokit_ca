
# CS Interview Question: Binary Search

## Question and Notes

Implement a binary search algorithm. You can assume the input to the algorithm is a sorted array.

- Be careful what happens if no match found (if the array does not contain the target value, do we successfully return -1?). 

- As with all algorithms, make sure that there is _progress_ at every loop / recursive call. A common error when implementing binary search is to have an edge case when the min / max get stuck when they are at a distance of 1 from each other (because then min + (max-min) / 2 == min using integer arithmetic).

Binary search in one of those problems that are used to illustrate recursive functions in textbook. However, it is a good practice to implement in a loop instead of with a recursive function whenever the complexity of using a loop is not much higher than using recursion. Note that it is __always__ possible to implement a recursive function in a loop (think of it that way: all you do when calling a function is putting variables on the stack and repeating operations from the current function, if you put the function's stack in variables and the instructions in a loop, the loop is equivalent to the recursive form).

## Code C++

dext.insertCode('binary_search.cpp')
    
