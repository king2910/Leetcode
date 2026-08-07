class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r=[]
        for x in nums1:
            if x in nums2:
                r.append(x)
                nums2.remove(x)
        return r