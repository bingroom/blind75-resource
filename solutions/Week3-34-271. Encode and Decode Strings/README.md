# Encode and Decode Strings

**Topic:** String
- **LeetCode 連結:** [271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)
- **難度:** Medium

## 題目描述

設計一個演算法，將字串列表編碼為單一字串，並能解碼還原。需處理任意字元（包含分隔符）。

## 解題思路

1. 編碼時，每個字串前加上「長度#」前綴（例如 "5#hello"）。
2. 解碼時，先讀取 '#' 前的數字得到長度。
3. 根據長度擷取對應數量的字元，還原原始字串。

## 程式碼

```python
# LeetCode 271. Encode and Decode Strings
# Time: O(n) for both encode and decode  Space: O(n)

from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encode each string as 'length#string'."""
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        """Decode by reading length, then extracting that many characters."""
        result = []
        i = 0
        while i < len(s):
            # Find the '#' delimiter
            j = s.index('#', i)
            length = int(s[i:j])
            result.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return result
```

## 複雜度分析

- **時間複雜度:** O(n) for both encode and decode, where n is total characters
- **空間複雜度:** O(n)
