class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        count = 0
        for i in nums:
            if i ==0:
                count += 1
                continue
            a *= i
        if 0 < count < 2:
            res = [a if i == 0 else 0 for i in nums]
        elif count == 0:
            res = [int( a / i )for i in nums]
        else:
            res = [ 0 for i in range(len(nums))]
        return res



        