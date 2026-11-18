"""
K Winners: weighted random pick without replacement
Category: Prefix Sum
Core algorithm: prefix sum + binary search (weighted random pick, like LeetCode 528) + rejection

Each customer has a purchase amount. Pick k distinct winners, where a
customer's chance of being picked is proportional to their amount.
If k > n, return every customer.

Approach: prefix sums + binary search for each weighted draw; if the drawn
index was already picked, draw again (rejection).
Time: O(n) to build prefix sums, O(log n) per draw. The expected number of
draws for the next new winner is total / (weight not yet picked), so it slows
down once most of the weight has been picked. Space O(n).
"""
import random 
from collections import Counter

def kwinners_no_dup(cus:list[int], k:int):
    if k > len(cus):
        return list(range(len(cus)))
    prefix = []
    total = 0 
    for i in range(len(cus)):
        total += cus[i]
        prefix.append(total)

    res = []
    seen = set()
    while len(res) < k:
        target = random.uniform(0, total)
        l, r = 0, len(prefix)
        while l < r:
            mid = (l + r) // 2
            if prefix[mid] < target:
                l = mid + 1
            else:
                r = mid
        if l not in seen:
            res.append(l)
            seen.add(l)
    return res 


# ============================================================
# TEST 1: Returns exactly K winners
# ============================================================
def test_returns_k_winners():
    prices = [1, 2, 3, 4, 5]
    winners = kwinners_no_dup(prices, 3)
    assert len(winners) == 3, f"Expected 3, got {len(winners)}"
    print("✓ TEST 1 passed: returns K winners")


# ============================================================
# TEST 2: No duplicates in the output
# ============================================================
def test_no_duplicates():
    random.seed(42)
    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # Run many times to catch rare duplicate bugs
    for trial in range(1000):
        winners = kwinners_no_dup(prices, 5)
        assert len(winners) == len(set(winners)), \
            f"Duplicates found: {winners}"
    print("✓ TEST 2 passed: no duplicates across 1000 trials")


# ============================================================
# TEST 3: K > N returns all customers exactly once
# ============================================================
def test_k_exceeds_n():
    prices = [5, 10, 15]
    winners = kwinners_no_dup(prices, 100)
    assert len(winners) == 3, f"Expected 3 (capped at N), got {len(winners)}"
    assert set(winners) == {0, 1, 2}
    print("✓ TEST 3 passed: K>N returns all customers")


# ============================================================
# TEST 4: K == N returns all customers
# ============================================================
def test_k_equals_n():
    random.seed(42)
    prices = [1, 10, 100, 1000]
    winners = kwinners_no_dup(prices, 4)
    assert sorted(winners) == [0, 1, 2, 3], f"Got {sorted(winners)}"
    print("✓ TEST 4 passed: K=N returns all customers")


# ============================================================
# TEST 5: K == 0 returns empty
# ============================================================
def test_k_zero():
    prices = [1, 2, 3]
    winners = kwinners_no_dup(prices, 0)
    assert winners == []
    print("✓ TEST 5 passed: K=0 returns []")


# ============================================================
# TEST 6: K == 1 gives a valid single winner
# ============================================================
def test_k_one():
    random.seed(42)
    prices = [1, 2, 3, 4, 5]
    winners = kwinners_no_dup(prices, 1)
    assert len(winners) == 1
    assert winners[0] in range(5)
    print("✓ TEST 6 passed: K=1 works")


# ============================================================
# TEST 7: Single customer
# ============================================================
def test_single_customer():
    prices = [50]
    winners = kwinners_no_dup(prices, 5)
    assert winners == [0]
    print("✓ TEST 7 passed: single customer returned once")


# ============================================================
# TEST 8: First-pick distribution matches weights
# ============================================================
def test_first_pick_weighted():
    """The FIRST winner should follow the weighted distribution.
    After that, probabilities shift, so we only check the first pick."""
    random.seed(42)
    prices = [1, 10, 100]
    trials = 50_000
    total = sum(prices)
    counts = Counter()
    for _ in range(trials):
        winners = kwinners_no_dup(prices, 1)
        counts[winners[0]] += 1
    
    expected = {i: trials * prices[i] / total for i in range(len(prices))}
    for i, exp in expected.items():
        actual = counts[i]
        err = abs(actual - exp) / exp
        assert err < 0.10, f"Index {i}: got {actual}, expected {exp:.0f}"
    print(f"✓ TEST 8 passed: first pick weighted correctly: {dict(counts)}")


# ============================================================
# TEST 9: Inclusion probability — heavy customers appear more often in the K-set
# ============================================================
def test_inclusion_probability():
    """Over many runs, heavier customers should appear in the winner set 
    more often than lighter ones."""
    random.seed(42)
    prices = [1, 10, 100]
    trials = 10_000
    k = 2
    counts = Counter()
    for _ in range(trials):
        winners = kwinners_no_dup(prices, k)
        for w in winners:
            counts[w] += 1
    
    # Heaviest should appear most often, lightest least often
    assert counts[2] > counts[1] > counts[0], \
        f"Expected count[2] > count[1] > count[0], got {dict(counts)}"
    # Heaviest should be in nearly every winning set
    assert counts[2] / trials > 0.95, f"Heavy customer inclusion rate: {counts[2]/trials}"
    print(f"✓ TEST 9 passed: inclusion counts: {dict(counts)}")


# ============================================================
# TEST 10: Uniform weights → uniform first-pick distribution
# ============================================================
def test_uniform_weights():
    random.seed(42)
    n = 5
    prices = [10] * n
    trials = 50_000
    counts = Counter()
    for _ in range(trials):
        winners = kwinners_no_dup(prices, 1)
        counts[winners[0]] += 1
    
    expected = trials / n
    for idx, count in counts.items():
        err = abs(count - expected) / expected
        assert err < 0.05, f"Index {idx}: got {count}, expected ~{expected}"
    print(f"✓ TEST 10 passed: uniform → uniform first pick: {dict(counts)}")


# ============================================================
# TEST 11: All indices in valid range
# ============================================================
def test_valid_indices():
    random.seed(42)
    prices = [1, 2, 3, 4, 5]
    for _ in range(1000):
        winners = kwinners_no_dup(prices, 3)
        assert all(0 <= w < 5 for w in winners)
    print("✓ TEST 11 passed: all indices in range")


# ============================================================
# TEST 12: Reproducibility with seed
# ============================================================
def test_reproducibility():
    prices = [1, 5, 10, 20, 50]
    random.seed(123)
    run1 = kwinners_no_dup(prices, 3)
    random.seed(123)
    run2 = kwinners_no_dup(prices, 3)
    assert run1 == run2, f"{run1} != {run2}"
    print("✓ TEST 12 passed: seeded runs reproducible")


# ============================================================
# TEST 13: Exhaustive small-case distribution check
# ============================================================
def test_exhaustive_small_case():
    """For prices [1, 2, 3] and k=2, verify each ordered pair appears 
    with approximately the correct probability.
    
    P(pick A first) = w_A / (w_A + w_B + w_C)
    P(pick B second | A first) = w_B / (w_B + w_C)
    """
    random.seed(42)
    prices = [1, 2, 3]
    trials = 60_000
    pair_counts = Counter()
    for _ in range(trials):
        winners = kwinners_no_dup(prices, 2)
        pair_counts[tuple(winners)] += 1
    
    # Expected probability for each ordered pair (i, j):
    # P(i) * P(j | i picked)
    total = sum(prices)
    expected = {}
    for i in range(3):
        for j in range(3):
            if i == j: continue
            p_i = prices[i] / total
            p_j_given_i = prices[j] / (total - prices[i])
            expected[(i, j)] = p_i * p_j_given_i * trials
    
    for pair, exp in expected.items():
        actual = pair_counts[pair]
        err = abs(actual - exp) / exp
        assert err < 0.10, f"Pair {pair}: got {actual}, expected {exp:.0f} (err {err:.2%})"
    print(f"✓ TEST 13 passed: ordered pair distribution matches theory")


# ============================================================
# TEST 14: Large input performance sanity
# ============================================================
def test_large_input():
    random.seed(42)
    n = 1000
    prices = [random.randint(1, 100) for _ in range(n)]
    winners = kwinners_no_dup(prices, 100)
    assert len(winners) == 100
    assert len(set(winners)) == 100, "Duplicates in large input!"
    print(f"✓ TEST 14 passed: N={n}, K=100 with no duplicates")


# ============================================================
# Run all
# ============================================================
if __name__ == "__main__":
    test_returns_k_winners()
    test_no_duplicates()
    test_k_exceeds_n()
    test_k_equals_n()
    test_k_zero()
    test_k_one()
    test_single_customer()
    test_first_pick_weighted()
    test_inclusion_probability()
    test_uniform_weights()
    test_valid_indices()
    test_reproducibility()
    test_exhaustive_small_case()
    test_large_input()
    print("\n🎉 All tests passed!")