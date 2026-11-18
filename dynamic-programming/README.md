# Dynamic Programming

**Core idea:** define what `dp[x]` means, write the transition from smaller subproblems, then fill in order (bottom-up) or recurse with a cache (top-down). Brute-force DFS becomes DP once the recursion returns "the answer for this subproblem" rather than carrying a running total down.

**When to use:** "fewest / most / number of ways", where the same subproblem repeats.


| # | Problem | Core algorithm | Time | Space |
|---|---------|----------------|------|-------|
| 322 | [Coin Change](0322_coin_change.py) | Unbounded knapsack: bottom-up DP, or DFS + memo on remaining amount | O(amount · len(coins)) | O(amount) |

## Mistakes to remember

**322 Coin Change**
- Called `Solution.coinExchange([1,2,5], 11)` on the class, so `[1,2,5]` was bound to `self` → `TypeError: missing 1 required positional argument: 'amount'`. Use `Solution().coinChange(...)` or a top-level function.
- `List[int]` without `from typing import List` (Pyright flagged it). Use built-in `list[int]`. Same root cause as `defaultdict(List[int])` in 314.
- First run printed nothing: forgot `print`.
- No -1 path: when no coin fits, `res` is empty and `min(res)` raises `ValueError` (e.g. `coins=[2], amount=3`).
- Plain DFS without memo is exponential (amount 25 → 30 got ~8x slower). Passing `coinNum` down as an accumulator also prevents memoization; return "fewest coins for `remaining`" and cache on `remaining`, or use bottom-up DP.
- Typo: `remainning`.
