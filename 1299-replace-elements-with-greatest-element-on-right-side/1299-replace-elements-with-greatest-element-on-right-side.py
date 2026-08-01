class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr)==1:
            return [-1]
        m=max(arr[1:])
        r=[m]
        for i in range(1,len(arr)):
            if i==len(arr)-1:
                r.append(-1)
            else:
                if arr[i]!=m:
                    r.append(m)
                else:
                    m=max(arr[i+1:])
                    r.append(m)
        return r