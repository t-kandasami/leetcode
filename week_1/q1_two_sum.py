class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # n^2 solution
        for i in range(len(nums)): 
            for j in range(len(nums) - 1): 
                first_digit = nums[i]
                second_digit = nums[j+1]
                if (first_digit+second_digit == target):
                    return [i, j+1]

if __name__ == "__main__":
    two_sum = Solution()
    print(two_sum.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]