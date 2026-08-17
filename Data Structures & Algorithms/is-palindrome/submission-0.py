class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed = "".join(char.lower() for char in s if char.isalnum())
        i=0
        j=len(trimmed)-1
        while i<=j:
            if trimmed[i]!=trimmed[j]:
                return False
            i+=1
            j-=1
        return True