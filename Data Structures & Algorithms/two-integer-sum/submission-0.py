class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i,n in enumerate(nums):
            a[target - n] = i
            if n in a and a[n] != i:
                return [a[n],i]


            
