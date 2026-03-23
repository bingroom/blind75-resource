# LeetCode 20. Valid Parentheses
# 時間複雜度: O(n)  空間複雜度: O(n)
# 可整段複製至 NeetCode / LeetCode 提交以確認 AC

class Solution:
    def isValid(self, s: str) -> bool:
        """
        判斷括號是否正確配對。用 stack：左括號 push，右括號 pop 並檢查是否對應。
        """
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in pair:
                if not stack or stack[-1] != pair[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0
