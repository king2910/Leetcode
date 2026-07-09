class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char in '({[':
                if char=='(':
                    stack.append(1)
                elif char=='{':
                    stack.append(2)
                else:
                    stack.append(3)
            elif not stack:
                return False
            else:
                if char==')':
                    if stack[-1]==1:
                        stack.pop()
                    else:
                        return False
                elif char=='}':
                    if stack[-1]==2:
                        stack.pop()
                    else:
                        return False
                else:
                    if stack[-1]==3:
                        stack.pop()
                    else:
                        return False
        if not stack:
            return True
        else:
            return False        