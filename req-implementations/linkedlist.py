# RECURSIVE IMPLEMENTATION OF PYTHON LINKEDLIST AS DISCUSSED IN ADM

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# function to insert a new node at the end of linkedlist
def insert_end(head, data):
    if head is None:
        return Node(data)
    head.next = insert_end(head.next, data)
    return head    

# function to insert at start of linked list
def insert_start(head, data):
    if head is None:
        return Node(data)
    else:
        temp = head
        head = Node(data)
        head.next = temp
    return head

# deletion from list
def deletion(head, key):
    # store head element in temp
    temp = head
    
    # case 1: if head is key:
    if (temp is not None): # this is to avoid None.data -> attribute error
        if (temp.data == key): 
            head = temp.next
            temp = None # if None is deleted, so will it's pointer to head.
            return head
            
    # case 2: search the list for the temp value that equals key and break
    while (temp is not None): # traverse until the last node
        if temp.data == key:
            break
        # keep track of previous and change temp to next value
        prev = temp
        temp = temp.next
        
    # if temp is none (we didn't find anything in the above loop, value became None after last temp=temp.next)
    if temp is None:
        return head
    
    prev.next = temp.next
    temp = None
    
    return head

# function to recursively traverse linked list
def traverse(head):
    if head is None:
        return  'List is empty'

    print(head.data, end = ' ')

    # recursive call
    traverse(head.next)

if __name__ == "__main__":

    # Insert nodes with data 1, 2, 3, 4, 5
    head = None
    head = insert_end(head, 1)
    head = insert_end(head, 2)
    head = insert_end(head, 3)
    head = insert_end(head, 4)
    head = insert_end(head, 5)
    head = insert_start(head, 8)

    traverse(head)
    
