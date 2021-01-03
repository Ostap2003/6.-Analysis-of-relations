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


print(read_matrix_file("rel_50_0.01.csv"))