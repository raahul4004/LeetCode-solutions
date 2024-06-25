class Solution:
 
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Iterate through the digits in reverse order.
        for i in reversed(range(len(digits))):
            # If the current digit is 9, set it to 0.
            if digits[i] == 9:
                digits[i] = 0
            # If the current digit is not 9, increment it by 1.
            else: 
                digits[i] += 1
                # Return the digits after incrementing by one.
                return digits
        # If all digits are 9, add a 1 at the beginning of the digits.
        return [1] + digits
        