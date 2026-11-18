"""
LeetCode 560. Subarray Sum Equals K

Count the contiguous subarrays whose sum equals k.
1 <= len(nums) <= 2 * 10^4; nums can contain negative numbers.

Approach: prefix sum + hash map. A subarray (i, j] sums to k exactly when
prefix[j] - prefix[i] == k, so at each prefix add how many earlier prefixes
equal prefix - k. Seed the map with {0: 1} to count subarrays starting at 0.
Time O(n), Space O(n).

A sliding window only works when every number is non-negative: with
negatives, extending the window can lower the sum, so there's no rule for
which pointer to move.
"""
import random
from collections import defaultdict


def subarraySum(nums: list[int], k: int) -> int:
    seen = defaultdict(int)
    seen[0] = 1
    prefix = count = 0
    for x in nums:
        prefix += x
        count += seen[prefix - k]
        seen[prefix] += 1
    return count


def brute(nums: list[int], k: int) -> int:
    return sum(sum(nums[i:j]) == k
               for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))


if __name__ == "__main__":
    assert subarraySum([1, 1, 1], 2) == 2
    assert subarraySum([1, 2, 3], 3) == 2       # [1, 2], [3]
    assert subarraySum([1, -1, 0], 0) == 3      # [1, -1], [0], [1, -1, 0]
    assert subarraySum([3], 3) == 1
    assert subarraySum([1], 0) == 0
    random.seed(0)
    for _ in range(500):
        nums = [random.randint(-3, 3) for _ in range(random.randint(1, 8))]
        k = random.randint(-4, 4)
        assert subarraySum(nums, k) == brute(nums, k), (nums, k)
    print("ok")
