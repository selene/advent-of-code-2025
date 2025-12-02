# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1
    separator = "\n"

    # @answer(1026)
    def part_1(self) -> int:
        pos = 50
        zeroes = 0
        for move in self.input:
            if move[0] == 'L':
                pos = (pos - int(move[1:])) % 100
            else:
                pos = (pos + int(move[1:])) % 100
            
            if pos == 0:
                zeroes += 1
        return zeroes

    # @answer(1234)
    def part_2(self) -> int:
        pos = 50
        zeroes = 0
        
        for move in self.input:
            dist = int(move[1:])
            if move[0] == 'L':
                to_zero = 100 if pos == 0 else pos
                if dist >= to_zero:
                    zeroes += (dist - to_zero) // 100 + 1
                    print(f'From {pos}, {move} will reach 0 {(dist - to_zero) // 100 + 1} times')
                pos = (pos - dist) % 100
                    
            else:
                to_zero = 100 if pos == 100 else 100 - pos
                if dist >= to_zero:
                    zeroes += (dist - to_zero) // 100 + 1
                    print(f'From {pos}, {move} will reach 0 {(dist - to_zero) // 100 + 1} times')
                pos = (pos + dist) % 100
        return zeroes
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
