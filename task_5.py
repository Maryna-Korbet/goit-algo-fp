import uuid

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def get_color_gradient(start_color, end_color, steps):
    start_rgb = mcolors.hex2color(start_color)
    end_rgb = mcolors.hex2color(end_color)
    colors = []
    for i in range(steps):
        r = start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / (steps - 1)
        g = start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / (steps - 1)
        b = start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / (steps - 1)
        colors.append(mcolors.rgb2hex((r, g, b)))
    return colors

def draw_tree(tree_root, visited_nodes):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    node_colors = [visited_nodes[node[0]] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

def dfs(root, visited_nodes, colors, index=0):
    if root is None:
        return index
    visited_nodes[root.id] = colors[index]
    index += 1
    index = dfs(root.left, visited_nodes, colors, index)
    index = dfs(root.right, visited_nodes, colors, index)
    return index

def bfs(root, visited_nodes, colors):
    queue = [root]
    index = 0
    while queue:
        current = queue.pop(0)
        if current is not None:
            visited_nodes[current.id] = colors[index]
            index += 1
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Color gradient
start_color = "#003366"  
end_color = "#FF99CC"    
colors = get_color_gradient(start_color, end_color, 10)

# BFS visualization with step-by-step color change
visited_nodes_bfs = {}
bfs(root, visited_nodes_bfs, colors)
draw_tree(root, visited_nodes_bfs)

# Color restoration for DFS visualization
for node in visited_nodes_bfs:
    visited_nodes_bfs[node] = "skyblue"

# DFS visualization with step-by-step color change
visited_nodes_dfs = {}
dfs(root, visited_nodes_dfs, colors)
draw_tree(root, visited_nodes_dfs)