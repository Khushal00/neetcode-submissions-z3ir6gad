class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split("/")
        for curr in directories:
            if curr == "..":
                if stack:
                    stack.pop()
            elif curr != "" and curr != ".":
                stack.append(curr)
        return "/" + "/".join(stack)