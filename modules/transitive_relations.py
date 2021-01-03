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
