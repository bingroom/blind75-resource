# Encode and Decode Strings

## Problem Description
Design an algorithm to encode a list of strings to a single string and decode it back to the original list. The encoded string is transmitted over a network.

## Approach
Length-prefixed encoding: each string is encoded as `"<length>#<string>"`. To decode, read digits until `#`, parse the length, extract that many characters, and repeat.

## Complexity
- **Time:** O(n) for both encode and decode, where n is total characters
- **Space:** O(n)
