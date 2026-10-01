class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        p1={"(":0,"[":1,"{":2}
        p2={")":0,"]":1,"}":2}
        for char in s:
            if char in p1:
                stack.append(p1[char])
            else:
                if len(stack)==0:
                    return False
                if stack[-1]==p2[char]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0