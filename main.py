from random import randint
from collections import deque

ROW = 5
COLUMN = 5

class Main:

    def __init__(self) -> None:
        self.grid = [[0 for _ in range(ROW)] for _ in range(COLUMN) ]
        self.visited = set()
        self.monkey_pos, self.chair, self.stick, self.banana = (0, 0), (0, 0), (0, 0), (0, 0)

    def set_location_object(self):
        # set the chair as number 1, stick as number 2 and bananas as number 3
        self.grid[randint(0, ROW - 1)][randint(0, COLUMN - 1)] = 1
        self.grid[randint(0, ROW - 1)][randint(0, COLUMN - 1)] = 2
        self.grid[randint(0, ROW - 1)][randint(0, COLUMN - 1)] = 3

    def bfs(self, rows, columns):
        queue = deque()
        self.visited.add((rows, columns))
        queue.append((rows, columns))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            temp_row, temp_column = queue.popleft()
            for direct_row, direct_column in directions:
                r, c = temp_row + direct_row, temp_column + direct_column
                if (r not in range(ROW) 
                        or c not in range(COLUMN)):
                    continue

                if (self.grid[r][c] == 0
                        and (r, c) not in self.visited):
                    queue.append((r, c))
                    self.visited.add((r, c))

                if self.grid[r][c] == 1:
                    self.chair = (r, c)
                if self.grid[r][c] == 2:
                    self.stick = (r, c)
                if self.grid[r][c] == 3:
                    self.banana = (r, c)
                if self.chair != (0, 0) and self.stick != (0, 0) and self.banana != (0, 0):
                    break
                

    # def movement(self):
    #     number_to_go = 0
    #     for cur_row, cur_column in self.monkey_pos:


    def isValid(self, rows, columns):
        for row in range(rows):
            for column in range(columns):
                if (self.grid[row][column] == 0
                        and (row, column) not in self.visited):
                    self.bfs(row, column)

if __name__ == "__main__":
    play = Main()
    play.set_location_object()
    print(play.grid)
    play.bfs(0, 0)
    print(play.banana, play.chair, play.stick)

