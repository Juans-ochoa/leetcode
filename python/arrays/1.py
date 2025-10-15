class Solution:
    def sumTwo(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # val:index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[n] = i


test = Solution()
print(test.sumTwo([2, 1, 5, 3], 4))
