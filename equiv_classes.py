def matrix_to_relations(matrix):
    """
    Reads a boolean matrix and receives it as a list of tuples of relations
    :param matrix: list of lists
    :return: list of tuples

    >>> matrix_to_relations([[1, 1, 0, 0],\
                    [1, 1, 0, 0],\
                    [0, 0, 1, 1],\
                    [0, 0, 1, 1]])
    [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)]
    """
    relations = []
    for row_id, row in enumerate(matrix):
        for col_id, column in enumerate(row):
            if column == 1:
                relations.append((row_id, col_id))
    return relations

def find_equiv_classes(relations):
    """
    Finds equivalency classes for given equivalent relation.
    Returns a list of lists, each list represents an equivalency class.
    :param relations: list of tuples
    :return: list of lists

    >>> find_equiv_classes([(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), \
    (3, 2), (3, 3)])
    [[0, 1], [2, 3]]
    """
    classes_list = [{}]
    for relation in relations:
        for class_list in classes_list:
            if relation[0] in class_list:
                class_list.add(relation[1])
            elif relation[1] in class_list:
                class_list.add(relation[0])
            elif class_list == classes_list[-1]:
                classes_list.append({relation[0], relation[1]})
    equiv_class = [list(equiv) for equiv in classes_list]
    return equiv_class[1:]
