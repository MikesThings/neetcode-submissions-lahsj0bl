class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '[' }
        stack = []
        for i in s: 
            if i not in bracket_map: 
                stack.append(i)
                continue
            if not stack or stack[-1] != bracket_map[i]:
                return False
            stack.pop()

        return not stack