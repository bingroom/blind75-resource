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
