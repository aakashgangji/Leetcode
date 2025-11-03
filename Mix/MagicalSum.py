"""
You are given two integers, m and k, and an integer array nums.
A sequence of integers seq is called magical if:
seq has a size of m.
0 <= seq[i] < nums.length
The binary representation of 2seq[0] + 2seq[1] + ... + 2seq[m - 1] has k set bits.
The array product of this sequence is defined as prod(seq) = (nums[seq[0]] * nums[seq[1]] * ... * nums[seq[m - 1]]).
Return the sum of the array products for all valid magical sequences.
Since the answer may be large, return it modulo 109 + 7.
A set bit refers to a bit in the binary representation of a number that has a value of 1.
Example 1:
Input: m = 5, k = 5, nums = [1,10,100,10000,1000000]
Output: 991600007
Explanation:
All permutations of [0, 1, 2, 3, 4] are magical sequences, each with an array product of 1013.
Example 2:
Input: m = 2, k = 2, nums = [5,4,3,2,1]
Output: 170
Explanation:
The magical sequences are [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 4], [4, 0], [4, 1], [4, 2], and [4, 3].
Example 3:
Input: m = 1, k = 1, nums = [28]
Output: 28
Explanation:
The only magical sequence is [0].
"""
class Solution:
  def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
    MOD = 1_000_000_007

    @functools.lru_cache(None)
    def dp(m: int, k: int, i: int, carry: int) -> int:
      """
      Returns the number of magical sequences of length `k` that can be formed
      from the first `i` numbers in `nums` with at most `m` elements.
      """
      if m < 0 or k < 0 or (m + carry.bit_count() < k):
        return 0
      if m == 0:
        return int(k == carry.bit_count())
      if i == len(nums):
        return 0
      res = 0
      for count in range(m + 1):
        contribution = math.comb(m, count) * pow(nums[i], count, MOD) % MOD
        newCarry = carry + count
        res += dp(m - count, k - (newCarry % 2),
                  i + 1, newCarry // 2) * contribution
        res %= MOD
      return res

    return dp(m, k, 0, 0)
    