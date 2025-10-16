# 15. 3Sum
"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[str]:
        res = []
        length = len(nums)

        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    a = nums[i]
                    b = nums[j]
                    c = nums[k]

                    triplet = f"{a} {b} {c}"
                    if a+b+c == 0 and triplet not in res:
                        res.append(triplet)

        return res

    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i-1] == nums[i]:
                continue

            low, high = i+1, n-1

            while low < high:
                summ = nums[i] + nums[low] + nums[high]

                if summ == 0:
                    res.append([nums[i], nums[low], nums[high]])
                    low, high = low + 1, high - 1

                    while low < high and nums[low] == nums[low-1]:
                        low += 1
                    while low < high and nums[high] == nums[high+1]:
                        high -= 1
                elif summ < 0:
                    low += 1
                else:
                    high -= 1

        return res

    def threeSum3(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1

            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res


test = Solution()

print(test.threeSum([-1, 0, 1, 2, -1, -4]))
print(test.threeSum2([-1, 0, 1, 2, -1, -4]))
print(test.threeSum3([-1, 0, 1, 2, -1, -4]))
