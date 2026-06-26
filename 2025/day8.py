from itertools import combinations
from math import dist, prod

s = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
739,650,466
431,825,988
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size
        self.num_components = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]

        self.num_components -= 1
        return True


points = [[int(num) for num in line.split(",")] for line in s.splitlines()]
n = len(points)
edges = []

for i, j in combinations(range(n), 2):
    d = dist(points[i], points[j])
    edges.append((d, i, j))

edges.sort()
dsu = DSU(n)

for _, i, j in edges[:1000]:
    dsu.union(i, j)

print(
    prod(
        sorted((dsu.size[i] for i in range(n) if dsu.parent[i] == i), reverse=True)[:3]
    )
)

dsu2 = DSU(n)

for _, i, j in edges:
    if dsu2.union(i, j) and dsu2.num_components == 1:
        print(points[i][0] * points[j][0])
        break
