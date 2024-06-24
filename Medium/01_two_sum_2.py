
##### TWO SUM 2 - Input array is sorted 
class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize pointers to the beginning and end of the array.
        l, r = 0, len(numbers) - 1

        # Iterate through the array until the pointers meet.
        while l < r:
            
            # Calculate the sum of the numbers at the current pointers.
            curSum = numbers[l] + numbers[r]

            # If the sum is less than the target, increment the left pointer.
            if curSum < target:
                l += 1
            # If the sum is greater than the target, decrement the right pointer.
            elif curSum > target:
                r -= 1
            # If the sum is equal to the target, return the indices.
            else:
                return [l+1, r+1]
