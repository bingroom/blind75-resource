# Valid Palindrome

**Topic:** String

- **LeetCode:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **NeetCode:** [Blind 75](https://neetcode.io/problems?list=blind75)

## Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or *`false`* otherwise*.

 

**Example 1:**

```

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

**Example 2:**

```

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

**Example 3:**

```

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

**Constraints:**

	- `1 <= s.length <= 2 * 10^5`

	- `s` consists only of printable ASCII characters.

## Solution

```python
# LeetCode 125. Valid Palindrome
# NeetCode: https://neetcode.io/problems/is-palindrome?list=blind75
# 時間複雜度: O(n)  空間複雜度: O(1)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        判斷是否為迴文（只考慮英數字、忽略大小寫與其他字元）。
        雙指針：左右往內，跳過非英數字，比較轉小寫後是否相同。
        """
        left, right = 0, len(s) - 1
        while left < right:
            # 跳過非英數字
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

```

## 思路

- **雙指針：** 左指針從頭、右指針從尾往內。若當前字元非英數字則移動跳過；否則比較轉小寫後是否相同，不同則回傳 False。相遇或交錯後回傳 True。

## 時間 / 空間複雜度

- **時間:** O(n)，每個字元最多被訪問兩次。
- **空間:** O(1)，只使用兩個指針與常數變數。

## 相關閱讀

- **演算法:** Two Pointers（雙指針）
- **字串:** 字元判斷 `isalnum()`、大小寫 `lower()`
