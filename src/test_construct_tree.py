# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_


from elv import construct_tree

def get_tree_indexes(T):
    '''Return a list of all the nodes' indexes of the tree
    Excludes the root'''

    l=[]
    for node in T:
        if node.indexlist!=None:
            l.append(node.indexlist)
    return l

def test_extends_from_node():
    '''Test the construction of trees only by creating new nodes from nodes'''
    T = construct_tree('abcde')
    results = get_tree_indexes(T)
    print(results)
    expectations = [[0,6],[1,6],[2,6],[3,6],[4,6],[5,6]]
    assert(sorted(results)==sorted(expectations))


def test_extends_from_edge():
    '''Test the construction of trees only by creating new nodes from edges'''
    T = construct_tree('aaaaa')
    results = get_tree_indexes(T)
    print(results)
    expectations = [[4,6],[5,6],[5,6],[5,6],[5,6],[5,6],[0,1],[1,2],[2,3],[3,4]]
    assert(sorted(results)==sorted(expectations))

def test_construct_tree():
    '''Test the construction of various trees'''

    T = construct_tree('abab')
    results = get_tree_indexes(T)
    print(results)
    expectations = [[2,5],[2,5],[4,5],[4,5],[4,5],[0,2],[1,2]]
    assert(sorted(results)==sorted(expectations))

    T = construct_tree('abbab')
    results = get_tree_indexes(T)
    print(results)
    expectations = [[2,6],[2,6],[3,6],[5,6],[5,6],[5,6],[0,2],[1,2]]
    assert(sorted(results)==sorted(expectations))

    T = construct_tree('abca')
    results = get_tree_indexes(T)
    print(results)
    expectations = [[1,5],[1,5],[2,5],[4,5],[4,5],[0,1]]
    assert(sorted(results)==sorted(expectations))

    T = construct_tree('abbabab')
    results = get_tree_indexes(T)
    print(results)
    expectations = [[2,8],[2,8],[5,8],[5,8],[7,8],[7,8],[7,8],[7,8],[0,2],[1,2],[3,5]]
    assert(sorted(results)==sorted(expectations))


