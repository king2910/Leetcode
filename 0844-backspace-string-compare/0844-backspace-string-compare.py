class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        for x in s:
            if x=="#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(x)
        for x in t:
            if x=="#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(x)
        return stack1==stack2 