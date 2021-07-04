from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].extend(v)

    @staticmethod
    def check(value):
        return True if 'm' in value else False

    def bfs(self, start):
        searched = []
        search_queue = deque()
        search_queue += self.graph[start]
        while search_queue:
            current = search_queue.popleft()
            if current not in searched:
                if self.check(current):
                    print(current)
                    return current
                searched.append(current)
                search_queue.extend(self.graph[current])
        return False


g = Graph()
g.add_edge("zane", ["alice", "bob", "claire"])
g.add_edge("bob", ["anju", "peggy"])
g.add_edge("alice", ["peggy"])
g.add_edge("claire", ["thom", "jonny"])
g.add_edge("anju", [])
g.add_edge("peggy", [])
g.add_edge("thom", [])
g.add_edge("jonny", [])
g.bfs('zane')
