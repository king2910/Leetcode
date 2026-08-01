class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for c in range(len(nums1)):
            for i in range(len(nums2)):
                if nums2[i]==nums1[c]:
                    j=0
                    while j+i<len(nums2):
                        if nums2[i+j]>nums1[c]:
                            r.append(nums2[i+j])
                            break
                        j+=1
            if len(r)!=c+1:
                r.append(-1)
        return r        