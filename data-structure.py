# -*- coding: utf-8 -*-


# 广度优先搜索，状态压缩。
class Graph:

    def __init__(self):
        self.node_neighbors = {}
        self.visited = {}

    def nodes(self):
        return self.node_neighbors.keys()

    def add_node(self, node):
        if node not in self.nodes():
            self.node_neighbors[node] = []

    def add_nodes(self, node_list):
        for node in node_list:
            self.add_node(node)

    def add_edge(self, edge):
        u, v = edge
        if (u not in self.node_neighbors[v]) and (v not in self.node_neighbors[u]):
            self.node_neighbors[u].append(v)
            self.node_neighbors[v].append(u)

    def depth_first_search(self, root, res):
        res.append(root)
        self.visited[root] = True
        for next in self.node_neighbors[root]:
            if next not in self.visited:
                self.depth_first_search(next, res)

    def breadth_first_search(self, root):  # 成功了呀.
        queue = []
        order = []
        queue.append(root)
        while queue:
            head = queue.pop(0)
            if head not in self.visited:
                order.append(head)
                self.visited[head] = True
            for one in self.node_neighbors[head]:
                if one not in self.visited:
                    queue.append(one)
        return order


if __name__ == '__main__':
    g = Graph()
    g.add_nodes([i+1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 4))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))
    order = []
    order = g.breadth_first_search(1)
    print order



