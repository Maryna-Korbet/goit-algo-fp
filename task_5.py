import uuid

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

# Class BinaryHeap
class BinaryHeap:
    def __init__(self, heap_type='min'):
        self.heap = []
        self.heap_type = heap_type  # 'min' or 'max'

    # Insert an element into the heap
    def insert(self, key):
        node = Node(key)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    # Heapify up a node
    def _heapify_up(self, index):
        # Check and adjust the heap when adding an element
        parent_index = (index - 1) // 2
        if parent_index >= 0:
            if (self.heap_type == 'min' and self.heap[index].val < self.heap[parent_index].val) or \
                (self.heap_type == 'max' and self.heap[index].val > self.heap[parent_index].val):
                    # If the element does not meet the conditions of the heap, we swap
                    self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                    self._heapify_up(parent_index)

    # Build the heap from a list of elements
    def build_heap(self, elements):
        for el in elements:
            self.insert(el)

    # Add edges to the graph for visualization
    def add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.id, color=node.color, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                pos[node.left.id] = (l, y - 1)
                l = self.add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                r = self.add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
        return graph

    # Draw the heap
    def draw_heap(self):
        if not self.heap:
            print("The heap is empty!")
            return
        
        tree_root = self.heap[0]

        tree = nx.DiGraph()
        pos = {tree_root.id: (0, 0)}
        tree = self.add_edges(tree, tree_root, pos)

        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.show()

# Usage example for minimal heap
heap = BinaryHeap(heap_type='min')
heap.build_heap([10, 4, 5, 3, 1, 2])

# Draw the heap
heap.draw_heap()