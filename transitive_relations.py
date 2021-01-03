""" The module that checks transitivity of the relation """

from copy import deepcopy

def warshall_alg(rel: list) -> list:
    """
    Worshall algorithm implementation.

    >>> warshall_alg([[0, 0, 0], [0, 0, 0]])
    [[0, 0, 0], [0, 0, 0]]

    >>> rel = [[0, 1, 0], [0, 1, 1], [0, 0, 0]]
    >>> warshall_alg(rel)
    [[0, 1, 1], [0, 1, 1], [0, 0, 0]]

    """
    for j in range(len(rel)):
        for i in range(len(rel)):
            if rel[i][j] == 1:
                rel[i] = compare(rel[i], rel[j])

    return rel


def compare(lst1: list, lst2: list) -> list:
    """
    Compares list's items to each other using OR operator.
    Saves the results of compairson to a new list and returns it.
    
    >>> compare([0, 0, 0], [1, 0, 1])
    [1, 0, 1]
    >>> compare([0, 0, 0], [1, 1, 1])
    [1, 1, 1]

    """
    compared = []
    for i in range(len(lst1)):
        compared.append(lst1[i] or lst2[i])

    return compared


def write_matrix_to_file(rel: list) -> None:
    """
    Recieves the matrix, passes it to warshall_alg func
    to get trasitive relation, then writes transitive relation
    to a .csv file as a matrix.

    >>> write_matrix_to_file([[0, 1, 0], [0, 1, 1], [0, 0, 0]])


    """
    rel = warshall_alg(rel)
    with open('transitive_matrix.csv', 'a', encoding='utf-8') as empt_fl:
        for i in range(len(rel)):
            line = ''
            for j in range(len(rel[i])):
                line += str(rel[i][j])
            line = ','.join(line)
            empt_fl.write(line)
            empt_fl.write('\n')

        empt_fl.write('\n')  # for empt line between the matrixes
    
    return None


def write_rel_to_file(rel: list) -> None:
    """
    Recieves the matrix, passes it to warshall_alg func
    to get transitive relation, then formats matrix into a
    relation and writes it to a file.
    
    >>> write_rel_to_file([[0, 1, 0], [0, 1, 1], [0, 0, 0]])


    """
    rel = warshall_alg(rel)
    with open('transitive_relation.txt', 'a', encoding='utf-8') as empt_fl:
        for i in range(len(rel)):
            for j in range(len(rel)):
                if rel[i][j] == 1:
                    rel_part = (i, j)
                    empt_fl.write(str(rel_part))
        empt_fl.write('\n')  # to start each relation in new line

    return None


def check_transition(rel: list) -> bool:
    """
    Recieves a relation and checks if it is a transitive one.
    If the relation is transitive returns True, in the other case returns False.
    
    >>> rel = [[1, 0, 0],\
               [0, 1, 0],\
               [0, 0 ,1]]
    >>> check_transition(rel)
    True

    >>> rel2 = [[0, 1, 0],\
                [0, 1, 1],\
                [0, 0, 0]]
    >>> check_transition(rel2)
    False

    """
    transit = warshall_alg(deepcopy(rel))
    if transit == rel:
        return True

    return False
