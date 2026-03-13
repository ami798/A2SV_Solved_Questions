class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                val = stack.pop()
                score = max(2 * val, 1)
                stack[-1] += score

        return stack[0]