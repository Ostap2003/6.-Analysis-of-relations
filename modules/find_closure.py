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


def find_symmetric_relation(matrix: list) -> list:
    """
    Return a matrix of symmetric closure of the relation.
    >>> find_symmetric_relation([[0, 1, 1], [0, 0, 0], [1, 1, 1]])
    [[0, 1, 1], [1, 0, 1], [1, 1, 1]]
    """
    for row in range(len(matrix)):
        for num in range(len(matrix)):
            if matrix[row][num] == 1 and matrix[num][row] != 1:
                matrix[num][row] = 1  # if el (a, b) in matrix, add element (b, a)
            elif matrix[row][num] != 1 and matrix[num][row] == 1:
                matrix[row][num] = 1  # if el (b, a) in matrix, add element (a, b)
    return matrix
