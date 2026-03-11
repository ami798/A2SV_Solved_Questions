class Solution:
    def minOperations(self, logs: List[str]) -> int:
        n = len(logs)
        stack = []

        for i in range(0, n):
            if logs[i] == "./":
                continue
            elif logs[i] == "../":
                if stack:
                    stack.pop()
            else:
                stack.append(logs[i])

        return len(stack) 