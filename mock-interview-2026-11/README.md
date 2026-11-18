# Mock Interview (2026-11)

| # | Problem | Approach | Complexity |
|---|---------|----------|------------|
| 415 | [Add Strings](0415_add_strings.py) | Two pointers from the end + carry, `deque.appendleft` | O(max(m, n)) |
| 314 | [Binary Tree Vertical Order Traversal](0314_vertical_order.py) | BFS with column index, track min/max column | O(n) |
| 987 | [Vertical Order Traversal of a Binary Tree](0987_vertical_traversal.py) | Follow-up 2: collect (col, row, val), sort, group | O(n log n) |
| — | [K Winners (weighted, no duplicates)](kwinners.py) | Prefix sums + binary search per draw, reject repeats | O(n) build, O(log n) per draw |
| 560 | [Subarray Sum Equals K](0560_subarray_sum_equals_k.py) | Prefix sum + hash map of prefix counts, seed `{0: 1}` | O(n) time, O(n) space |
| 322 | [Coin Change](0322_coin_change.py) | DFS + memo on remaining amount, or bottom-up DP | O(amount · len(coins)) time, O(amount) space |

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

**560 Subarray Sum Equals K** (not finished in the interview)
- Went straight to a sliding window (`left, right`, grow while `cur < k`). It breaks when nums has negative numbers: ask about negatives first, then use prefix sum + hash map.
- Base case `if len(nums) == 0 or len(nums) == 1: return 1` is wrong: one element counts only if it equals k; empty gives 0.

**322 Coin Change**
- Called `Solution.coinExchange([1,2,5], 11)` on the class, so `[1,2,5]` was bound to `self` → `TypeError: missing 1 required positional argument: 'amount'`. Use `Solution().coinChange(...)` or a top-level function.
- `List[int]` without `from typing import List` (Pyright flagged it). Use built-in `list[int]`. Same root cause as `defaultdict(List[int])` in 314.
- First run printed nothing: forgot `print`.
- No -1 path: when no coin fits, `res` is empty and `min(res)` raises `ValueError` (e.g. `coins=[2], amount=3`).
- Plain DFS without memo is exponential (amount 25 → 30 got ~8x slower). Passing `coinNum` down as an accumulator also prevents memoization; return "fewest coins for `remaining`" and cache on `remaining`, or use bottom-up DP.
- Typo: `remainning`.

## Interviewer notes (560 / 322 session)

| Note (as written in the pad) | Meaning |
|------------------------------|---------|
| empty, sorted, negative number, directed graph, input, output | Clarifying questions to ask: empty input? sorted? negatives? graph directed? input/output format? |
| clarification | Clarify before solving |
| high level solution (观察表情) | Give the high-level solution before coding and watch the interviewer's reaction |
| 变量名字 | Variable names |
| 需不需要更复杂的example — 好不好 | Ask whether a more complex example is needed |
| 时间空间复杂度 | Time/space complexity |
| 准备几道题? | At the start, ask the interviewer roughly how many problems there will be |
| rush | Don't rush |
| syntax | Syntax |

## REACTO framework
Repeat → Example → Approach 1/2/3 (state time/space complexity for each) → Coding → Test → Optimization

Feedback #1: time/space complexity.
