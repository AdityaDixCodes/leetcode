#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        
        write = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        
        for j in range(write, len(nums)):
            nums[j] = 0
        

# @lc code=end

