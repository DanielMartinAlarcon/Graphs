from ancestors import ancestors

lineage =   [(1, 3),
            (2, 3),
            (3, 6),
            (5, 6),
            (5, 7),
            (4, 5),
            (4, 8),
            (8, 9),
            (11, 8),
            (10, 1),
            (12,13),
            (13,2),
            (14,13)]


def test_single_ascestor():
    assert ancestors(7, lineage) == [4]

def test_multiple_ancestors():
    assert ancestors(6, lineage) == [12,14]

def test_intermediate_node():
    assert ancestors(5, lineage) == [4]

def test_no_parents():
    assert ancestors(11, lineage) == -1
    assert ancestors(10, lineage) == -1