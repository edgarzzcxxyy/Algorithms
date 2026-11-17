"""
LeetCode 415. Add Strings

Two non-negative integers given as strings (no leading zeros except "0").
Return their sum as a string.

Approach: simulate column addition from the last digit, track carry,
build the result with deque.appendleft.
Time O(max(m, n)), Space O(max(m, n)).
"""
from collections import deque


def addStrings(num1: str, num2: str) -> str:
    i, j, carry = len(num1) - 1, len(num2) - 1, 0
    res = deque()
    while i >= 0 or j >= 0 or carry:
        d1 = int(num1[i]) if i >= 0 else 0
        d2 = int(num2[j]) if j >= 0 else 0
        total = d1 + d2 + carry
        res.appendleft(str(total % 10))
        carry = total // 10
        i, j = i - 1, j - 1
    return "".join(res)


if __name__ == "__main__":
    assert addStrings("532", "87") == "619"
    assert addStrings("0", "0") == "0"
    assert addStrings("999", "1") == "1000"
    print("ok")
