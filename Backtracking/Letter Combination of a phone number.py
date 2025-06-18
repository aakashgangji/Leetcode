from typing import List
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = ""
# Output: []
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        dtc={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def backtrack(i,curstr):
            if len(curstr)==len(digits):
                res.append(curstr)
                return
            for c in dtc[digits[i]]:
                backtrack(i+1,curstr+c)
        if digits:
            backtrack(0,"")
        return res
            

digits = "23"
sol=Solution()
print(sol.letterCombinations(digits))