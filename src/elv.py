# To do:

# for matching we only need node?
# Parse through subtree when end of pattern match reached
# Retrieve index from leaves
# Be able to have both partial and complete matches

# class for nodes
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

    return T

#Function searches for string x in Suffix tree T
def search_tree(x, T, i):

    # need node, p, x and an iterator i through p for pattern matching
    # need node, x and iterator i through suffix for suffix matching

    def search_node(x, node, i): # if i == int, then suffix. if i == str, then pattern
        # if type(i) == int:
            # matching suffix
        # elif type(i) == str:
            # matching pattern

        letter = x[i] # 

        # Check if a child starting with the required letter exists
        if not node.is_leaf() and node.exists_child(letter):
            w = node.get_child(letter)
            index = w.indexlist
            edge_l = index[1]-index[0]
            lx = len(x)
            substr_len = lx-i-1

            # Match through edge
            for match_l_edge in range(1,edge_l):
                match_l_suf = i+match_l_edge # index of current match in x
                same = x[index[0]+match_l_edge] == x[match_l_suf]

                # matched until end of string, not end of edge
                if same and match_l_edge == substr_len and substr_len != edge_l:
                    return w, match_l_edge, match_l_suf
                elif same: # match
                    continue
                else:
                    return w, match_l_edge, match_l_suf-1

            return search_node(x, w, i+edge_l)

        else:
            return node, 0, i-1 
    
    root = T[0]
    return search_node(x, root, i)

def match_tree(x, T, i):

    # need node, p, x and an iterator i through p for pattern matching
    # need node, x and iterator i through suffix for suffix matching

    def match_node(x, node, i): # if i == int, then suffix. if i == str, then pattern
        # if type(i) == int:
            # matching suffix
        # elif type(i) == str:
            # matching pattern

        letter = x[i] # 

        # Check if a child starting with the required letter exists
        if not node.is_leaf() and node.exists_child(letter):
            w = node.get_child(letter)
            index = w.indexlist
            edge_l = index[1]-index[0]
            lx = len(x)
            substr_len = lx-i

            # Match through edge
            for match_l_edge in range(1,edge_l):
                match_l_suf = i+match_l_edge # index of current match in x
                same = x[index[0]+match_l_edge] == x[match_l_suf]

                # matched until end of string, not end of edge
                if same and match_l_edge == substr_len and substr_len != edge_l:
                    return w, match_l_edge, match_l_suf
                elif same: # match
                    continue
                else:
                    return w, match_l_edge, match_l_suf-1
            
            return match_node(x, w, i+edge_l)

        else:
            return node, 0, i-1 
    
    root = T[0]
    return match_node(x, root, i)

def extend_from_node(node, i, match_l_suf, x, T):
    # parent is node
    # create leaf node with string[i:]
    
    lx = len(x)
    index_list = [match_l_suf+1, lx]
    new_node = Node(index_list, None, i)
    T.append(new_node)
    # print(node.children)
    # print(x[i:match_l_suf])
    # print(f'x[i]: {x[i]}')
    # print(node)
    node.reproduction(new_node, x[i]) # x[i]=string[0]

    return T

def extend_from_edge(node, i, match_l_suf, x, T, match_l):

    # create new node w = node[:match_l] with parent of 'node' as parent, string and node as children
    # update parent child from node to w
    # update node indexlist to [match_l:], change parent to w

    previous_indexes = node.indexlist
    # x_last_match_letter = x[previous_indexes[0]+match_l-1]
    x_mismatch_letter = x[previous_indexes[0]+match_l]

    # create the intermediate node
    w_index_list = [previous_indexes[0], previous_indexes[0]+match_l]       
    w = Node(w_index_list, None, {}) #node.parent doesnt exist 

    # make the parent of node the parent of w, and w its child
    node.parent.reproduction(w, x[previous_indexes[0]])
    T.append(w)

    # create the new node

    lx = len(x)
    #j = index of first mismatch in string
    new_index_list = [match_l_suf+1, lx]
    new_node = Node(new_index_list, None, i) # index list, parent, label because leaf
    T.append(new_node)

    # change node index
    node.update_index(0, previous_indexes[0]+match_l)

    # add w children
    w.reproduction(new_node, x[i+match_l]) # string[match_l]
    w.reproduction(node, x_mismatch_letter)

    return T

def match(p, x, T = None):

    # should not work with empty pattern

    if T is None:
        T = construct_tree(x)

    # node, match_l_edge, match_l_p = search_tree(p, T, 0)

    # match_labels = subtree_labels(node)

    # if match_l_p != len(p):
    #     print("Partial match of p until index match_l_p")
    #     print("Indexes with matching prefix in x:")
    # else:
    #     print("Complete match of p at the following indexes in x:")
    # print(match_labels)

def subtree_labels(current_n):
        if current_n.is_leaf():
            yield current_n.children
        else:
            yield from [subtree_labels(v) for (k, v) in current_n.children.iteritems()]

def main():
    # b = 'acgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgtacgtaaaaaacgt'
    # b = 'acgtaaacgtaaacgtaaacgtaaacgtaaacgtaa'
    b = 'acgtaaacgtaaacgtaaacgtaaacgtaa'
    # b = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    # b = 'agcgtgatcgatagctagctagctagcggggatacgctg'
    # b = 'abcdefghijklmnopqrstuvwxyzaaaaaaaaaaabbbbbbbbaaaaa'
    # print(b[:21])
    T = construct_tree(b) #abca
    # match('aaba', 'aabaababb')

if __name__ == '__main__':
    main()