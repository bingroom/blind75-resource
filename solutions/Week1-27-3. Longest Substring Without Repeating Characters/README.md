# Longest Substring Without Repeating Characters

**Topic:** String
- **LeetCode 連結:** [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- **難度:** Medium

## 題目描述

給定一個字串 `s`，找出其中不包含重複字元的最長子字串的長度。

## 解題思路

1. 使用滑動視窗搭配集合（set）來追蹤視窗內的字元。
2. 右指針逐步向右擴展視窗。
3. 若新字元已存在於集合中，左指針向右收縮並移除字元，直到無重複。
4. 每次擴展後更新最長長度。
5. 遍歷結束後回傳最長長度。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)。
- **空間複雜度:** O(min(n, |Σ|))，Σ 為字元集。
