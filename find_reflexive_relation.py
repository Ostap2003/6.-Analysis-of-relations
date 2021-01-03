def find_reflexive_relation(matrix):
    """
    Return a matrix of reflexive closure of the relation.
    >>> find_reflexive_relation([[1, 1, 1], [0, 0, 0], [1, 0, 0]])
    [[1, 1, 1], [0, 1, 0], [1, 0, 1]]
    """
    for index in range(len(matrix)):
        if matrix[index][index] != 1:
            matrix[index][index] = 1  # replace 0 to 1 for each element in diagonal of matrix
    return matrix
