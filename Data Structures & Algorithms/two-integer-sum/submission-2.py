class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,n in enumerate(nums):
            if (target - n) not in a:
                a[target - n] = i
            elif 2 * n == target:
                return [a[n],i]
            else:
                continue
            if n in a and a[n] != i:
                return [a[n],i]
