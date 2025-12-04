# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from collections import defaultdict, namedtuple
from copy import deepcopy


from ...base import StrSplitSolution, answer


class TileContent:
    ROLL = '@'
    FLOOR = '.'
    FORKLIFT = 'x'

class Tile:
    def __init__(self, row, column, content, neighbors):
        self.row = row
        self.column = column
        self.content = content
        self.neighbors = neighbors or [None] * 8

Pos = namedtuple('Pos', ['row', 'col'])

def add_pos(pos1, pos2):
  return Pos(pos1.row + pos2.row, pos1.col + pos2.col)

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
        
        return grid
    
    def find_removable_rolls(self, grid, height, width):
        removable = []
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
                    removable.append(Pos(ridx, cidx))
        return removable
                    

    # @answer(1234)
    def part_1(self) -> int:
        grid = self.make_grid()
        
        height = len(self.input)
        width = len(self.input[0])
        
        grid2 = deepcopy(grid)
        liftable_spaces = 0
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
                    grid2[ridx][cidx] = TileContent.FORKLIFT
                    liftable_spaces += 1
        
        print_map(grid2)
        return liftable_spaces

    # @answer(1234)
    def part_2(self) -> int:
        grid = self.make_grid()

        height = len(self.input)
        width = len(self.input[0])
        
        
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
