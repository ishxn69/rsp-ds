adj_list = {
    "A" : ["B", "D"],
    "B" : ["A", "C"],
    "C" : ["B"],
    "D" : ["A", "E", "F"],
    "E" : ["D", "F", "G"],
    "F" : ["D", "E", "H"],
    "G" : ["E", "H"],
    "H" : ["G", "F"]
}

# --------------------------------
# PRINT BREADTH FIRST SEARCH ORDER
from queue import Queue

visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    # we pop the current element
    u = queue.get()
    bfs_traversal_output.append(u)

    # for all adjacent vertices of curr
    for v in adj_list[u]:
        # check to ensure adj vertex is not visited
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)
print(bfs_traversal_output)

# --------------------------
# SHORTEST DISTANCE EXAMPLES
# shortest distance of all nodes from source nodes
print(level)
# to print shortest distance of node G from source node:
print(level["G"]) # output should return 3 {A -> D -> E -> G}

# -----------------------------------------
# SHORTEST PATH OF ANY NODE FROM SOURCE NODE
v = "G"
path = []
# Do this till v is None (parent of A)
while v is not None: 
  path.append(v) # add v to path
  v = parent[v] # change v to parent of v. 
path.reverse() # from 'G -> A' to 'A -> G'
print(path)
