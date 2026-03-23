# LC 394. Decode String (Medium)
# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_num = 0

        for ch in s:
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)
            elif ch == '[':
                # Save current state and start fresh
                stack.append((cur_str, cur_num))
                cur_str = ""
                cur_num = 0
            elif ch == ']':
                # Pop previous state and repeat current string
                prev_str, repeat = stack.pop()
                cur_str = prev_str + cur_str * repeat
            else:
                cur_str += ch

        return cur_str
