# LC 224. Basic Calculator (Hard)
# https://leetcode.com/problems/basic-calculator/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1  # +1 or -1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                # Save current result and sign, then reset
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                # Finalize the expression inside parentheses
                result += sign * num
                num = 0
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result

        # Don't forget the last number
        result += sign * num
        return result
