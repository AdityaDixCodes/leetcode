#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):

            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i
            else:
                left_sum += nums[i]
        return -1
            

        

        

        
# @lc code=end

