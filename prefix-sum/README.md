# Prefix Sum

**Core idea:** `prefix[j] - prefix[i]` is the sum of elements `(i, j]`, so any range sum is O(1) after an O(n) pass.

**When to use:**
- Count or find subarrays with a target sum → prefix sum + hash map. Works with negative numbers; a sliding window doesn't.
- Weighted random pick → prefix sums of positive weights are increasing, so binary search (`bisect_left`) finds the bucket for a random target.


| # | Problem | Core algorithm | Time | Space |
|---|---------|----------------|------|-------|
| 560 | [Subarray Sum Equals K](0560_subarray_sum_equals_k.py) | Prefix sum + hash map, seed `{0: 1}` | O(n) | O(n) |
| — | [K Winners (weighted, no duplicates)](kwinners.py) | Prefix sum + binary search per draw, reject repeats (base problem: LeetCode 528) | O(n) build, O(log n) per draw | O(n) |

## Mistakes to remember

**560 Subarray Sum Equals K** (not finished in the interview)
- Went straight to a sliding window (`left, right`, grow while `cur < k`). It breaks when nums has negative numbers: ask about negatives first, then use prefix sum + hash map.
- Base case `if len(nums) == 0 or len(nums) == 1: return 1` is wrong: one element counts only if it equals k; empty gives 0.

**K Winners**
- A zero weight with k == n loops forever (that index can't be drawn).
- Rejection slows down once most of the weight is picked: the expected draws for the next new winner = total / remaining weight.
