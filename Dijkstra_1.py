import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = None

    def dijkstra(self, src):

        d = [sys.maxsize] * self.V
        arrived = [ False ] * self.V

        d[src] = 0

        for _ in range(self.V):

            # min dist
            min_ind = -1
            min_dist = sys.maxsize
            for i in range(self.V):
                if d[i] < min_dist and not arrived[i]:
                    min_ind = i
                    min_dist = d[i]
            

            arrived[min_ind] = True

            # lets updated connected values weight
            for i in range(self.V):
                if not arrived[i] and self.graph[min_ind][i] > 0 and self.graph[min_ind][i] + d[min_ind] < d[i]:
                    d[i] = self.graph[min_ind][i] + d[min_ind]


        return d

# time complexity O(n^2)
# Driver's code
if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

    res = g.dijkstra(0)
    print(res)
