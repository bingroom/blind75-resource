# Decode String

## Problem Description
Given an encoded string like `3[a2[c]]`, decode it by repeating the substring inside brackets by the preceding number. The example decodes to `accaccacc`.

## Approach
Maintain a running `cur_str` and `cur_num`. When hitting `[`, push the current string and number onto the stack and reset them. When hitting `]`, pop the previous string and repeat count, then set `cur_str = prev_str + cur_str * repeat`. Digits build up `cur_num` (handling multi-digit numbers), and letters are appended to `cur_str`.

## Complexity
- **Time:** O(n * max_k) where n is the length of the output string and max_k is the maximum nesting multiplier
- **Space:** O(n) for the stack and output string
