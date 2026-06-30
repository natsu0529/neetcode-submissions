class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = 1
        zero = False
        for i in nums:
            if i ==0:
                zero = True           
                continue            
            a *= i
        if zero:
            b = 0
        else:
            b = a
        res = [ a if i == 0 else int(b / i) for i in nums]
        return res



        