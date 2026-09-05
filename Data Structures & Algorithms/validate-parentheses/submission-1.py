class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        front = ['(', '[', '{']
        end = [')', ']', '}']

        for char in s:
            if char in front:
                stack.append(char)
            elif char in end and len(stack) > 0:
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            else:
                return False
        
        return len(stack) == 0