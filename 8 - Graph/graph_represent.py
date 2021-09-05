"""
A Python program to demonstrate the adjacency
list representation of the graph
"""

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V


    def add_edge(self, src, dest):
        # adding the node to the source nod
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex of vertex %d\nhead"%(i), end="")
            temp = self.graph[i]
            while temp:
                print("-> %d"%(temp.vertex), end="")
                temp = temp.next
            print("\n")

if __name__ == '__main__':
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
