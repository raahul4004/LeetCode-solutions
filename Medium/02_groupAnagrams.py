class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Create a hash map to store the anagrams.
        hashMap = defaultdict(list)

        # Iterate through each string.
        for s in strs:

            # Create a count array to store the frequency of each character in the string.
            count = [0] * 26
            for c in s:
                # Increment the count of the character.
                count[ord(c) - ord('a')] += 1

            # Use the count array as the key to the hash map and store the string.
            hashMap[tuple(count)].append(s)

        # Return the values of the hash map, which are the anagrams grouped together.
        return hashMap.values()
