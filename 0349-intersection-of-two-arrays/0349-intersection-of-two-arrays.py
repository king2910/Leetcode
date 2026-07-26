class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set(nums1+nums2)
        for x in set(nums1):
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        for x in set(nums2):
            if x in s:
                s.remove(x)
            else:
                s.add(x)
        return list(s)