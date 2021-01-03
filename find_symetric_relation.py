import write_file
import read_file


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


print(write_file.write_matrix(find_symmetric_relation(read_file.read_matrix_file("rel_1500_0.1.csv"))))