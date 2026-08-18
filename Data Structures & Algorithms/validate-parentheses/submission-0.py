class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                bracket = stack.pop()
                if not ((c == ')' and bracket == '(') or (c == ']' and bracket == '[') or (c == '}' and bracket == '{')):
                    return False

        return True
