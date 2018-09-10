# Roads and Libraries
# https://www.hackerrank.com/challenges/torque-and-development/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs

class Node():
	def __init__(self, id):
		self.id = id
		self.neighboors = set()
		self.visited = False

class Graph():
	def __init__(self, n):
		self.vertices = [Node(x) for x in range(n)]

	def add_edge(self, u, v):
		self.vertices[u].neighboors.add(self.vertices[v])
		self.vertices[v].neighboors.add(self.vertices[u])

	def dfs(self, u):
		spanning_tree_len = 0
		aux = self.vertices[u]
		aux.visited = True 
		stack = [aux]
		while stack:
			x = stack.pop()
			for v in x.neighboors:
				if not v.visited:
					v.visited = True
					stack.append(v)
					spanning_tree_len += 1
		return spanning_tree_len

	def min_cost(self, c_lib, c_road):
		# Explore connected components
		spanning_tree_len = []
		for u in self.vertices:
			if not u.visited:
				spanning_tree_len.append(self.dfs(u.id))

		#print(spanning_tree_len)
		r = 0
		for x in spanning_tree_len:
			r += min((x*c_road)+c_lib, (x+1)*c_lib)

		return r

t = int(input())
for _ in range(t):
	n, m, c_lib, c_road = [int(x) for x in input().split()]
	g = Graph(n)
	for _ in range(m):
		a, b = [int(x) for x in input().split()]
		g.add_edge(a-1, b-1)
	print(g.min_cost(c_lib, c_road))
