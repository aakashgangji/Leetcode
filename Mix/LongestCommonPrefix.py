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
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        first=strs
        for i, char in enumerate(strs[0]):
            for other_str in strs[1:]:
                if i>=len(other_str) or other_str[i]!=char:
                    return strs[0][:i]

        return strs[0]
