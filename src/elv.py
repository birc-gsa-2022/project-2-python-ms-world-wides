# To do:
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
        child_node.adoption(self)

    def index(self):
        return self.indexlist
    
    def update_index(self, index_pos, new_index):
        self.indexlist[index_pos] = new_index
    
    def get_parent(self):
        return self.parent
    
    def adoption(self, new_parent):
        self.parent = new_parent
        
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
        node, head_l, match_l = search_tree(x, T, i) # ab$, T, b$
        if match_l == 0: # no match in node, extend from it
            T = extend_from_node(node, x[i:], x, head_l, T)
        else: # match within part of edge, extend within edge
            T = extend_from_edge(node, x[i:], x, head_l, T, match_l)

    for el in T:
        print(el)

#Function searchs for string x in Suffixtree T
def search_tree(x, T, i):

    def search_node(node, x, i):
        letter = x[i]
        # Check if a child starting with the required letter exists
        if not node.is_leaf() and node.exists_child(letter):
            w = node.get_child(letter)
            index = w.indexlist
            edge_l = index[1]-index[0]
            substr_len = len(x[i:])

            # Match through edge
            for match_l in range(1,edge_l):
                same = x[index[0]+match_l] == x[i+match_l]

                # matched until end of string, not end of edge
                if same and match_l == substr_len and substr_len != edge_l:
                    return w, i, match_l
                elif same: # match
                    continue
                else: # mismatch
                    return w, i, match_l
            
            # search next node
            search_node(w, x, i+edge_l)

        else:
            return node, i, 0 

    root = T[0]

    return search_node(root, x, i)

def extend_from_node(node, string, x, i, T):
    # parent is node
    # create leaf node with string[i:]
    
    l = len(string)
    index_list = [i, i+l]
    new_node = Node(index_list, None, (len(x)-len(string)))
    T.append(new_node)
    node.reproduction(new_node, string[0])

    # Added return T to update tree. Maybe instead return new elements and concatenate with T in construct_tree?
    return T

def extend_from_edge(node, string, x, head_l, T, match_l):
    # create new node w = node[:match_l] with parent of 'node' as parent, string and node as children
    # update parent child from node to w
    # update node indexlist to [match_l:], change parent to w

    previous_indexes = node.index()
    x_last_match_letter = x[previous_indexes[0]+match_l-1]
    x_mismatch_letter = x[previous_indexes[0]+match_l]

    # create the intermediate node
    w_index_list = [previous_indexes[0], previous_indexes[0]+match_l]       
    w = Node(w_index_list, node.get_parent(), {}) #node.parent doesnt exist 

    # make the parent of node the parent of w, and w its child
    node.get_parent().reproduction(w, x_last_match_letter)
    T.append(w)

    # create the new node

    l = len(x)
    new_index_list = [head_l+match_l, l]
    new_node = Node(new_index_list, None, len(x)-len(string)) # index list, parent, label because leaf
    T.append(new_node)

    # change node index
    node.update_index(0, previous_indexes[0]+match_l)

    # add w children
    w.reproduction(new_node, string[match_l])
    w.reproduction(node, x_mismatch_letter)

    return T


def main():
    construct_tree('aaaa')


if __name__ == '__main__':
    main()