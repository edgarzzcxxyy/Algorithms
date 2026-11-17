"""
LeetCode 987. Vertical Order Traversal of a Binary Tree
(Follow-up 2 of 314: sort nodes in the same row and column by value.)

Approach: record (col, row, val) for every node, sort, group by column.
Time O(n log n), Space O(n).
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    nodes = []

    def dfs(node, row, col):
        if not node:
            return
        nodes.append((col, row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)
    nodes.sort()
    res, prev = [], None
    for col, _, val in nodes:
        if col != prev:
            res.append([])
            prev = col
        res[-1].append(val)
    return res


if __name__ == "__main__":
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(6)),
                    TreeNode(3, TreeNode(5), TreeNode(7)))
    assert verticalTraversal(root) == [[4], [2], [1, 5, 6], [3], [7]]
    print("ok")
