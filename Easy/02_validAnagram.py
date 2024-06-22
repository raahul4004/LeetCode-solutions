class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        
        # Check if the strings have the same length
        if len(s) != len(t):
            return False 

        # Count the occurrences of each character in the strings
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Check if the character counts are the same
        for i in countS:
            if countS[i] != countT.get(i, 0):
                return False

        # If all checks pass, the strings are anagrams
        return True
