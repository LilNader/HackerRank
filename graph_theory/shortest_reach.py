class Node():
    def __init__(self, id):
        self.id = id
        self.neighbors = set()      

class Graph():
    def __init__(self, nodes):
        self.nodes = [Node(x) for x in range(nodes)]
        
    def add_edge(self, u, v):
        self.nodes[u].neighbors.add(self.nodes[v])
        self.nodes[v].neighbors.add(self.nodes[u])

    def distance_from_start(self, s):
        distances = [-1 for _ in range(len(self.nodes))]
        distances[s] = 0
        queue = [self.nodes[s]]
        # DFS
        while len(queue) != 0:
            current_node = queue.pop(0)
            # Traverse its neighbors
            for neighbor in current_node.neighbors:
                # Node not explored
                if distances[neighbor.id] == -1:
                    distances[neighbor.id] = 6 + distances[current_node.id]
                    queue.append(neighbor)

        return ' '.join([str(x) for x in filter(lambda x: x != 0, distances)])


q = int(input())
for _ in range(q):
    g_n, g_e = [int(x) for x in input().split()]
    graph = Graph(g_n)

    for _ in range(g_e):
        u, v = [int(x) for x in input().split()]
        graph.add_edge(u-1, v-1)

    s_n = int(input())
    print(graph.distance_from_start(s_n-1))
