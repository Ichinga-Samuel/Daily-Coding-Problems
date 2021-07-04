from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].extend(v)

    def dfs_util(self, visited, v):
        nodes = self.graph[v]
        for node in nodes:
            if node not in visited:
                self.dfs_util(visited, node)

    def dfs(self):
        visited = set()
        nodes = self.graph.keys()
        for node in nodes:
            if node not in visited:
                self.dfs_util(visited, node)
