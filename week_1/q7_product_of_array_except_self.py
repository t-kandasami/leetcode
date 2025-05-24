class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1] * len(nums)
        left = 1
        for i in range(len(nums)):
            output[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, - 1, -1):
            output[i] *= right
            right *= nums[i]

        return output


if __name__ == "__main__":
    product_except_self = Solution()
    print(product_except_self.productExceptSelf(
        [1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
    print(product_except_self.productExceptSelf(
        [0, 1]))        # Output: [1, 0]
    print(product_except_self.productExceptSelf(
        [-1, 1, 0, -3, 3]))  # Output: [0, 0, 9, 0, 0]
