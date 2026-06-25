class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        count = {}
        l = 0
        min_len = 1000
        ans_l, ans_r = 0, 0  
        for i in range(len(t)):
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            
        required = len(count_t)
        formed = 0
        for r in range(len(s)):
            char_r = s[r]
            count[char_r] = count.get(char_r, 0) + 1
            
            if char_r in count_t and count[char_r] == count_t[char_r]:
                formed += 1
                
            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    ans_l, ans_r = l, r
                
                char_l = s[l]
                count[char_l] -= 1
                
                if char_l in count_t and count[char_l] < count_t[char_l]:
                    formed -= 1
                l += 1 
        if min_len == 1000:
            return ""
        return s[ans_l:ans_r+1]