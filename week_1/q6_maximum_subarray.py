class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = nums[0]
        total = 0
        for i in nums:
            if total < 0:
                total = 0

            total += i
            first = max(first, total)

        return first


if __name__ == "__main__":
    max_sub_array = Solution()
    print(max_sub_array.maxSubArray(
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
    print(max_sub_array.maxSubArray([1]))                       # Output: 1
    print(max_sub_array.maxSubArray(
        [5, 4, -1, 7, 8]))              # Output: 23
    print(max_sub_array.maxSubArray([-1, -2, -3]))                # Output: -1
