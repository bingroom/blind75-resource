# Decode Ways

- **LeetCode:** [91. Decode Ways](https://leetcode.com/problems/decode-ways/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

You have intercepted a secret message encoded as a string of numbers. The message is **decoded** via the following mapping:

`"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'`

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes (`"2"` and `"5"` vs `"25"`).

For example, `"11106"` can be decoded into:

	- `"AAJF"` with the grouping `(1, 1, 10, 6)`

	- `"KJF"` with the grouping `(11, 10, 6)`

	- The grouping `(1, 11, 06)` is invalid because `"06"` is not a valid code (only `"6"` is valid).

Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the **number of ways** to **decode** it. If the entire string cannot be decoded in any valid way, return `0`.

The test cases are generated so that the answer fits in a **32-bit** integer.

 

**Example 1:**

**Input:** s = "12"

**Output:** 2

**Explanation:**

"12" could be decoded as "AB" (1 2) or "L" (12).

**Example 2:**

**Input:** s = "226"

**Output:** 3

**Explanation:**

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

**Example 3:**

**Input:** s = "06"

**Output:** 0

**Explanation:**

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

**Constraints:**

	- `1 <= s.length <= 100`

	- `s` contains only digits and may contain leading zero(s).

## Solution

```python
# LeetCode 91. Decode Ways
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        數字串可解碼成 A=1..Z=26，求解碼方法數。dp[i] 與 dp[i-1]、dp[i-2] 有關（單字元 / 雙字元）。
        """
        if not s or s[0] == "0":
            return 0
        prev, cur = 1, 1
        for i in range(1, len(s)):
            next_ = 0
            if s[i] != "0":
                next_ += cur
            two = int(s[i - 1 : i + 1])
            if 10 <= two <= 26:
                next_ += prev
            prev, cur = cur, next_
        return cur

```

## 思路

- **DP：** 當前位置可從前一個（單字元）或前兩個（雙字元 10–26）轉移。注意 '0' 不能單獨解碼。可壓成兩變數。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Dynamic Programming、字串解碼
