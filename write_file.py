def write_matrix(matrix: list):
    """
    Write matrix into csv-file.
    """
    file = open("matrix1.csv", "w")
    for line in matrix:
        file.write(str(line).replace(", ", " ")[1:][:-1])
        file.write("\n")
    file.close()


def write_relation(matrix: list):
    """
    Write relation into txt-file.
    """
    file = open("matrix2.csv", "w")

    for row_id in range(len(matrix)):
        for column_id in range(len(matrix)):
            if matrix[row_id][column_id] == 1:
                pair = (row_id, column_id)
                file.write(str(pair) + ", ")

    file.close()
