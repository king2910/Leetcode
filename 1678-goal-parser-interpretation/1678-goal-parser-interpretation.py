class Solution:
    def interpret(self, command: str) -> str:
        r=''
        c=0
        for x in command:
            if x=='G':
                r+='G'
            elif x=='(' or x=='a' or x=='l':
                c+=1
            else:
                if c==1:
                    r+='o'
                else:
                    r+='al'
                c=0
        return r