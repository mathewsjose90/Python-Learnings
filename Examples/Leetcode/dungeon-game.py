'''

'''


class Solution:
    def calculateMinimumHP(self, dungeon):
        rows = len(dungeon)
        columns = len(dungeon[0])
        start_min_health = dungeon[0][0]
        min_health_seen_vs_total_health_in_path = {}

        def traverse(pos, current_min_health_seen, current_total):
            if pos == (rows - 1, columns - 1):
                current_total += dungeon[pos[0]][pos[1]]
                if current_total < current_min_health_seen:
                    current_min_health_seen = current_total
                min_health_seen_vs_total_health_in_path[current_min_health_seen] = current_total
                return
            next_pos_to_right = pos[1] + 1
            next_pos_to_down = pos[0] + 1
            # print(pos)

            current_total += dungeon[pos[0]][pos[1]]
            if current_total < current_min_health_seen:
                current_min_health_seen = current_total

            if next_pos_to_right <= columns - 1:
                traverse((pos[0], next_pos_to_right), current_min_health_seen, current_total)
            if next_pos_to_down <= rows - 1:
                traverse((next_pos_to_down, pos[1]), current_min_health_seen, current_total)

        traverse((0, 0), 0, 0)
        # print(min_health_seen_vs_total_health_in_path)
        min_healths = min_health_seen_vs_total_health_in_path.keys()
        if all([x > 0 for x in min_healths]):
            return 1
        return 1 + abs(max([x for x in min_healths if x <= 0]))
