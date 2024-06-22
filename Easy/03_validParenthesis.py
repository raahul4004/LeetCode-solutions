class Solution:

    def isValid(self, s: str) -> bool:
        # Mapping of closing brackets to their corresponding opening brackets
        closeToOpen={"}": "{", ")": "(", "]": "["}
        
        # Stack to store opening brackets
        stack = []
        
        # Iterate through each character in the input string
        for c in s:
            
            # If the character is a closing bracket
            if c in closeToOpen:
                # If the stack is not empty and the top of the stack is the corresponding opening bracket, pop the top
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # If the stack is empty or the top of the stack is not the corresponding opening bracket, return False
                else:
                    return False 
            # If the character is an opening bracket, push it onto the stack
            else: 
                stack.append(c)
        
        # If the stack is empty, the input string is valid
        return True if not stack else False
