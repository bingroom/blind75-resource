# Longest Substring Without Repeating Characters

- **LeetCode:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Given a string `s`, find the length of the **longest** **substring** without duplicate characters.

 

**Example 1:**

```

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

```

**Example 2:**

```

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

```

**Example 3:**

```

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

```

 

**Constraints:**

	- `0 <= s.length <= 5 * 10^4`

	- `s` consists of English letters, digits, symbols and spaces.

## Solution

```python
# LeetCode 3. Longest Substring Without Repeating Characters
# 時間複雜度: O(n)  空間複雜度: O(min(n, |Σ|))
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        求最長不重複字元的子字串長度。滑窗 + set：右擴、遇重複則左縮直到無重複。
        """
        seen = set()
        left = 0
        best = 0
        for right, c in enumerate(s):
            while c in seen:
                seen.discard(s[left])
                left += 1
            seen.add(c)
            best = max(best, right - left + 1)
        return best

```

## 思路

- **滑動視窗 + Set：** 右指針擴展，用 set 記錄視窗內字元；若新字元已存在則左指針往右縮直到該字元被移除，再擴右。過程中記錄最大視窗長度。

## 時間 / 空間複雜度

- **時間:** O(n)。
- **空間:** O(min(n, |Σ|))，Σ 為字元集。

## 相關閱讀

- **演算法:** Sliding Window、Hash Set
- **資料結構:** Set
