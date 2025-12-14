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

# arguments it takes is graph, vertex, visited.
def dfs_recursive(graph, vertex, visited):
  # we add visited and print
  visited.add(vertex)
  print(vertex, end=' ')
  # then we traverse through the neighbours and call 
  # the dfs function on the first neighbour that is
  # not in visited. 
  # the function then backtracks and recursively call
  # those nodes that are not printed.
  for neighbour in graph[vertex]:
    if neigbour not in visited:
      dfs_recursive(graph, neighbour, visited)

# calling the function. We use set for visited
# contains unique elements.
dfs_recursive(adj_list, 'A', set())
