class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range (len(nums) - 1):
            if 0 < i and nums[i] == nums[i - 1]:
                continue
            r = len(nums) - 1
            l = i + 1
            while r > l:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while 0 < r and nums[r] == nums[r - 1]:
                        r -= 1
                    while l < len(nums - 1) and nums[l] == nums[l + 1]:
                        l -= 1

                    l += 1
                    r -= 1
        return res