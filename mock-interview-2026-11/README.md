# Mock Interview (2026-11)

| # | Problem | Approach | Complexity |
|---|---------|----------|------------|
| 415 | [Add Strings](0415_add_strings.py) | Two pointers from the end + carry, `deque.appendleft` | O(max(m, n)) |
| 314 | [Binary Tree Vertical Order Traversal](0314_vertical_order.py) | BFS with column index, track min/max column | O(n) |
| 987 | [Vertical Order Traversal of a Binary Tree](0987_vertical_traversal.py) | Follow-up 2: collect (col, row, val), sort, group | O(n log n) |

## Mistakes to remember

**415 Add Strings**
- `if ptr < 0: digit = 0` followed by an unconditional `digit = int(s[ptr])` overwrites the 0; a negative index silently reads from the end in Python. Use if/else.
- Handle the final carry (put `carry` in the while condition).
- Special-casing "0" is unnecessary.

**314 Vertical Order**
- `defaultdict(List[int])` fails; use `defaultdict(list)`.
- `append[...]` vs `append(...)`.
- Right child recursed with `node.left` by mistake.
- Assigning `minColumn/maxColumn` inside a nested function needs `nonlocal`; initialize to 0, not ±inf.
- DFS does not guarantee top-to-bottom order within a column; use BFS.

## REACTO framework
Repeat → Example → Approach 1/2/3 (state time/space complexity for each) → Coding → Test → Optimization

Feedback #1: time/space complexity.
