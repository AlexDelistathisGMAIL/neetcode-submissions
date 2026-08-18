class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            isDigit = None
            if token.startswith("-"):
                isDigit = token[1:].isdigit()
            else:
                isDigit = token.isdigit()
            
            if isDigit:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    stack.append(first + second)
                elif token == "-":
                    stack.append(first - second)
                elif token == "*":
                    stack.append(first * second)
                else:
                    stack.append(first // second)
        
        return stack[-1]
        