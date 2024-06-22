class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating a Hashmap to store the previos visited values 
        prevMap = {} # {list_element: index}

        for i in range(len(nums)):
            
            # Calculating the difference between the target and the element currently we're on
            diff = target - nums[i]
            if diff in prevMap: # if the difference is found in the hashMap then returning the indices
                return [prevMap[diff], i]
            # else making the current element to the hashmap
            prevMap[nums[i]] = i