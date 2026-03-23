# LeetCode 191. Number of 1 Bits (Hamming weight)
# 時間複雜度: O(1) 位元數  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        計算 n 的二進位表示中 1 的個數。每次 n &= n - 1 會消掉最右邊一個 1。
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
