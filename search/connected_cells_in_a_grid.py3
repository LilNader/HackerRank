class Node():
    def __init__(self, id):
        self.id = id
        self.explored = False
        self.neighbors = set()
        

class Graph():
    def __init__(self, size, marked_nodes):
        self.nodes = [Node(x) for x in range(size)]
        self.marked_nodes = list(filter(lambda x: x.id in marked_nodes, self.nodes))
        
    def connect_vertices(self, u, v):
        self.nodes[u].neighbors.add(self.nodes[v])
        self.nodes[v].neighbors.add(self.nodes[u])

    def dfs(self, u):
        if u.explored:
            return 0

        u.explored = True
        nodes_explored = 1
        stack = [u]
        while len(stack) > 0:
            current_node = stack.pop()
            for neighbor in current_node.neighbors:
                if not neighbor.explored:
                    neighbor.explored = True
                    nodes_explored += 1
                    stack.append(neighbor)

        return nodes_explored

    def size_max_connected_component(self):
        r = -1
        for u in self.marked_nodes:
            connected_component_size = self.dfs(u)
            if connected_component_size > r:
                r = connected_component_size
        return r

def solution(matrix, n, m, marked_nodes):
    graph = Graph(n*m, marked_nodes)
    # Constructing an undirected graph by checking the cells that are below
    # and on the righ on the current cell. 
    c = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if j+1 < m and matrix[i][j+1] == 1:
                    graph.connect_vertices(c, c+1)
                if i+1 < n and matrix[i+1][j] == 1:
                    graph.connect_vertices(c, c+m)
            c += 1
    # I didn't have any other good idea to traverse the matrix diagonally.
    c = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                if i+1 < n and j+1 < m and matrix[i+1][j+1] == 1:
                    graph.connect_vertices(c, c+m+1)
                if i+1 < n and j-1 >=0 and matrix[i+1][j-1] == 1:
                    graph.connect_vertices(c, c+m-1)
            c += 1

    return graph.size_max_connected_component()


n = int(input())
m = int(input())
matrix = []
marked_nodes = set()
c = 0
for i in range(n):
    lj = [int(x) for x in input().split()]
    for j in range(len(lj)):
        if lj[j] == 1:
            marked_nodes.add(c)
        c += 1
    matrix.append(lj)

print(solution(matrix, n, m, marked_nodes))