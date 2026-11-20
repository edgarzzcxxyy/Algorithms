# Two Pointers

**Core idea:** move two indices through one or two sequences so each element is visited once, instead of nested loops.

**When to use:** sorted arrays, palindromes, merging, and digit-by-digit arithmetic on strings or lists (walk both from the end).


| # | Problem | Core algorithm | Time | Space |
|---|---------|----------------|------|-------|
| 415 | [Add Strings](0415_add_strings.py) | Two pointers from the end + carry, `deque.appendleft` | O(max(m, n)) | O(max(m, n)) |
| — | [Two Sum: all unique pairs](two_sum_all_pairs.py) | Sort + two pointers from both ends, skip duplicates | O(n log n) | O(n) |

## Mistakes to remember

**415 Add Strings**
- `if ptr < 0: digit = 0` followed by an unconditional `digit = int(s[ptr])` overwrites the 0; a negative index silently reads from the end in Python. Use if/else.
- Handle the final carry (put `carry` in the while condition).
- Special-casing "0" is unnecessary.
