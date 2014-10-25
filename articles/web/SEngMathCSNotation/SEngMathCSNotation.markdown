
# SEngMathCSNotation

Literal: a fixed value. E.g: 1 or "one".

List: ~= Tuple

Vector: same as a list, but usually contiguous in memory. (Should we just shove this in implementation detail?).

Tuple: (1,2,3)
	(1,2,3) != (3,2,1) since tuples (or n-tuples) are not ordered (ordering matters).
	(1,2,2,3) is a valid set (allows duplicates).

Set: {1,2,3}
	{1,2,3} = {3,2,1} since set are not ordered.
	{1,2,2} is not a valid set since set do not repeat elements.


## Notes

Distinction between what it is, and the underlying implementation.

## References and Links

- http://en.wikipedia.org/wiki/Tuple#n-tuple
- http://en.wikipedia.org/wiki/ISO_31-11
- http://en.wikipedia.org/wiki/List_of_mathematical_symbols
- http://en.wikipedia.org/wiki/List_of_logic_symbols

↦: maps to

@@todo: merge with what I started in my thesis.
