
# Notation for Software Engineering and CS

CS and Math have a rich and well defined syntax to express the difference between different primitives (e.g: literal, set, list, ...). However, since ideas and documentation often needs to be done in plain-text, there is no official

This article attempts to achieve the following goals:

1. All-in one place definition and explanation of the notation for common computer science primitives.
2. For all the primitives in 1., suggest a consistent annotation for plain-text files.
3. A reference place for myself so that I am consistent with my notation.

## Elementary Types

### Literal

Literals are simple values. For example, in `int i = 1`, i is a literal. Literals start with a lowercase letter. Examples:

		int i = 1;
		float pressure = 0.5;
		string name = "Marcus Aurelius";

### Arrays

An array is a collection of elements. Those elements can be literals, or complex objects.

Arrays uses square brackets: [1, 2, 3, 4, 1, 2].

They are a collection of element with no special restrictions (can repeat, no specific order). Arrays are usually contiguous in memory.

Note that many languages (such as C++) use curly brackets as array initializers -- that conflicts with that is typically used in Mathematics: curly banquets '{' and '}' are usually reserved for _sets_.

### Tuple

A tuple is a sequence of elements _where the order matters_. A n-tuple is a sequence of n elements. For example, (1, 2, 3) is a 3-tuple.

Since the _order matters_, (1, 2, 3) and (3, 2, 1) are two distinct tuples.

Value can repeat in tuples and are not necessarily ordered. So (5, 5, 5, 1, 4) is a valid tuple. (5, 5) is a distinct tuple from (5).

Square brackets '[]' are also sometime used as a notation for tuple since tuples are very similar to arrays.

- http://en.wikipedia.org/wiki/Tuple

### Set

A set is a collection of distinct objects. Think of a set as telling you if an element is present or not.

For example, the set of people at a party can either contain or not contain each of your friend once.

Set use curly brackets; {1, 2, 3} is a set of items 1, 2 and 3.

Since order does not matter in sets, {1, 2, 3} = {3, 2, 1}; they are considered equivalent. However, it is less confusing to order the elements in a set as a matter of convention, so {1, 2, 3} would be preferred to {3, 2, 1} or {2, 3, 1}, although all three sets are equivalent.

Note that {1, 2, 2} is not a valid set since set do not repeat elements; 2 is present or not, having it twice in the set is meaningless.

- http://en.wikipedia.org/wiki/Set_(mathematics)
- http://en.wikipedia.org/wiki/Set-builder_notation
- http://0a.io/0a-explains-set-theory-and-axiomatic-systems-with-pics-and-gifs

## Complex Types

### Graphs

Graphs are a set of vertices (singular: vertex, somtimes also called nodes) where some pair of vertices are connected by edges (sometimes called links).

A popular notation for graphs is `G = (V, E)`, where V is a set of vertices which are connected by edges E, which are 2-element subsets of V.

For example:

		V = {1, 2, 3, 4, 5, 6}
		E = {{1, 2}, {1, 5}, {2, 3}, {2, 5}, {3, 4}, {4, 5}, {4, 6}}

... is a valid graph.

- http://en.wikipedia.org/wiki/Graph_(mathematics)
- @@todo: adjacency list and matrix notation for graph.

### Matrix

A matrix is a rectangular 2D-array of elements arranges in _rows_ and _columns_.

A column is vertical whereas a row is horizontal.

A common convention with matrices is that the first number (y) represents the column, and the second (x) the line. In general, column represent different _dimentions_: they represent different type of entities whereas the line elements represent another instance of the same type of entity.

Matrixes can be represented in plain-text files using a capital letter followed by an underscore, then the column and row number: M_y,x. For example, the last element of a 3x3 matrix 'M' is denoted as M_3,3.

The complete matrix can be enumerated by using square brackets. Since it is hard to represent matrices in a a text file, the coma (;) represents the end of a line. So [1, 2, 3; 4, 5, 6] is the same as:

	[1, 2, 3
	 4, 5, 6]

Transpose is 'T', so [1, 2, 3; 4, 5, 6]T is:

	[1, 4
	 2, 5
	 3, 6]

http://en.wikipedia.org/wiki/Matrix_(mathematics)

## References and Links

- Commonly used mathematical symbols: http://en.wikipedia.org/wiki/ISO_31-11
- Graph notation and set examples: http://en.wikipedia.org/wiki/Graph_(mathematics)
- Hash functions: http://research.microsoft.com/pubs/64588/hash_survey.pdf, check section 2.1.