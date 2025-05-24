import sys

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxsize
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        
        return max_profit
    
if __name__ == "__main__":
    max_profit = Solution()
    print(max_profit.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
    print(max_profit.maxProfit([7, 6, 4, 3, 1]))     # Output: 0
    print(max_profit.maxProfit([2, 4, 1]))           # Output: 2
    print(max_profit.maxProfit([1, 2]))              # Output: 1
    print(max_profit.maxProfit([2, 1]))              # Output: 0