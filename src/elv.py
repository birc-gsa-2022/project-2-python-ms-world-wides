# To do:

# test for matching
# Be able to have both partial and complete matches
# make sure match works

# class for nodes
from re import L


class Node():
    def __init__(self, indexlist, parent, children):
        self.indexlist = indexlist
        self.parent = parent
        self.children = children

    def reproduction(self, child_node, first_letter):
        self.children[first_letter] = child_node
        child_node.parent = self
    
    def update_index(self, index_pos, new_index):
        self.indexlist[index_pos] = new_index
        
    # if node is leaf int represents start position of suffix in x
    def is_leaf(self):
        return type(self.children) == int

    def exists_child(self, letter):
        return letter in self.children
    
    def get_child(self, letter):
        return self.children[letter]
    
    def __str__(self):
        if self.is_leaf():
            return f'I am leaf {self.children} with edge {self.indexlist}'
        else:
            return f'I am inner node between {self.indexlist}'

def construct_tree(x):
    '''Function construct_tree(x) that takes a string x and constructs a suffix tree 
    using the class Node.'''

    root = Node(None, None, {})
    T = [root]

    x += '$'

    for i in range(len(x)): # loop through all suffixes
        node, match_l_edge, match_l_suf = search_tree(x, T, i)
        if match_l_edge == 0: # no match in node, extend from it
            T = extend_from_node(node, i, match_l_suf, x, T) # i_match 
        else: # match within part of edge, extend within edge
            T = extend_from_edge(node, i, match_l_suf, x, T, match_l_edge) 

        # print(get_tree_indexes(T))

    return T

#Function searches for string x in Suffix tree T
def search_tree(x, T, i):

    def search_node(x, node, i, match_length_suf): # if i == int, then suffix. if i == str, then pattern

        letter = x[i]
        # Check if a child starting with the required letter exists
        if not node.is_leaf() and node.exists_child(letter):
            w = node.get_child(letter)
            index = w.indexlist
            edge_l = index[1]-index[0]
            lx = len(x)
            substr_len = lx-i-1


            # Match through edge
            for match_l_edge in range(1,edge_l): # just edge or edge+1?
                same = x[index[0]+match_l_edge] == x[i+match_l_edge]

                # matched until end of string, not end of edge
                if same and match_l_edge == substr_len: # and substr_len < edge_l: #do we need this?
                    return w, match_l_edge, match_length_suf+match_l_edge
                elif not same:
                    return w, match_l_edge, match_length_suf+match_l_edge

            # search the next node, update how far we have matched so far
            return search_node(x, w, i+edge_l, match_length_suf+edge_l)

        else:
            return node, 0, match_length_suf #i-1
    
    root = T[0]
    return search_node(x, root, i, 0)

def extend_from_node(node, i, match_l_suf, x, T):
    # parent is node
    # create leaf node with string[i:]

    lx = len(x)
    index_list = [match_l_suf+i, lx]
    new_node = Node(index_list, None, i)
    T.append(new_node)

    node.reproduction(new_node, x[index_list[0]]) # x[i]

    return T

def extend_from_edge(node, i, match_l_suf, x, T, match_l):

    # create new node w = node[:match_l] with parent of 'node' as parent, string and node as children
    # update parent child from node to w
    # update node indexlist to [match_l:], change parent to w

    previous_indexes = node.indexlist
    x_mismatch_letter = x[previous_indexes[0]+match_l]

    # create the intermediate node
    w_index_list = [previous_indexes[0], previous_indexes[0]+match_l]       
    w = Node(w_index_list, None, {}) #node.parent doesnt exist 

    # make the parent of node the parent of w, and w its child
    node.parent.reproduction(w, x[previous_indexes[0]])
    T.append(w)

    # create the new node

    lx = len(x)
    new_index_list = [i+match_l_suf, lx] #[match_l_suf+i, lx] # how long we matched the suffix w edge +1
    new_node = Node(new_index_list, None, i) # index list, parent, label because leaf
    T.append(new_node)

    # change node index
    node.update_index(0, previous_indexes[0]+match_l)

    # add w children
    w.reproduction(new_node, x[new_index_list[0]]) # string[match_l]
    w.reproduction(node, x_mismatch_letter)

    return T

def match(p, x, T = None):

    def match_node(p, i, x, node, match_length_p): 

        if len(p) == 0:
            return node, i, match_length_p

        letter = p[i]
        # Check if a child starting with the required letter exists
        if not node.is_leaf() and node.exists_child(letter):
            w = node.get_child(letter)
            print(w)
            index = w.indexlist
            edge_l = index[1]-index[0]
            p_len = len(p)-i


            # Match through edge
            for match_l_edge in range(1,edge_l): # just edge or edge+1?

                same = x[index[0]+match_l_edge] == p[i+match_l_edge]
                
                if len(p) == i+match_l_edge+1: # reached end
                    return w
                # matched until end of string, not end of edge
                if same and match_l_edge == p_len: # and substr_len < edge_l: #do we need this?
                    return w
                elif not same:
                    return None

            # search the next node, update how far we have matched so far
            return match_node(p, i+edge_l, x, w, match_length_p+edge_l)

        else:
            return node, 0, match_length_p


    if T is None:
        T = construct_tree(x)

    root = T[0]
    m_node = match_node(p, 0, x, root, 0)
    print(m_node)

    leaf_list = []
    
    if m_node == None:
        print('No match')
        return leaf_list 
    
    get_leafs(m_node, leaf_list)

    leaf_list_2 = subtree_labels(m_node)
    
    for el in leaf_list:
        print(el)
    for el in leaf_list_2:
        print(el)
            
    return leaf_list

def subtree_labels(current_n):
        if current_n.is_leaf():
            yield current_n.children
        else:
            yield from [subtree_labels(v) for (k, v) in current_n.children.iteritems()]

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

def main():
    # b = 'acgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgt'
    b = 'agcttacg'
    T = construct_tree(b)
    p = 'ac'

    print(match(p, b, T))


if __name__ == '__main__':
    main()