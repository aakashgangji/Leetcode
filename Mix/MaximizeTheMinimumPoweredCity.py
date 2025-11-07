class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        def can_achieve_min_power(target_min_power: int, available_stations: int) -> bool:

            power_additions = [0] * (num_cities + 1)
            current_added_power = 0
          
            for city_idx in range(num_cities):
                # Update current added power based on difference array
                current_added_power += power_additions[city_idx]
              
                # Calculate power deficit for current city
                current_city_power = initial_power[city_idx] + current_added_power
                power_deficit = target_min_power - current_city_power
              
                if power_deficit > 0:
                    # Check if we have enough stations to cover the deficit
                    if available_stations < power_deficit:
                        return False
                  
                    # Greedily place new stations as far right as possible
                    # while still covering the current city
                    available_stations -= power_deficit
                  
                    # Find the rightmost position to place new stations
                    rightmost_position = min(city_idx + r, num_cities - 1)
                  
                    # Calculate the range affected by stations at rightmost_position
                    affected_start = max(0, rightmost_position - r)
                    affected_end = min(rightmost_position + r, num_cities - 1)
                  
                    # Update difference array to add power to affected range
                    power_additions[affected_start] += power_deficit
                    power_additions[affected_end + 1] -= power_deficit
                  
                    # Update current added power for this city
                    current_added_power += power_deficit
          
            return True
      
        num_cities = len(stations)
      
        # Calculate initial power for each city using difference array technique
        # Each station affects cities within range r
        power_diff = [0] * (num_cities + 1)
      
        for station_idx, station_power in enumerate(stations):
            # Calculate the range of cities affected by this station
            left_bound = max(0, station_idx - r)
            right_bound = min(station_idx + r, num_cities - 1)
          
            # Update difference array
            power_diff[left_bound] += station_power
            power_diff[right_bound + 1] -= station_power
      
        # Convert difference array to actual power values using prefix sum
        initial_power = list(accumulate(power_diff))
      
        # Binary search for the maximum achievable minimum power
        left, right = 0, 1 << 40  # Upper bound is 2^40 (large enough for the problem)
      
        while left < right:
            # Use upper mid to maximize the result
            mid = (left + right + 1) >> 1
          
            if can_achieve_min_power(mid, k):
                # Can achieve mid, try for higher minimum power
                left = mid
            else:
                # Cannot achieve mid, try lower values
                right = mid - 1
      
        return left