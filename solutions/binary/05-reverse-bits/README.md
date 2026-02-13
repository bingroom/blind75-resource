# Reverse Bits

- **LeetCode:** [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

Reverse bits of a given 32 bits signed integer.

 

**Example 1:**

**Input:** n = 43261596

**Output:** 964176192

**Explanation:**

	
		
			Integer
			Binary
		
		
			43261596
			00000010100101000001111010011100
		
		
			964176192
			00111001011110000010100101000000
		
	

**Example 2:**

**Input:** n = 2147483644

**Output:** 1073741822

**Explanation:**

	
		
			Integer
			Binary
		
		
			2147483644
			01111111111111111111111111111100
		
		
			1073741822
			00111111111111111111111111111110
		
	

 

**Constraints:**

	- `0 <= n <= 2^31 - 2`

	- `n` is even.

 

**Follow up:** If this function is called many times, how would you optimize it?

## Solution

```python
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

```

## 思路

- 從 n 的最低位開始取（n & 1），每次把結果左移並加上該位，共做 32 次。

## 時間 / 空間複雜度

- **時間:** O(1)（32 次）。
- **空間:** O(1)。

## 相關閱讀

- **演算法:** Bit Manipulation
