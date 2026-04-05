class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stack = []
        for i in range(len(a)):
            while stack and a[i] < 0 and stack[-1] > 0:
                diff = stack[-1] + a[i]
                if diff < 0:
                    stack.pop()
                elif diff == 0:
                    a[i] = 0
                    stack.pop()
                else:
                    a[i] = 0
            if a[i]:
                stack.append(a[i])
        return stack