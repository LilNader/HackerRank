# Even Tree
# https://www.hackerrank.com/challenges/even-tree/problem
#
# Technique used: Graph traversals: DFS
# Counting connected components, trees and forests.

class Node(object):
    def __init__(self, id):
        self.id = id
        self.explored = False
        self.neighbors = set()


class Graph(object):
    def __init__(self, size):
        self.nodes = [Node(x) for x in range(size)]
        self.removed_edges = 0

    def add_edge(self, u, v):
        self.nodes[u].neighbors.add(self.nodes[v])
        self.nodes[v].neighbors.add(self.nodes[u])

    def remove_edge(self, u, v):
        self.nodes[u].neighbors.remove(self.nodes[v])
        self.nodes[v].neighbors.remove(self.nodes[u])

    def connected_component(self, u):
        if self.nodes[u].explored:
            return []
        else:
            self.nodes[u].explored = True
            stack = [self.nodes[u]]
            r = []
            while stack:
                aux = stack.pop(0)
                r.append(aux)
                for x in aux.neighbors:
                    if not x.explored:
                        x.explored = True
                        stack.append(x)
            return r

    def marked_nodes_as_not_explored(self):
        for x in self.nodes:
            x.explored = False

    def prune_tree(self, u):

        if len(self.nodes[u].neighbors) > 1:
            neighbors = [x.id for x in self.nodes[u].neighbors]

            for v in neighbors:
                self.remove_edge(u, v)
                tree = self.connected_component(v)
                self.marked_nodes_as_not_explored()

                if len(tree) % 2 == 0:
                    #print('removed', u, v)
                    self.removed_edges +=1
                else:
                    self.add_edge(u, v)
        
    def trees_in_forest(self):
        for u in range(len(self.nodes)):
            self.prune_tree(u)
        return self.removed_edges


n, m = [int(x) for x in input().split()]

graph = Graph(n)
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    graph.add_edge(a-1, b-1)

print(graph.trees_in_forest())