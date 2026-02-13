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
