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
