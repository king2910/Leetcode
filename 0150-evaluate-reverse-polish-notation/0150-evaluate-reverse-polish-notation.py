class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i not in '+-*/':
                s.append(i)
            else:
                r=int(s.pop())
                l=int(s.pop())
                if i == '+':
                    s.append(l+r)
                elif i == '-':
                    s.append(l-r)
                elif i == '*':
                    s.append(l*r)
                else:
                    s.append(l/r)
        return int(s[0])