# 16. 3Sum Closest

"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i+1, n-1

            while lo < hi:
                curr_sum = nums[i] + nums[lo] + nums[hi]

                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum

                if curr_sum == target:
                    return curr_sum
                elif curr_sum < target:
                    lo += 1
                else:
                    hi -= 1

        return closest_sum
