# Creating the node of the BST
class Node:
    def __init__(self, key):
        self.value = key  
        self.left = None  
        self.right = None    

# Recursive Insert function
# Time Complexity: O(h) # O(logn) for Balanced BST
def insert(root, key):
    if root is None:
        return Node(key)
    if root.value == key:
            return root
    if root.value < key:
            root.right = insert(root.right, key)
    else:
            root.left = insert(root.left, key)
    return root
    
# Recursive Search in BST
# Same time complexity as Insert
def search(root, key):
  
    # Base Cases: root is null or key 
    # is present at root
    if root is None or root.value == key:
        return root
    
    # Key is greater than root's key
    if root.value < key:
        return search(root.right, key)
    
    # Key is smaller than root's key
    return search(root.left, key)
    
# Deletion in a BST

# Deletion Part 1: Successor Function
# As long as curr.left is not None we keep going left.
def get_successor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr
    
# Deletion Part 2: Deletion function
def del_node(root, x):
    # base case
    if root.value == None:
        return root
        
    # Firstly, search for the value
    if root.value > x:
        root.left = del_node(root.left, x)
    elif root.value < x:
        root.right = del_node(root.right, x)
    else:
        # Reaching this loop means root has matched with given value (x)
        
        # case 1 and 2: when left or right node is empty 
        if root.left is None:
            return root.right
            
        if root.right is None: 
            return root.left
        
        # case 3: when both left and right child are present
        inorder_successor = get_successor(root)
        root.value = inorder_successor.value
        root.right = del_node(root.right, inorder_successor.value)
    #ensures the changed tree is returned.
    return root
