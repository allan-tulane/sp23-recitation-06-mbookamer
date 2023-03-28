import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        # TODO
        x = p.get()
        y = p.get() #we want to find the nodes x,y with the lowest frequency 
        z = TreeNode(x, y, (x.data[0] + y.data[0], "")) #creating a new node that has a frequency that is the sum of x and y and 
        #we put it into the tree as an empty character since it is really just a 'filler' node for our calculations
        p.put(z) #inserting the new node into our tree
        
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
#recursively call get_code, appending 0 or 1 to the prefix 
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    if (node.left == None and node.right == None): #we want to clearly define our base case here which is a leaf 
        code[node.data[1]] = prefix  #create a mapping from value to prefix, update the code dict object
    else:
        get_code(node.left, prefix + "0", code) #append 0 if the node is the left child
        get_code(node.right, prefix + "1", code) #append 1 if the node is the right child
    return code
    pass

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    # TODO
    bits = bin(len(f)) #want the binary representation of our string f
    bits = bits[2:] #restrict bits to include all bits except the first 2 
    bitsNeeded = len(bits) #want to know how many bits are needed to represent each character in f 
    sum = 0
    for i in f.values(): #loop over the digits in f
        product = i * bitsNeeded #want to find the number of unique elements in our string f
        sum = product + sum #compute the sum of unique characters in f
    return sum
    pass

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # TODO
    cost = 0
    for c in f.keys(): #loop through unique characters in f
        cost = cost + (f[c] * len(C[c])) #want to know the frequency of each character and how many digits are needed to represent the specific character
    return cost
    pass

f = get_frequencies('f1.txt')
print("Fixed-length cost:  %d" % fixed_length_cost(f))
T = make_huffman_tree(f)
C = get_code(T)
print("Huffman cost:  %d" % huffman_cost(C, f))
