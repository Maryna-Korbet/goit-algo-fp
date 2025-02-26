import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        # Graph initialization
        self.graph = {}

    # Add a rib
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))

    # Dijkstra algorithm for finding shortest paths
    def dijkstra(self, start):
        # Initialization of structures
        heap = [(0, start)] 
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        paths = {}

        while heap:
            current_distance, node = heapq.heappop(heap)

            # Skip already processed vertices
            if current_distance > distances[node]:
                continue

            for neighbor, weight in self.graph[node]:
                distance = current_distance + weight

                # If a shorter distance is found, we update it
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = node
                    heapq.heappush(heap, (distance, neighbor))

        return distances, paths

    # Return the shortest path from start to target
    def get_shortest_path(self, start, target, paths):
        path = []
        current = target
        while current != start:
            path.append(current)
            current = paths.get(current)
        path.append(start)
        return path[::-1]

    # Visualize the graph using networkx and matplotlib
    def visualize(self, paths, start):
        # Create a NetworkX graph
        G = nx.Graph()

        # Add vertices and edges
        for u in self.graph:
            for v, w in self.graph[u]:
                G.add_edge(u, v, weight=w)

        # Set the layout
        pos = nx.spring_layout(G)  

        # Set node colors
        node_colors = {node: "skyblue" for node in G.nodes}
        node_colors[start] = "limegreen" 

        shortest_path_nodes = set(paths.values())
        for node in shortest_path_nodes:
            # Shortest path nodes are red
            node_colors[node] = "red" 

        # Vizualization of edges colors
        edge_colors = []
        for u, v in G.edges:
            if (u, v) in paths.items() or (v, u) in paths.items():
                edge_colors.append("red") 
            else:
                edge_colors.append("black")  

        # Draw graph
        nx.draw(
            G, pos, with_labels=True, node_size=800,
            node_color=[node_colors[n] for n in G.nodes],
            font_size=14, width=2, edge_color=edge_colors, font_weight="bold", node_shape='o'  # Змінив форму на коло
        )

        # Add edge labels
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}
        )

        plt.show()

# Create a graph
graph = Graph()
edges = [('A', 'B', 3), ('A', 'C', 2), ('B', 'D', 6), ('C', 'D', 5), ('D', 'E', 4)]
for u, v, w in edges:
    graph.add_edge(u, v, w)

# Run Dijkstra's algorithm
start = 'A'
distances, paths = graph.dijkstra(start)
print(f"Shortest distances from {start}: {distances}")

# Print shortest paths from start to other vertices
for target in distances:
    if target != start:
        path = graph.get_shortest_path(start, target, paths)
        print(f"The shortest path from {start} to {target}: {path} with distance {distances[target]}")

# Visualize the graph
graph.visualize(paths, start)
