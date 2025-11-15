"""
You are given a binary string s.

Return the number of substrings with dominant ones.

A string has dominant ones if the number of ones in the string is greater than or equal to the square of the number of zeros in the string.

 

Example 1:

Input: s = "00011"

Output: 5

Explanation:

The substrings with dominant ones are shown in the table below.

i	j	s[i..j]	Number of Zeros	Number of Ones
3	3	1	0	1
4	4	1	0	1
2	3	01	1	1
3	4	11	0	2
2	4	011	1	2
Example 2:

Input: s = "101101"

Output: 16

Explanation:

The substrings with non-dominant ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non-dominant ones, it follows that there are 16 substrings with dominant ones.

i	j	s[i..j]	Number of Zeros	Number of Ones
1	1	0	1	0
4	4	0	1	0
1	4	0110	2	2
0	4	10110	2	3
1	5	01101	2	3
"""
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lens = len(s)
        res = 0
        i = 0
        first1 = -1
        while i < lens:
            if s[i] == '1':
                if first1 == -1:
                    first1 = i
                res += i - first1 + 1
            else:
                first1 = -1
            i += 1
        for zeroNum in range(1, int(sqrt(lens)) + 1):

            zeroPos = deque([]) 
            curZeroNum = 0
            firstZeroI = -1
            oneNum = 0          
            for r in range(lens):
                if s[r] == '0':
                    zeroPos.append(r)
                    curZeroNum += 1
                    if curZeroNum > zeroNum:
                        curZeroNum -= 1
                        oneNum -= zeroPos[0] - firstZeroI - 1
                        firstZeroI = zeroPos.popleft()
                else:
                    oneNum += 1
                if curZeroNum == zeroNum and oneNum >= zeroNum ** 2:
                    res += min(zeroPos[0] - firstZeroI, oneNum - zeroNum**2 + 1)
        return res

            