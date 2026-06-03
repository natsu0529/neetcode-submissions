class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(a.lower() for a in s if a.isalnum())
        return ss == ss[::-1]