class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        l, r = 0, m
        
        while l <= r:
            i1 = (l + r) >> 1
            i2 = (m + n + 1) // 2 - i1
            l1 = nums1[i1 - 1] if i1 > 0 else float('-inf')
            l2 = nums2[i2 - 1] if i2 > 0 else float('-inf')
            r1 = nums1[i1] if i1 < m else float('inf')
            r2 = nums2[i2] if i2 < n else float('inf')
            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 ==1:
                    return max(l1,l2)
                else:
                    return ((max(l1,l2) + min(r1,r2)) / 2)
            elif r2 < l1:
                r = i1 - 1
            else:
                l = i1 + 1
        return 0


