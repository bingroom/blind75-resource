# LeetCode 190. Reverse Bits
# 時間複雜度: O(1) 32 次  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        將 32 位無符號整數的二進位反轉。從右到左取位，依序放到結果的左到右。
        """
        out = 0
        for _ in range(32):
            out = (out << 1) | (n & 1)
            n >>= 1
        return out
