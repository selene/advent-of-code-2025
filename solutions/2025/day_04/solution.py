# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/4

from collections import defaultdict, namedtuple


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

class Grid:
    def __init__(self, input_chars):
        self.grid = defaultdict(lambda: defaultdict(lambda: TileContent.FLOOR))
        
        for ridx, line in enumerate(input_chars):
            for cidx, char in enumerate(line):
                self.grid[ridx][cidx] = char
        
        self.height = len(input_chars)
        self.width = len(input_chars)
    
    def print_grid(self):
        for r in range(0, max(self.grid.keys())+1):
            for c in range(0, max(self.grid[r].keys())+1):
                print(self.grid[r][c], end='')
            print()
    
    def at(self, row, col):
        return self.grid[row][col]
    
    def set_tile(self, row, col, tile):
        self.grid[row][col] = tile
    
    def tiles(self):
        for ridx in range(self.height):
            for cidx in range(self.width):
                yield self.grid[ridx][cidx], ridx, cidx


class Solution(StrSplitSolution):
    _year = 2025
    _day = 4    
    separator = "\n"


    def load_grid(self):
        return Grid(self.input)
    
    def find_removable_rolls(self, grid: Grid):
        removables = []
        for tile, ridx, cidx in grid.tiles():
            if tile == TileContent.FLOOR:
                continue
            roll_count = 0
            for d in DIRECTIONS:
                neighbor = grid.at(d.row + ridx, d.col + cidx)
                if neighbor == TileContent.ROLL:
                    roll_count += 1
            if roll_count < 4:
                removables.append(Pos(ridx, cidx))
        return removables
                    

    # @answer(1489)
    def part_1(self) -> int:
        grid = self.load_grid()
        
        return len(self.find_removable_rolls(grid))

    # @answer(8890)
    def part_2(self) -> int:
        grid = self.load_grid()

        removed = 0
        while True:
            removables = self.find_removable_rolls(grid)
            if not removables:
                break
            for pos in removables:
                grid.set_tile(pos.row, pos.col, TileContent.FLOOR)
                removed += 1
        
        return removed
        
        
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
