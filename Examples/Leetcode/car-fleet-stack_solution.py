'''
https://leetcode.com/problems/car-fleet/
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
'''


class Solution:
    def carFleet(self, target: int, position, speed):
        sorted_car_pos = sorted(zip(position, speed), reverse=True)
        time_needed_to_reach_target = [(target - x) / y for x, y in sorted_car_pos]
        fleet_count = 0
        while len(time_needed_to_reach_target) > 1:
            t = time_needed_to_reach_target.pop()
            if t > time_needed_to_reach_target[-1]:
                fleet_count += 1
            else:
                time_needed_to_reach_target[-1] = t
        return fleet_count + bool(time_needed_to_reach_target)


s = Solution()
print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
