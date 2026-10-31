class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, point):
        INF = float('inf')

        dist = [INF] * self.size
        parent = [None] * self.size
        dist[point] = 0

        for i in range(self.size - 1):
            upd = False
            for u, v, w in self.edges:
                if dist[u] == INF:
                    continue
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u
                    upd = True
            if not upd:
                break

        neg = False
        for u, v, w in self.edges:
            if dist[u] == INF:
                continue
            if dist[u] + w < dist[v]:
                neg = True
                break

        return dist, parent, neg

    def neg_cycle_nums(self, point):
        INF = float('inf')
        dist, parent, neg = self.bellman_ford(point)
        if not neg:
            return None

        node = None
        for u, v, w in self.edges:
            if dist[u] == INF:
                continue
            if dist[u] + w < dist[v]:
                node = v
                break

        for i in range(self.size):
            node = parent[node]

        cycle = []
        start = node
        while True:
            cycle.append(node)
            node = parent[node]
            if node == start:
                break
        cycle.append(start)
        cycle.reverse()
        return cycle

    def way(self, parent, point, target):
        if parent[target] is None and target != point:
            return []
        way = []
        node = target
        while node is not None:
            way.append(node)
            if node == point:
                break
            node = parent[node]
        way.reverse()
        return way

'''
g = Graph(4)
g.add_edge(0, 1, 4)
g.add_edge(0, 3, 5)
g.add_edge(1, 2, -3)
g.add_edge(3, 2, 2)

dist, parent, neg = g.bellman_ford(0)
print("Расстояния от 0:", dist)
print("Отрицательный цикл:", neg)
print("Путь 0 -> 2:", g.way(parent, 0, 2))
'''
g2 = Graph(4)
g2.add_edge(0, 1, 1)
g2.add_edge(1, 2, -1)
g2.add_edge(2, 1, -1)
g2.add_edge(0, 3, 5)
g2.add_edge(3, 2, 2)
print("g2.edges:", g2.edges)
dist2, parent2, neg2 = g2.bellman_ford(0)
print("Расстояния:", dist2)
print("Отрицательный цикл:", neg2)
print("Вершины цикла:", g2.neg_cycle_nums(0))
