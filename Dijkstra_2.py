import heapq

# iPair ==> Integer Pair
iPair = tuple

# This class represents a directed graph using
# adjacency list representation
class Graph:
    def __init__(self, V: int): # Constructor
        self.V = V
        self.adj = [[] for _ in range(V)]

    def addEdge(self, u: int, v: int, w: int):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))

    # Prints shortest paths from src to all other vertices
    def shortestPath(self, src: int):
        
        d = [float('inf')] * self.V
        nodes = []
        heapq.heappush( nodes, (0,src) )
        d[src] = 0


        while nodes:

            source_weight, source_ind = heapq.heappop(nodes)

            for target_ind, target_weight in self.adj[source_ind]:
                if d[source_ind] + target_weight < d[target_ind]:
                    d[target_ind] = d[source_ind] + target_weight
                    heapq.heappush(nodes, (d[target_ind],target_ind) )


        return d




# Driver's code
if __name__ == "__main__":
    # create the graph given in above figure
    V = 9
    g = Graph(V)

    # making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)

    result = g.shortestPath(0)

    print(result)
