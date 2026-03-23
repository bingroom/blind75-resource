# LC 227. Basic Calculator II (Medium)
# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur_num = 0
        op = '+'  # previous operator

        for i, ch in enumerate(s):
            if ch.isdigit():
                cur_num = cur_num * 10 + int(ch)

            # Process when we hit an operator or end of string
            if ch in "+-*/" or i == len(s) - 1:
                if op == '+':
                    stack.append(cur_num)
                elif op == '-':
                    stack.append(-cur_num)
                elif op == '*':
                    stack.append(stack.pop() * cur_num)
                elif op == '/':
                    stack.append(int(stack.pop() / cur_num))
                op = ch
                cur_num = 0

        return sum(stack)
