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
        # order the cars based on the distance from the target.
        ordered_pos = sorted(zip(position, speed), reverse=True)
        # find the remaining time needed to reach the target for each cars
        remaining_time_for_each_car = [(target - x) / y for x, y in ordered_pos]
        total_cars = len(position)
        fleet_count = 0
        i = 0
        while i < total_cars:
            # Only 1 car is remaining
            if i == (total_cars - 1):
                fleet_count += 1
                break
            next_pos_to_visit = i + 1
            # Club all the cars whose time to reach target is less than the current car at ith position (as all they have to go together)
            while next_pos_to_visit <= (total_cars - 1) and remaining_time_for_each_car[next_pos_to_visit] <= \
                    remaining_time_for_each_car[next_pos_to_visit - 1]:
                next_pos_to_visit += 1
            # Club all the cars whose remaining_time is greater than the previous car position , but less than the current car at ith position .
            while next_pos_to_visit <= (total_cars - 1) and remaining_time_for_each_car[next_pos_to_visit] <= \
                    remaining_time_for_each_car[i]:
                next_pos_to_visit += 1
            i = next_pos_to_visit
            fleet_count += 1

        return fleet_count


s = Solution()
print(s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
