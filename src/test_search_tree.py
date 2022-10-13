# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_


from elv import construct_tree
from elv import subtree_labels
from elv import match

def test_subtree_labels():
    '''Test if we can get all the leafs from a node'''

    results = []
    T = construct_tree('abab')
    for branch in T:
        L = subtree_labels(branch)
        results.append(sorted(L))
    print(L)
    expectations = [[0,1,2,3,4],[0],[1],[2],[3],[4],[0,2],[1,3]]
    assert(sorted(results)==sorted(expectations))


    results = []
    T = construct_tree('abcd')
    for branch in T:
        L = subtree_labels(branch)
        results.append(sorted(L))
    print(L)
    expectations = [[0,1,2,3,4],[0],[1],[2],[3],[4]]
    assert(sorted(results)==sorted(expectations))


    results = []
    T = construct_tree('aaaa')
    for branch in T:
        L = subtree_labels(branch)
        results.append(sorted(L))
    print(L)
    expectations = [[0,1,2,3,4],[0],[1],[2],[3],[4],[0,1,2,3],[0,1,2],[0,1]]
    assert(sorted(results)==sorted(expectations))

    results = []
    T = construct_tree('acgtgacg')
    node = T[0].children['a']
    L = subtree_labels(node)
    results.append(sorted(L))
    print(L)
    expectations = [[0,5]]
    assert(sorted(results)==sorted(expectations))

def test_search_tree_simple():
    '''Test the search_tree function with simple strings and patterns'''

    string = 'abcdeabcdeabced'
    pattern = 'ab'
    expectations = [0,5,10]
    results = match(pattern, string)
    assert(sorted(results)==sorted(expectations))

    pattern = 'cde'
    expectations = [2,7]
    results = match(pattern, string)
    assert(sorted(results)==sorted(expectations))

    pattern = ''
    expectations = []
    results = match(pattern, string)
    assert(sorted(results)==sorted(expectations))

