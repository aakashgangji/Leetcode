"""Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 
Example 2:

Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
Example 3:

Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
"""
class Solution:
    def concatenatedBinary(self, n: int) -> int:

        # Define modulo constant to prevent integer overflow
        MOD = 10**9 + 7
      
        # Initialize result accumulator
        result = 0
      
        # Iterate through each number from 1 to n
        for current_num in range(1, n + 1):
            # Get the number of bits required to represent current_num
            num_bits = current_num.bit_length()

            result = ((result << num_bits) | current_num) % MOD
          
        return result
# Example usage:
solution = Solution()
print(solution.concatenatedBinary(1))  # Output: 1
print(solution.concatenatedBinary(3))  # Output: 27
print(solution.concatenatedBinary(12)) # Output: 505379714