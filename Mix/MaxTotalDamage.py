"""
A magician has various spells.
You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.
It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.
Each spell can be cast only once.
Return the maximum possible total damage that a magician can cast.
Example 1:
Input: power = [1,1,3,4]
Output: 6
Explanation:
The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.
Example 2:
Input: power = [7,1,6,6]
Output: 13
Explanation:
The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.
"""

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        """
        Calculate the maximum total damage that can be achieved.
        When selecting a power value, all values within range [power-2, power+2] become unavailable.
      
        Args:
            power: List of power values
          
        Returns:
            Maximum total damage achievable
        """
      
        @cache
        def calculate_max_damage(index: int) -> int:
            """
            Recursively calculate maximum damage starting from given index.
          
            Args:
                index: Current position in sorted power array
              
            Returns:
                Maximum damage achievable from this position onwards
            """
            # Base case: reached end of array
            if index >= array_length:
                return 0
          
            # Option 1: Skip current power value and all its duplicates
            skip_current = calculate_max_damage(index + power_count[sorted_power[index]])
          
            # Option 2: Take current power value (and all duplicates)
            # Then skip to next valid position (beyond power+2 range)
            current_damage = sorted_power[index] * power_count[sorted_power[index]]
            take_current = current_damage + calculate_max_damage(next_valid_index[index])
          
            # Return maximum of both options
            return max(skip_current, take_current)
      
        # Initialize variables
        array_length = len(power)
      
        # Count frequency of each power value
        power_count = Counter(power)
      
        # Sort power values for efficient processing
        sorted_power = sorted(power)
      
        # Pre-compute next valid index for each position
        # Next valid index is the first position where power > current_power + 2
        next_valid_index = [
            bisect_right(sorted_power, value + 2, lo=i + 1) 
            for i, value in enumerate(sorted_power)
        ]
      
        # Start dynamic programming from index 0
        return calculate_max_damage(0)
        