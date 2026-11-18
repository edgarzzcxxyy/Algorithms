# Algorithms

Algorithm practice and mock interview solutions (Python), grouped by core algorithm. Each topic folder's README has the core idea, a problem table and mistakes to remember. Each solution file starts with `Category:` and `Core algorithm:` lines.

## Topics

| Topic | Core idea | Problems |
|-------|-----------|----------|
| [Two Pointers](two-pointers/) | Two indices instead of nested loops; walk from the end for digit arithmetic | 415 |
| [Prefix Sum](prefix-sum/) | Range sum = prefix difference; + hash map for target sums, + binary search for weighted pick | 560, K Winners |
| [Trees](trees/) | BFS / DFS carrying extra info (column, row) | 314, 987 |
| [Graphs](graphs/) | BFS for shortest path; expand the state when it depends on more than the node | Shortest Trip with Fuel |
| [Dynamic Programming](dynamic-programming/) | Define `dp[x]`, write the transition, fill bottom-up or memoize | 322 |

## Other
- [Mock interviews](mock-interviews/): session logs with problem lists, interviewer notes, REACTO
- [Behavioral](behavioral/): BQ notes and question list

## Adding a problem
1. Put the file in its topic folder as `NNNN_name.py` (LeetCode number, if any).
2. Start the docstring with the title, `Category:` and `Core algorithm:`, then the approach and time/space complexity; add asserts under `if __name__ == "__main__"`.
3. Add a row to the topic README's table (and mistakes, if any).
