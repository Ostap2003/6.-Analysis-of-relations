"""
transitive_counter.py

The module is for counting the number of transitive relations on a set of n elements.
In order to know the number of transitive relations on a set of n, call count_transitive function
with parameter n.

[[[[[[[[[   Description of the algorithm of finding the number of transitive relations  ]]]]]]]]]

Suppose that we want to find the number of transitive relations on a set of n elements.

Step 1. Find the number of transitive relations on a set of n elements, whose boolean matrix
representations contain 1 in 1st row and 1st column:
    1 ? ? ... ?
    ? ? ? ... ?
    . . . .   ?
    . . .  .  ?
    . . .   . ?
    ? ? ? ... ?

Step 2. Find the number of transitive relations on a set of n elements, whose boolean matrix
representations contain 0 in 1st row and 1st column:
    0 ? ? ... ?
    ? ? ? ... ?
    . . . .   ?
    . . .  .  ?
    . . .   . ?
    ? ? ? ... ?

Step 3. Add the results from step 1 and step 2 and, thus, get the number of transitive relations
on a set of n elements.

To perform step 1 and step 2, we need to find solutions to their subproblems. In particular, to
perform step 1, we have to find solutions for two subproblems:

Subproblem 1. Find the number of transitive relations on a set of n elements, whose boolean matrix
representations look as follows:
    1 1 ? ... ?
    ? ? ? ... ?
    . . . .   ?
    . . .  .  ?
    . . .   . ?
    ? ? ? ... ?

Subproblem 2. Find the number of transitive relations on a set of n elements, whose bolean matrix
representations look as follows:
    1 0 ? ... ?
    ? ? ? ... ?
    . . . .   ?
    . . .  .  ?
    . . .   . ?
    ? ? ? ... ?

Then we will add together the results from subproblem 1 and subproblem 2.
However, to solve the subproblem 1, we have to solve another two subsubproblens. It's the same with
subproblem 2 and all of their subproblems and subprolems of their subproblems. We will stop dividing
problems into subproblems, when all the entries of the matrices are defined (either 1 or 0) or when
we know that matrix that is partly completed can't be transitive for sure. For example, for the
following matrix
    1 0 1 ... 1
    1 1 0 ... 0
    . . . .   0
    . . .  .  0
    . . .   . 1
    1 0 1 ... 0
we can check weather it is transitive or not. And for the following matrix
    1 1 1 ... 0
    1 0 ? ... ?
    . . . .   ?
    . . .  .  ?
    . . .   . ?
    ? ? ? ... ?
we know that, no matter with what values we replace the question marks, the matrices of this class
will not be transitive.

Thus, knowing number of transitive relations for some classes of n by n matrices, we can find the
overall number of transitive relations on a set of n elements.
"""

from typing import List


def count_transitive(n: int):
    """
    Return number of transitive relations on a set of n elements.

    >>> count_transitive(0)
    1
    >>> count_transitive(1)
    2
    >>> count_transitive(2)
    13
    >>> count_transitive(3)
    171
    """

    return count_transitive_containing(n, [])


def count_transitive_containing(n: int, prefix: List[bool]):
    """
    Recursively calculate and return number of transitive relations on a set of n elements, whose
    matrices contain the given prefix in the beginning.

    Precondition: prefix[:-1] doesn't ruin the transitivity of matrix.

    Examples:

    # The following examples will count all transitive relations on a set of 2 elements,
    # whose matrices look as follows:
    #   1 1
    #   ? ?
    # where ? can be either 1 or 0
    >>> count_transitive_containing(2, [True, False])
    4

    # The following example will count all transitive relation on a set of 3, whose matrices look
    # as follows:
    #   0 1 1
    #   0 ? ?
    #   ? ? ?
    # where ? can be either 1 or 0
    >>> count_transitive_containing(3, [False, True, True, False])
    13

    # The following example will show how many relations on a set of 4 elements there are.
    # In other words, it will find how many relations on a set of 4 there are, whose matrices look
    # as follows:
    #   ? ? ? ?
    #   ? ? ? ?
    #   ? ? ? ?
    #   ? ? ? ?
    # where ? can be either 1 or 0
    >>> count_transitive_containing(4, [])
    3994
    """

    is_transitive = check_transitive(prefix, n)

    # first base case
    if not is_transitive:
        return 0

    # second base case
    if n**2 == len(prefix):
        if is_transitive:
            return 1
        return 0

    # recursive calls
    num_transitive_rels_in_subproblem1 = count_transitive_containing(n, prefix + [True])
    num_transitive_rels_in_subproblem2 = count_transitive_containing(n, prefix + [False])

    return num_transitive_rels_in_subproblem1 + num_transitive_rels_in_subproblem2


def check_transitive(prefix: List[bool], n: int) -> bool:
    """
    Return False if n by n matrix that begins with prefix can't be transitive. Otherwise, return
    True.
    Precondition: matrix that begins with prefix[:-1] can be possibly transitive.

    The function checks whether the last element of prefix (the one which was added the last)
    doesn't ruin possible transitivity of matrix.

    The function is needed for optimization of the algorithm. It helps us to know whether all the
    relations from some particular class of relations are not transitive, so we don't need to go
    through those relations and count the number of transitive relations among them.
    """

    if len(prefix) > 0:
        last_index = len(prefix) - 1
        num_row = last_index // n
        num_col = last_index % n

        if prefix[last_index] == False:
            for i, j in zip(range(num_row*n, min((num_row+1)*n, len(prefix))),
                                                                    range(num_col, len(prefix), n)):
                if prefix[i] == prefix[j] == True:
                    return False
            return True
        else:
            # now we know that prefix[last_index] is equal to True
            for i in range(num_row*n, min((num_row+1)*n, len(prefix))):
                if prefix[i] == True:
                    continue
                if get_element_by_row_column(prefix, n, num_col, i%n) == True:
                    return False
            for i in range(num_col, len(prefix), n):
                if prefix[i] == True:
                    continue
                if get_element_by_row_column(prefix, n, i//n, num_row) == True:
                    return False

    return True


def get_element_by_row_column(matrix: List[bool], n: int, num_row: int, num_col: int) -> bool:
    """
    Get element in specified row and column of square (n by n) matrix.

    Matrix can be incomplete. If trying to get an element that doesn't exist, return None.

    matrix - a list of booleans that represent an incomplete bolean matrix.
    n - length of matrix.
    num_row - row-index of the element. (indexing starts with 0)
    num_col - column-index of the element. (indexing starts with 0)

    >>> get_element_by_row_column([True, False, False, False], 2, 0, 0)
    True
    >>> get_element_by_row_column([False, False], 3, 2, 1) \
    == None
    True
    >>> get_element_by_row_column([True, True, True, True, True, False, True], 3, 1, 2)
    False
    >>> get_element_by_row_column([False], 1, 0, 0)
    False
    """

    try:
        index = n * num_row + num_col
        return matrix[index]
    except IndexError:
        return None
