# Palindromic Substrings

**Topic:** String

- **LeetCode:** [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

 

**Example 1:**

```

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

```

**Example 2:**

```

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase English letters.

## Solution

```python
# LeetCode 647. Palindromic Substrings
# 時間複雜度: O(n²)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        計算迴文子字串的個數。以每個位置為中心向外擴展，每擴展成功一次就多一個迴文。
        """
        n = len(s)
        count = 0

        def expand(l: int, r: int) -> None:
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        return count

```

## 思路

- **中心擴展：** 與「最長迴文子字串」相同，以每個位置為奇/偶中心向外擴展，每成功擴展一格就多一個迴文，累加 count。

## 時間 / 空間複雜度

- **時間:** O(n²)。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Expand Around Center
