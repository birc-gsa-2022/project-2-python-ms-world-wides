# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_


from elv import construct_tree

def get_leafs(node,L):
    
    if node.is_leaf():
        L.append(node.children)
    
    else: 
        for letter in node.children:
            child = node.get_child(letter)
            if child.is_leaf():
                L.append(child.children)
            else:
                get_leafs(child,L)

def test_get_leafs():
    '''Test if we can get all the leafs from a node'''

    results = []
    T = construct_tree('abab')
    for branch in T:
        L = []
        get_leafs(branch, L)
        results.append(sorted(L))
    print(L)
    expectations = [[0,1,2,3,4],[0],[1],[2],[3],[4],[0,2],[1,3]]
    assert(sorted(results)==sorted(expectations))


    results = []
    T = construct_tree('abcd')
    for branch in T:
        L = []
        get_leafs(branch, L)
        results.append(sorted(L))
    print(L)
    expectations = [[0,1,2,3,4],[0],[1],[2],[3],[4]]
    assert(sorted(results)==sorted(expectations))


    results = []
    T = construct_tree('aaaa')
    for branch in T:
        L = []
        get_leafs(branch, L)
        results.append(sorted(L))
    print(L)
    expectations = [[0,1,2,3,4],[0],[1],[2],[3],[4],[0,1,2,3],[0,1,2],[0,1]]
    assert(sorted(results)==sorted(expectations))

# def test_search_tree_simple():
#     '''Test the search_tree function with simple strings and patterns'''

#     string = 'abcdeabcdeabced'
#     pattern = 'ab'
#     expectations = [0,5,10]
#     results = search_pattern(pattern, string)
#     assert(sorted(results)==sorted(expectations))

#     pattern = 'cde'
#     expectations = [2,7]
#     results = search_pattern(pattern, string)
#     assert(sorted(results)==sorted(expectations))

#     pattern = ''
#     expectations = []
#     results = search_pattern(pattern, string)
#     assert(sorted(results)==sorted(expectations))

