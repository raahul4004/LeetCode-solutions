class Solution:
    """
    This class represents a solution to the binary search problem.
    """

    def search(self, nums: List[int], target: int) -> int:
        
        # Initialize pointers to the leftmost and rightmost indices of the list
        l, r = 0, len(nums) - 1

        # Iterate until the pointers meet
        while l <= r:
            # Calculate the midpoint of the current range
            mid = (l + r) // 2

            # Check if the target is equal to the middle element
            if nums[mid] == target:
                return mid
            # Check if the target is less than the middle element
            elif nums[mid] < target:
                # Move the left pointer to the right of the middle
                l = mid + 1
            # If the target is greater than the middle element, move the right pointer to the left of the middle
            else:
                r = mid - 1

        # If the target is not found, return -1
        return -1
                   