# Abdul Munim Zahid
import collections
import networkx as nx


def bfs(self, root):
    seen, queue = set([root]), collections.deque([root])
    visited = []
    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        for node in self[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    return visited


def BFS_graph_connected_components(self):
    connectedGraph=[]
    for vertex in self.nodes():
        setToAdd = set(bfs(self,vertex))
        if setToAdd not in connectedGraph:
            connectedGraph.append(set(bfs(self,vertex)))
    return connectedGraph
