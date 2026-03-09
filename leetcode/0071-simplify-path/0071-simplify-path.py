class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for char in path:
            if char in ["", "."]:
                continue
            elif char == "..":
                if stack:
                    stack.pop()
                continue

            stack.append(char)

        return "/" + "/".join(stack)
