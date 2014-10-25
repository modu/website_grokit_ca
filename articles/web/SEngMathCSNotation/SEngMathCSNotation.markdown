
# SEngMathCSNotation

Literal: a fixed value. E.g: 1 or "one".

List: ~= Tuple

Tuple: (1,2,3)
	(1,2,3) != (3,2,1) since tuples (or n-tuples) are not ordered (ordering matters).
	(1,2,2,3) is a valid set (allows duplicates).

Set: {1,2,3}
	{1,2,3} = {3,2,1} since set are not ordered.
	{1,2,2} is not a valid set since set do not repeat elements.

Matrix: M_x,y. E.g: M_3,3.

A common convention with matrices is that the first number (x) represents the column, and the second (y) the line. In general, numbers in a column are a different _dimention_: they represent different type of entities whereas the line elements represent another instance of the same type of entity.

Since it is hard to represent matrices in a a text file, the coma (;) represents the end of a line. So [1, 2, 3; 4, 5, 6] is the same as:

	[1, 2, 3
	 4, 5, 6]
	 
Transpose is 'T', so [1, 2, 3; 4, 5, 6]T is:

	[1, 4
	 2, 5
	 3, 6]

## Notes

Distinction between what it is, and the underlying implementation.

Vector: same as a list, but usually contiguous in memory.

## References and Links

- http://en.wikipedia.org/wiki/Tuple#n-tuple
- http://en.wikipedia.org/wiki/ISO_31-11
- http://en.wikipedia.org/wiki/List_of_mathematical_symbols
- http://en.wikipedia.org/wiki/List_of_logic_symbols

↦: maps to

@@todo: merge with what I started in my thesis.
