# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    separator = ","

    # @answer(8576933996)
    def part_1(self) -> int:
        total = 0
        for rng in self.input:
            low, high = rng.split("-")
            for i in range(int(low), int(high) + 1):
                stri = str(i)
                length = len(stri)
                if length % 2 == 1:
                    continue
                if stri[:length//2] == stri[length//2:]:
                    total += i
            
        return total
            

    # @answer(25663320831)
    def part_2(self) -> int:
        total = 0
        for rng in self.input:
            lowstr, highstr = rng.split("-")
            for i in range(int(lowstr), int(highstr) + 1):
                stri = str(i)
                is_invalid = False
                for j in range(1, len(stri)//2 + 1):
                    num_subs = stri.count(stri[:j])
                    if num_subs * j == len(stri):
                        is_invalid = True
                        break
                if is_invalid:
                    total += i
                
        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
