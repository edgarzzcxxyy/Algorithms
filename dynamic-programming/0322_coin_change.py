"""
LeetCode 322. Coin Change
Category: Dynamic Programming
Core algorithm: unbounded knapsack DP (or DFS + memo)

Given coin denominations and an amount, return the fewest coins that make up
the amount (unlimited supply of each coin), or -1 if it can't be made.

Approach 1: DFS + memo on the remaining amount. dfs(r) returns the fewest
coins for r (not "coins used so far"), so results can be cached.
Approach 2: bottom-up DP. dp[a] = min(dp[a - c] + 1) over coins c <= a.
Both: Time O(amount * len(coins)), Space O(amount).
Plain DFS without memo is exponential.
"""
from functools import lru_cache


def coinChangeMemo(coins: list[int], amount: int) -> int:
    @lru_cache(maxsize=None)
    def dfs(remaining: int) -> float:
        if remaining == 0:
            return 0
        best = float("inf")
        for c in coins:
            if c <= remaining:
                best = min(best, dfs(remaining - c) + 1)
        return best

    ans = dfs(amount)
    return -1 if ans == float("inf") else ans


def coinChange(coins: list[int], amount: int) -> int:
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return -1 if dp[amount] == INF else dp[amount]


if __name__ == "__main__":
    cases = [
        (([1, 2, 5], 11), 3),
        (([1, 2], 6), 3),
        (([2], 3), -1),      # can't be made
        (([1], 0), 0),       # amount 0
        (([186, 419, 83, 408], 6249), 20),
    ]
    for (coins, amount), want in cases:
        assert coinChange(coins, amount) == want, (coins, amount)
        assert coinChangeMemo(coins, amount) == want, (coins, amount)
    print("ok")
