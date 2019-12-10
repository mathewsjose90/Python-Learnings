'''
https://leetcode.com/problems/battleships-in-a-board/

X..X
...X
...X

Ans: 2
'''


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x_positions = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == 'X':
                    x_positions.append((i, j))
        ship_count = 0
        rows = len(board)
        columns = len(board[0])
        for x, y in x_positions:
            while y < columns:
                if (x, y + 1) in x_positions:
                    x_positions.remove((x, y + 1))
                    y += 1
                else:
                    break;
            while x < rows:
                if (x + 1, y) in x_positions:
                    x_positions.remove((x + 1, y))
                    x += 1
                else:
                    break
        return len(x_positions)


s = Solution()
print(s.countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
print(s.countBattleships([["X", ".", ".", "X"], [".", ".", ".", "."], [".", ".", ".", "X"]]))
