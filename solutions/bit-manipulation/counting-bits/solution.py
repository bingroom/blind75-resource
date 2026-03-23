# LeetCode 338. Counting Bits
# 時間複雜度: O(n)  空間複雜度: O(1) 不含輸出
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        對 0..n 每個數回傳其二進位中 1 的個數。DP：i 的 1 的個數 = i>>1 的個數 + (i&1)。
        """
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
