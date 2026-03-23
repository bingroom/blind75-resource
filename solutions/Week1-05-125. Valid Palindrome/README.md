# Valid Palindrome

**Topic:** String
- **LeetCode 連結:** [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- **難度:** Easy

## 題目描述

給定一個字串 `s`，判斷它是否為迴文（palindrome）。判斷時只考慮英文字母和數字，忽略大小寫及其他字元。

## 解題思路

1. 設定左右兩個指針，分別從字串頭尾開始向中間移動。
2. 遇到非英數字元時跳過。
3. 比較左右指針所指的字元（轉小寫後），若不同則回傳 `False`。
4. 若所有比較都相同，回傳 `True`。

## 程式碼

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

## 複雜度分析

- **時間複雜度:** O(n)，每個字元最多被訪問兩次。
- **空間複雜度:** O(1)，只使用兩個指針與常數變數。
