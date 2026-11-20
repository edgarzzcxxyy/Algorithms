"""
Two Sum: all unique pairs
Category: Two Pointers
Core algorithm: sort + two pointers from both ends, skip duplicates
"""
from typing import List, Tuple


def two_sum_all_pairs(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique pairs in nums that sum to target.
    Each pair is returned as a sorted tuple (a, b) where a <= b.
    No duplicate pairs in the output.
    
    Time: O(n)  |  Space: O(n)
    """
    nums.sort()
    l,r = 0, len(nums) - 1
    res = []
    while l < r:
        total = nums[l] + nums[r]
        if total < target:
            l += 1
        elif total > target:
            r -= 1
        else:
            res.append((nums[l], nums[r]))
            l += 1
            while l < r and nums[l-1] == nums[l]:
                l += 1
    print(res)
    return res 





# ── Test Cases ──────────────────────────────────────────────────────────

def test_basic():
    assert two_sum_all_pairs([1, 3, 2, 2, 4, 0], 4) == [(0, 4), (1, 3), (2, 2)]

def test_no_pairs():
    assert two_sum_all_pairs([1, 2, 3], 10) == []

def test_single_element():
    assert two_sum_all_pairs([5], 10) == []

def test_empty():
    assert two_sum_all_pairs([], 0) == []

def test_negatives():
    assert two_sum_all_pairs([-1, 0, 1, 2, -2, 3], 1) == [(-2, 3), (-1, 2), (0, 1)]

def test_duplicates_only_one_pair():
    # Multiple 3s and 2s, but (2,3) should appear only once
    assert two_sum_all_pairs([3, 3, 2, 2, 2], 5) == [(2, 3)]

def test_zeros():
    assert two_sum_all_pairs([0, 0, 0], 0) == [(0, 0)]

def test_all_same():
    assert two_sum_all_pairs([4, 4, 4, 4], 8) == [(4, 4)]

def test_large_target():
    assert two_sum_all_pairs([100, 200, 300, 400], 500) == [(100, 400), (200, 300)]

def test_negative_target():
    assert two_sum_all_pairs([-5, -3, -2, 0, 1], -5) == [(-5, 0), (-3, -2)]


if __name__ == "__main__":
    tests = [
        test_basic,
        test_no_pairs,
        test_single_element,
        test_empty,
        test_negatives,
        test_duplicates_only_one_pair,
        test_zeros,
        test_all_same,
        test_large_target,
        test_negative_target,
    ]
    for t in tests:
        try:
            t()
            print(f"✓ {t.__name__}")
        except AssertionError as e:
            print(f"✗ {t.__name__}: {e}")

    print(f"\nRan {len(tests)} tests.")