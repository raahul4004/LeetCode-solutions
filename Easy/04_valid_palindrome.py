class Solution:
   

    def isPalindrome(self, s: str) -> bool:
     
        l, r = 0, len(s) - 1
        # Initialize pointers to the beginning and end of the string.
        while l < r:
            
            # Skip non-alphanumeric characters. for l pointer
            while l < r and not self.isalnum(s[l]):
                l += 1

            # Skip non-alphanumeric characters. for r pointer
            while r > l and not self.isalnum(s[r]):
                r -= 1
            
            # Check if the characters at the pointers are equal.
            if s[l].lower() != s[r].lower():
                return False 
            l, r = l + 1, r - 1
        return True
    


    def isalnum(self, c):
        # returning true if c is alphanumeric else false 
        return ((ord('A') <= ord(c) <= ord('Z')) or
           (ord('a') <= ord(c) <= ord('z')) or
           (ord('0') <= ord(c) <= ord('9')))
