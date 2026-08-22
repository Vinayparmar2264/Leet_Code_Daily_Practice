"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        from collections import deque

        # original node -> cloned node
        clones = {}

        # Clone the starting node
        clones[node] = Node(node.val)

        que = deque()
        que.append(node)

        while que:

            current = que.popleft()

            for neighbor in current.neighbors:

                # If neighbor is not cloned yet
                if neighbor not in clones:

                    clones[neighbor] = Node(neighbor.val)
                    que.append(neighbor)

                # Connect cloned current node to cloned neighbor
                clones[current].neighbors.append(clones[neighbor])

        return clones[node]