class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=1
        r=[]
        for x in nums:
            p*=x
        for i in range(len(nums)):
            if nums[i]==0:
                t=1
                for j in range(len(nums)):
                    if i==j:
                        continue
                    else:
                        t*=nums[j]
                r.append(t)
            else:
                r.append(int(p/nums[i]))
        return r