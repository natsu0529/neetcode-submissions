class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        b = 1
        for i in nums:
            a *= i
            if i ==0:           
                continue            
            b *= i
        res = [ b if i == 0 else int(a / i) for i in nums]
        return res



        