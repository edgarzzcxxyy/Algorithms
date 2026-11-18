# Trees

**Core idea:** traverse with BFS (level order, top to bottom) or DFS (recursion), carrying extra info such as column, row or depth alongside each node.

**When to use:**
- Order by level / "top to bottom" → BFS.
- Need every node's coordinates, then a custom order → DFS to collect, then sort.


| # | Problem | Core algorithm | Time | Space |
|---|---------|----------------|------|-------|
| 314 | [Binary Tree Vertical Order Traversal](0314_vertical_order.py) | BFS with column index, track min/max column | O(n) | O(n) |
| 987 | [Vertical Order Traversal of a Binary Tree](0987_vertical_traversal.py) | Follow-up 2 of 314: DFS collect (col, row, val), sort, group | O(n log n) | O(n) |

## Mistakes to remember

**314 Vertical Order**
- `defaultdict(List[int])` fails; use `defaultdict(list)`.
- `append[...]` vs `append(...)`.
- Right child recursed with `node.left` by mistake.
- Assigning `minColumn/maxColumn` inside a nested function needs `nonlocal`; initialize to 0, not ±inf.
- DFS does not guarantee top-to-bottom order within a column; use BFS.
