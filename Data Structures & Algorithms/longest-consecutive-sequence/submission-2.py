class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_nums = list(set(nums))
        unique_nums.sort()
        res = 0
        count = 0
        for i in range(len(unique_nums)-1):
            if unique_nums[i+1] - unique_nums[i] == 1:
                count += 1
                if count > res:
                    res = count
            else:
                count = 0
        return res + 1