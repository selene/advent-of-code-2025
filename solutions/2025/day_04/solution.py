# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from collections import defaultdict, namedtuple
from copy import deepcopy


from ...base import StrSplitSolution, answer


class TileContent:
    ROLL = '@'
    FLOOR = '.'

Pos = namedtuple('Pos', ['row', 'col'])

DIRECTIONS = [
    Pos(0, 1),   # right >
    Pos(1, 1),   # down-right \
    Pos(1, 0),   # down v
    Pos(1, -1),  # down-left /
    Pos(0, -1),  # left <
    Pos(-1, -1), # up-left \
    Pos(-1, 0),  # up ^
    Pos(-1, 1),  # up-right /
]

   
def print_map(grid):
    for r in range(0, max(grid.keys())+1):
        for c in range(0, max(grid[r].keys())+1):
            print(grid[r][c], end='')
        print()


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4    
    separator = "\n"


    def make_grid(self):
        grid = defaultdict(lambda: defaultdict(lambda: TileContent.FLOOR))
        
        for ridx, line in enumerate(self.input):
            for cidx, char in enumerate(line):
                grid[ridx][cidx] = char
        
        height = len(self.input)
        width = len(self.input[0])
        return grid, height, width
    
    def find_removable_rolls(self, grid, height, width):
        removables = []
        for ridx in range(height):
            for cidx in range(width):
                if grid[ridx][cidx] == TileContent.FLOOR:
                    continue
                roll_count = 0
                for d in DIRECTIONS:
                    neighbor = grid[d.row + ridx][d.col + cidx]
                    if neighbor == TileContent.ROLL:
                        roll_count += 1
                if roll_count < 4:
                    removables.append(Pos(ridx, cidx))
        return removables
                    

    # @answer(1489)
    def part_1(self) -> int:
        grid, height, width = self.make_grid()
        
        return len(self.find_removable_rolls(grid, height, width))

    # @answer(8890)
    def part_2(self) -> int:
        grid, height, width = self.make_grid()

        removed = 0
        while True:
            removables = self.find_removable_rolls(grid, height, width)
            if not removables:
                break
            for pos in removables:
                grid[pos.row][pos.col] = TileContent.FLOOR
                removed += 1
        
        return removed
        
        
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
