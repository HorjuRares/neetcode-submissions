from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            '(' : ')', 
            '{' : '}',
            '[' : ']',
        }

        stack = deque()

        for ch in s:
            if ch in matches.keys():
                stack.append(ch)
            elif len(stack) > 0:
                if ch != matches[stack.pop()]:
                    return False
            else:
                return False

        if len(stack) > 0:
            return False

        return True