def read_matrix_file(file: str) -> list:
    """
    Read file with matrix and return a list of lists that represents matrix.
    """
    with open(file, "r") as file:
        temporary_matrix = []
        for line in file.readlines():
            temporary_matrix.append(line)  # add each line of file in the list

    matrix = []
    for row in temporary_matrix:
        matrix.append(row[:-1].split())  # delete /n from the end of each line

    final_matrix = []
    for row in matrix:
        final_row = []
        for num in row:
            for i in num.split(" "):
                final_row.append(int(i))
        final_matrix.append(final_row)
    return final_matrix


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
