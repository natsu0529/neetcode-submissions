class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,n in enumerate(nums):
            if target - n in a:
                return [a[target - n],i]
            a[n] = i