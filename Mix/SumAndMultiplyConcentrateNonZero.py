"""
You are given a string s of length m consisting of digits. You are also given a 2D integer array queries, where queries[i] = [li, ri].

For each queries[i], extract the substring s[li..ri]. Then, perform the following:

Form a new integer x by concatenating all the non-zero digits from the substring in their original order. If there are no non-zero digits, x = 0.
Let sum be the sum of digits in x. The answer is x * sum.
Return an array of integers answer where answer[i] is the answer to the ith query.

Since the answers may be very large, return them modulo 109 + 7.

 

Example 1:

Input: s = "10203004", queries = [[0,7],[1,3],[4,6]]

Output: [12340, 4, 9]

Explanation:

s[0..7] = "10203004"
x = 1234
sum = 1 + 2 + 3 + 4 = 10
Therefore, answer is 1234 * 10 = 12340.
s[1..3] = "020"
x = 2
sum = 2
Therefore, the answer is 2 * 2 = 4.
s[4..6] = "300"
x = 3
sum = 3
Therefore, the answer is 3 * 3 = 9.
Example 2:

Input: s = "1000", queries = [[0,3],[1,1]]

Output: [1, 0]

Explanation:

s[0..3] = "1000"
x = 1
sum = 1
Therefore, the answer is 1 * 1 = 1.
s[1..1] = "0"
x = 0
sum = 0
Therefore, the answer is 0 * 0 = 0.
Example 3:

Input: s = "9876543210", queries = [[0,9]]

Output: [444444137]

Explanation:

s[0..9] = "9876543210"
x = 987654321
sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45
Therefore, the answer is 987654321 * 45 = 44444444445.
We return 44444444445 modulo (109 + 7) = 444444137
"""
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)

        # Preprocess non-zero digits
        nz = []
        nz_sum = []
        pow10 = [1]  # powers of 10 modulo MOD
        curr_x = [0]  # prefix mod-X value
        
        for i in range(m):
            if s[i] != '0':
                nz.append(i)
                val = int(s[i])
                nz_sum.append((nz_sum[-1] if nz_sum else 0) + val)
                pow10.append((pow10[-1] * 10)%MOD)
                curr_x.append((curr_x[-1]*10 + val)%MOD)
        
        from bisect import bisect_left, bisect_right
        ans = []
        nzn = len(nz)
        
        for l, r in queries:
            left = bisect_left(nz, l)
            right = bisect_right(nz, r)
            k = right - left
            if k == 0:
                ans.append(0)
            else:
                # Get x in range
                x_val = (curr_x[right] - curr_x[left]*pow10[k]) % MOD
                digit_sum = (nz_sum[right-1] - (nz_sum[left-1] if left > 0 else 0)) % MOD
                ans.append((x_val * digit_sum)%MOD)
        return ans

sol=Solution()
print(sol.sumAndMultiply("10203004", [[0,7],[1,3],[4,6]]))  # Output: [12340, 4, 9]
print(sol.sumAndMultiply("1000", [[0,3],[1,1]]))  # Output: [1, 0]
print(sol.sumAndMultiply("9876543210", [[0,9]]))  # Output: [444444137] 