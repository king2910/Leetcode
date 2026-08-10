class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for i in range(len(operations)):
            if operations[i]=="D":
                s.append(s[-1]*2)
            elif operations[i]=="C":
                s.pop()
            elif operations[i]=="+":
                s.append(s[-1]+s[-2])
            else:
                s.append(int(operations[i]))
        return sum(s)