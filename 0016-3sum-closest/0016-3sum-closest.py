class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        a=set()
        for x in range(1,len(nums)-1):
            l=0
            r=len(nums)-1
            while l<x and x<r:
                i=nums[l]+nums[x]+nums[r]
                if i<target:
                    l+=1
                else:
                    r-=1
                a.add(i)
        a=list(a)
        print(a)
        q=[]
        for i in range(len(a)):
            q.append(a[i]-target)
        q.sort()
        c=min(q,key=lambda x:(abs(x),-x))
        return c+target