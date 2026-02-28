class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        Calculate the decimal value of the binary concatenation of integers from 1 to n.
      
        For example, if n = 3:
        - Binary of 1 is "1"
        - Binary of 2 is "10" 
        - Binary of 3 is "11"
        - Concatenated: "11011" which equals 27 in decimal
      
        Args:
            n: The upper limit of integers to concatenate (1 to n)
          
        Returns:
            The decimal value of concatenated binary representation modulo 10^9 + 7
        """
        # Define modulo constant to prevent integer overflow
        MOD = 10**9 + 7
      
        # Initialize result accumulator
        result = 0
      
        # Iterate through each number from 1 to n
        for current_num in range(1, n + 1):
            # Get the number of bits required to represent current_num
            num_bits = current_num.bit_length()
          
            # Left shift result by num_bits positions to make room for current_num
            # Then use bitwise OR to append current_num's binary representation
            # Apply modulo to keep the number within bounds
            result = ((result << num_bits) | current_num) % MOD
          
        return result