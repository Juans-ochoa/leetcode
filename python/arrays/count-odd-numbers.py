class Solution:
    def countOddNumbers(self, low: int, height: int) -> int:
        count = 0
        for i in range(low, height+1):
            if (i % 2 != 0):
                count += 1

        return count

    def countOddNumbers2(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2


solution = Solution()
print(solution.countOddNumbers(1, 5))
print(solution.countOddNumbers2(1, 5))
