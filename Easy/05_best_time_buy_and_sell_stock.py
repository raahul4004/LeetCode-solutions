class Solution:
    """
    This class represents a solution to the best time to buy and sell stock problem.
    """

    def maxProfit(self, prices: List[int]) -> int:
        
        # Initialize variables
        maxP = 0  # Maximum profit so far
        l = 0  # Index of the leftmost element in the current interval

        # Iterate through the prices list
        for r in range(1, len(prices)):
            # Calculate the profit of buying and selling at the current index
            profit = prices[r] - prices[l]

            # If the profit is negative, move the left index to the current index
            if profit < 0:
                l = r

            # Update the maximum profit if the current profit is greater
            maxP = max(profit, maxP)
        
        return maxP