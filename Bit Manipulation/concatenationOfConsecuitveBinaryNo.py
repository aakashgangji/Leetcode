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