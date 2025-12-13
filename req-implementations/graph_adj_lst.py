class Graph:
    '''
    Functions we use:
    1. init(Nodes array, is_directed variable), is_directed is False by default
    2. add_edges(u,v)
    3. degree(node)
    4. print_adj_list()
    '''
    # we can use the same code for directed graphs and undirected graphs
    # by setting the is_directed variable false or true.
    def __init__(self, Nodes, is_directed = False):
        self.nodes = Nodes
        self.adj_list = {}
        self.is_directed = is_directed

        # we then add an empty edges list to all nodes.
        for node in self.nodes:
            self.adj_list[node] = []
    
    def add_edges(self, u, v):
        self.adj_list[u].append(v)

        # change made when is_directed is True/False
        # for directed graph, edge (u,v) != (v, u), so 
        # u will not be added to v's edge list, 
        # unless specified in 'edges' list.
        if self.is_directed == False:
            self.adj_list[v].append(u)

    def degree(self, u):
        deg = len(self.adj_list[u])
        return deg
    
    def print_adj_list(self):
        for node in self.nodes:
            print(node, '->', self.adj_list[node])

if __name__ == '__main__':
  # defining nodes and edges of the program
  nodes = ['A', 'B', 'C', 'D', 'E']
  edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]

  # in this case we are implementing directed graph
  my_graph = Graph(nodes, is_directed=True)
  
  for u, v in edges:
      my_graph.add_edges(u, v)
  
  my_graph.print_adj_list()
  
  my_graph.degree('A')
