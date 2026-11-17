"""
LeetCode 314. Binary Tree Vertical Order Traversal

Output columns left to right; within a column top to bottom,
same row and column left to right.

Approach: BFS with (node, column); track min/max column so no sort is needed.
DFS alone does not guarantee top-to-bottom order within a column.
Time O(n), Space O(n).
"""
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    cols = defaultdict(list)
    q = deque([(root, 0)])
    lo = hi = 0
    while q:
        node, c = q.popleft()
        cols[c].append(node.val)
        lo, hi = min(lo, c), max(hi, c)
        if node.left:
            q.append((node.left, c - 1))
        if node.right:
            q.append((node.right, c + 1))
    return [cols[c] for c in range(lo, hi + 1)]


if __name__ == "__main__":
    #        3
    #      /   \
    #     9     8
    #    / \   / \
    #   4   0 1   7
    #  /
    # 10
    root = TreeNode(3,
                    TreeNode(9, TreeNode(4, TreeNode(10)), TreeNode(0)),
                    TreeNode(8, TreeNode(1), TreeNode(7)))
    assert verticalOrder(root) == [[10], [4], [9], [3, 0, 1], [8], [7]]
    print("ok")
