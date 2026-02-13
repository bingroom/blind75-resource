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
