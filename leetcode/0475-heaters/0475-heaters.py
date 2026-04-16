class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        def find_closest_heater(house: int) -> int:
            left, right = 0, len(heaters) - 1
            closest = float('inf')
            
            while left <= right:
                mid = (left + right) // 2
                dist = abs(heaters[mid] - house)
                closest = min(closest, dist)
                
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            return closest

        houses.sort()
        heaters.sort()
        max_radius = 0

        for house in houses:
            radius = find_closest_heater(house)
            max_radius = max(max_radius, radius)

        return max_radius