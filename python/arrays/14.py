# 14. Longest Common Prefix
"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ''

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            res += strs[0][i]

        return res

    def longestCommonPrefix2(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]

                if not prefix:
                    return ''
        return prefix


test = Solution()

test.longestCommonPrefix2(["flower", "flow", "flight"])
