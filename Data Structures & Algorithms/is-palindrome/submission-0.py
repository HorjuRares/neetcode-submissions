class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0

        s = "".join(ch.lower() if ch.isalnum() else "" for ch in s)
        n = len(s)

        while i < (n / 2):
            if s[i] != s[n - 1 - i]: return False
            i += 1

        return True